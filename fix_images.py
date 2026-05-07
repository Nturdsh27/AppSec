"""
Fix mismatched images in markdown files by extracting correct images
from docx files and replacing the attachment_N.png files.

For each docx/folder pair:
  1. Extract images from docx in document order
  2. Collect all attachment_N references across the folder's .md files, sorted by N
  3. Map docx_image[i] -> attachment_N[i] and overwrite the file
"""

import zipfile
import xml.etree.ElementTree as ET
import os
import re
import shutil
from pathlib import Path

BASE = Path(r"c:\Users\gedim\Downloads\AppSec-Hafifa-main\AppSec-Hafifa")
DOCX_DIR = BASE / "docx_files"
ATTACHMENTS = BASE / "Attachments"

# Map docx filename -> folder name (relative to BASE)
DOCX_TO_FOLDER = {
    "CICD.docx":             "CI-CD",
    "Cloud Providers.docx":  "ספקי ענן",
    "DevSecOps.docx":        "DevSecOps",
    "Git & Github.docx":     "GIT & GITHUB",
    "Linux.docx":            "Linux",
    "Networking.docx":       "רשתות",
    "Security.docx":         "Security",
    "Virtualization.docx":   "וירטואליזציה",
}

NSMAP = {
    'a':  'http://schemas.openxmlformats.org/drawingml/2006/main',
    'r':  'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
    'rel':'http://schemas.openxmlformats.org/package/2006/relationships',
}


def get_image_order_from_docx(docx_path):
    """Return list of image bytes in the order they appear in the document."""
    with zipfile.ZipFile(docx_path, 'r') as z:
        # Build rId -> media filename map
        rels_xml = z.read('word/_rels/document.xml.rels')
        rels_root = ET.fromstring(rels_xml)
        rid_to_media = {}
        for rel in rels_root:
            rid = rel.get('Id')
            target = rel.get('Target')
            rtype = rel.get('Type', '')
            if 'image' in rtype and target:
                # Target may be "/media/image.png" (absolute) or "media/image.png" (relative)
                # Strip leading slash; images live at top-level "media/" in this docx format
                clean = target.lstrip('/')
                rid_to_media[rid] = clean

        # Walk document.xml in order, collect blip embeds
        doc_xml = z.read('word/document.xml')
        doc_root = ET.fromstring(doc_xml)

        ordered_images = []
        seen = set()
        for elem in doc_root.iter():
            tag = elem.tag
            # <a:blip r:embed="rId6"/>
            if tag == f'{{{NSMAP["a"]}}}blip':
                rid = elem.get(f'{{{NSMAP["r"]}}}embed')
                if rid and rid in rid_to_media:
                    media_path = rid_to_media[rid]
                    if media_path not in seen:
                        seen.add(media_path)
                        try:
                            img_bytes = z.read(media_path)
                            ordered_images.append((media_path, img_bytes))
                        except KeyError:
                            print(f"  WARNING: {media_path} not found in zip (files: {z.namelist()[:5]})")

        return ordered_images


def get_attachment_refs_from_folder(folder_path):
    """Return sorted list of attachment numbers referenced in all .md files in folder."""
    refs = set()
    for md_file in Path(folder_path).glob('*.md'):
        content = md_file.read_text(encoding='utf-8', errors='ignore')
        for m in re.findall(r'attachment_(\d+)', content):
            refs.add(int(m))
    return sorted(refs)


def process(docx_name, folder_name):
    docx_path = DOCX_DIR / docx_name
    folder_path = BASE / folder_name

    if not docx_path.exists():
        print(f"SKIP: {docx_name} not found")
        return
    if not folder_path.exists():
        print(f"SKIP: folder {folder_name} not found")
        return

    print(f"\n=== {docx_name} -> {folder_name} ===")

    images = get_image_order_from_docx(docx_path)
    attachment_nums = get_attachment_refs_from_folder(folder_path)

    print(f"  docx images:       {len(images)}")
    print(f"  md attachment refs: {len(attachment_nums)}")

    if len(images) != len(attachment_nums):
        print(f"  WARNING: count mismatch! docx={len(images)}, md={len(attachment_nums)}")
        count = min(len(images), len(attachment_nums))
        print(f"  Will map first {count} pairs.")
    else:
        count = len(images)

    replaced = 0
    for i in range(count):
        media_path, img_bytes = images[i]
        att_num = attachment_nums[i]
        dest = ATTACHMENTS / f"attachment_{att_num}.png"

        # Get extension from source
        ext = Path(media_path).suffix.lower()
        if ext not in ('.png', '.jpg', '.jpeg', '.gif', '.webp', '.bmp'):
            ext = '.png'

        dest_with_ext = ATTACHMENTS / f"attachment_{att_num}{ext}"
        dest_with_ext.write_bytes(img_bytes)

        # If the md references it as .png but docx image is .jpg, also write a .png copy
        if ext != '.png':
            dest.write_bytes(img_bytes)

        replaced += 1

    print(f"  Replaced {replaced} images.")


def main():
    print("Backing up Attachments folder...")
    backup = ATTACHMENTS.parent / "Attachments_backup"
    if not backup.exists():
        shutil.copytree(ATTACHMENTS, backup)
        print(f"  Backup saved to: {backup}")
    else:
        print("  Backup already exists, skipping.")

    for docx_name, folder_name in DOCX_TO_FOLDER.items():
        process(docx_name, folder_name)

    print("\nDone.")


if __name__ == '__main__':
    main()

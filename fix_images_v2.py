"""
Fix images using POSITIONAL mapping:
  - Extract images from Hafifa.docx in document order
  - The Nth image in the doc = attachment_N (sorted)
"""
import zipfile, re, xml.etree.ElementTree as ET, shutil
from pathlib import Path

DOCX    = Path(r"c:\Users\gedim\Downloads\AppSec-Hafifa-main\AppSec-Hafifa\docx_files\Hafifa.docx")
BASE    = Path(r"c:\Users\gedim\Downloads\AppSec-Hafifa-main\AppSec-Hafifa")
ATT     = BASE / "Attachments"
BACKUP  = BASE / "Attachments_backup"
NS_A    = "http://schemas.openxmlformats.org/drawingml/2006/main"
NS_R    = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"

# Step 1: restore from backup
print("Restoring Attachments from backup...")
if BACKUP.exists():
    shutil.rmtree(ATT)
    shutil.copytree(BACKUP, ATT)
    print(f"  Restored {sum(1 for _ in ATT.iterdir())} files.")
else:
    print("  WARNING: No backup found, proceeding with current files.")

# Step 2: get images in document order from Hafifa.docx
with zipfile.ZipFile(DOCX) as z:
    rels_root = ET.fromstring(z.read("word/_rels/document.xml.rels"))
    rid_map = {}
    for r in rels_root:
        if "image" in r.get("Type", ""):
            rid_map[r.get("Id")] = r.get("Target", "").lstrip("/")

    doc_root = ET.fromstring(z.read("word/document.xml"))
    ordered_media = []
    seen = set()
    for elem in doc_root.iter(f"{{{NS_A}}}blip"):
        rid = elem.get(f"{{{NS_R}}}embed")
        if rid and rid in rid_map and rid_map[rid] not in seen:
            seen.add(rid_map[rid])
            ordered_media.append(rid_map[rid])

    print(f"\nDocx images in document order: {len(ordered_media)}")

    # Step 3: get sorted attachment numbers from all md files
    md_refs = sorted(set(
        int(m)
        for md in BASE.rglob("*.md")
        for m in re.findall(r"attachment_(\d+)", md.read_text(encoding="utf-8", errors="ignore"))
    ))
    print(f"MD attachment refs: {len(md_refs)} ({md_refs[0]}..{md_refs[-1]})")

    count = min(len(ordered_media), len(md_refs))
    print(f"\nMapping {count} images positionally...")

    replaced = 0
    for i in range(count):
        media_path = ordered_media[i]
        att_num = md_refs[i]
        dest = ATT / f"attachment_{att_num}.png"
        zip_path = media_path if media_path in z.namelist() else "word/" + media_path
        dest.write_bytes(z.read(zip_path))
        replaced += 1

    print(f"Done. Replaced {replaced} images.")
    if len(ordered_media) > len(md_refs):
        print(f"  ({len(ordered_media) - len(md_refs)} extra docx images not mapped)")
    elif len(md_refs) > len(ordered_media):
        unmapped = md_refs[len(ordered_media):]
        print(f"  WARNING: {len(unmapped)} attachment refs have no docx image: {unmapped}")

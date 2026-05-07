import re
from pathlib import Path

BASE = Path(r'c:\Users\gedim\Downloads\AppSec-Hafifa-main\AppSec-Hafifa')
ATT  = BASE / 'Attachments'

md_refs = sorted(set(int(m) for md in BASE.rglob('*.md') for m in re.findall(r'attachment_(\d+)', md.read_text(encoding='utf-8', errors='ignore'))))
gaps = [n for n in range(md_refs[0], md_refs[-1]+1) if n not in md_refs]
print('Gaps in md refs:', gaps)

existing = sorted(int(f.stem.replace('attachment_','')) for f in ATT.glob('*.png'))
unreferenced = [n for n in existing if n not in md_refs]
print('Unreferenced attachment files:', unreferenced)

"""
Build script to turn docx files into pdfs.
"""

import os
import sys
from pathlib import Path

from docx2pdf import convert

if sys.platform != 'darwin':
    raise NotImplementedError

if not os.path.exists('/Applications/Microsoft Word.app'):
    raise RuntimeError(
        'Microsoft Word is a dependency of this script, but is not installed '
        'on this device.'
    )

for f in Path(Path(__file__).parent, 'docx').iterdir():
    convert(f, Path(Path(__file__).parent, 'pdf', f'{f.stem}.pdf'))

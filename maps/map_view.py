import sys
from PIL import Image
import numpy as np

if len(sys.argv) < 2:
    print("Penggunaan: python3 map_view.py <path_file_pgm>")
    sys.exit(1)

pgm_path = sys.argv[1]

try:
    img = Image.open(pgm_path).convert('L')
    arr = np.array(img)
except Exception as e:
    print(f"Gagal membaca file PGM: {e}")
    sys.exit(1)

rows, cols = arr.shape

col_header = "".join(str(c % 10) for c in range(cols))
print(f"  {col_header}")

for r in range(rows):
    line = ""
    for c in range(cols):
        val = arr[r, c]
        if val < 50:        # Dinding (Hitam)
            line += '#'
        elif val > 240:     # Area Bebas / Lorong (Putih)
            line += '.'
        else:               # Unknown (Abu-abu / 205)
            line += ' '
    print(f"{r:2d} {line}")

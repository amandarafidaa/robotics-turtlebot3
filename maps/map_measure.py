import sys
import os
from PIL import Image
import numpy as np

if len(sys.argv) < 3:
    print("Penggunaan: python3 map_measure.py <path_file_pgm> <nomor_baris>")
    sys.exit(1)

pgm_path = sys.argv[1]
target_row = int(sys.argv[2])

resolution = 0.05
yaml_path = os.path.splitext(pgm_path)[0] + ".yaml"
if os.path.exists(yaml_path):
    with open(yaml_path, 'r') as f:
        for line in f:
            if 'resolution:' in line:
                resolution = float(line.split(':')[1].strip())
                break

try:
    img = Image.open(pgm_path).convert('L')
    arr = np.array(img)
except Exception as e:
    print(f"Gagal membaca file PGM: {e}")
    sys.exit(1)

rows, cols = arr.shape
total_cells = rows * cols

occupied = np.sum(arr < 50)
unknown = np.sum((arr >= 50) & (arr <= 240))
unknown_pct = (unknown / total_cells) * 100

print(f"ukuran peta (baris x kolom): ({rows}, {cols})")
print(f"occupied cells: {occupied}")
print(f"unknown cells: {unknown}")
print(f"unknown (%): {unknown_pct:.1f}")

if 0 <= target_row < rows:
    row_data = arr[target_row]
    occupied_cols = np.where(row_data < 50)[0]
    
    if len(occupied_cols) >= 2:
        dist_cells = occupied_cols[-1] - occupied_cols[0]
        dist_meters = dist_cells * resolution
        print(f"baris {target_row} -> jarak antar dinding (m): {dist_meters}")
    elif len(occupied_cols) == 1:
        print(f"baris {target_row} -> hanya ditemukan 1 dinding")
    else:
        print(f"baris {target_row} -> tidak ada dinding")
else:
    print(f"baris {target_row} di luar jangkauan peta")

#!/usr/bin/env python3
import os
import re
import struct
import zipfile
import sys

def print_help():
    print("""
Extracts RIFF/WAV audio chunks from a Rockstar .awc file.

Usage:
  python extract_awc.py <input.awc> <output_dir> <output.zip>

Example:
  python extract_awc.py narrator02.awc awc_wavs narrator02_wavs.zip

Arguments:
  <input.awc>    Path to the input .awc file
  <output_dir>   Directory to save extracted WAV files
  <output.zip>   Output ZIP archive containing all WAV files

Optional:
  --help         Show this help message
""")

def extract_awc_to_wavs(awc_path, output_dir, zip_path):
    try:
        with open(awc_path, 'rb') as f:
            data = f.read()
    except FileNotFoundError:
        print(f"Error: File '{awc_path}' not found.")
        sys.exit(1)

    # Find all 'RIFF' chunk start positions
    riff_offsets = [m.start() for m in re.finditer(b'RIFF', data)]
    if not riff_offsets:
        print("No RIFF chunks found in the file.")
        return

    os.makedirs(output_dir, exist_ok=True)
    extracted = []

    for idx, off in enumerate(riff_offsets):
        # Chunk size (4 bytes after 'RIFF', little endian)
        if off + 8 > len(data):
            continue
        size = struct.unpack_from('<I', data, off + 4)[0]
        end = off + 8 + size
        if end > len(data):
            continue  # incomplete chunk, skip

        wav_bytes = data[off:end]
        filename = f'narrator02_{idx:03d}.wav'
        out_path = os.path.join(output_dir, filename)
        with open(out_path, 'wb') as wf:
            wf.write(wav_bytes)
        extracted.append(out_path)
        print(f"Extracted: {filename} ({size} bytes)")

    # Create ZIP archive
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        for path in extracted:
            zf.write(path, arcname=os.path.basename(path))

    print(f"\nDone! {len(extracted)} WAV files packed into '{zip_path}'.")

if __name__ == '__main__':
    if '--help' in sys.argv or len(sys.argv) != 4:
        print_help()
        sys.exit(0 if '--help' in sys.argv else 1)

    awc_file      = sys.argv[1]
    output_folder = sys.argv[2]
    zip_file      = sys.argv[3]

    extract_awc_to_wavs(awc_file, output_folder, zip_file)

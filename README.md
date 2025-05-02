# AWC2WAV

**AWC2WAV** is a Python-based extraction tool designed to easily convert Rockstar Games' Audio Wave Container (.awc) files into individual RIFF/WAV audio chunks, conveniently packed into a ZIP archive.

## Features

* Automatically detects and extracts embedded RIFF/WAV audio chunks.
* Supports batch extraction from single `.awc` files.
* Outputs organized WAV files and packs them into a convenient ZIP archive.
* Simple, intuitive command-line interface with helpful error messages.

## Requirements

* Python 3.x

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/AWC2WAV.git
cd AWC2WAV
```

Ensure you have Python installed:

```bash
python3 --version
```

No additional Python packages are required.

## Usage

Extract WAV audio from `.awc` files:

```bash
python extract_awc.py <input.awc> <output_directory> <output.zip>
```

**Example:**

```bash
python extract_awc.py narrator02.awc extracted_wavs narrator02_audio.zip
```

View help information:

```bash
python extract_awc.py --help
```

## Example Output

```
Extracted: narrator02_000.wav (187654 bytes)
Extracted: narrator02_001.wav (276543 bytes)
...

Done! 158 WAV files packed into 'narrator02_audio.zip'.
```

## Supported Formats

* Rockstar Games Audio Wave Container (.awc)
* RIFF/WAV embedded audio chunks

## License

GPLv3 © Brian Daker

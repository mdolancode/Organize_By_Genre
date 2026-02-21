# Organize By Genre

A Python command-line tool that scans a music library and automatically organizes audio files into genre-based folders by reading embedded metadata tags. Built to solve a real problem — managing a large DJ music collection.

---

## Why This Exists

As a DJ, I have a large library of audio files across multiple formats. Manually sorting tracks by genre is tedious and error-prone. This script reads the genre metadata already embedded in each file and does the organizing automatically.

---

## How It Works

1. Provide a source directory containing your music files
2. Provide a destination directory for the organized output
3. The script recursively walks the source directory
4. For each file, it reads the embedded genre tag
5. Creates a subfolder for each genre if it doesn't already exist
6. Moves the file into the appropriate genre folder
7. Files with no genre tag are moved to an `Unknown` folder rather than being skipped

---

## Supported Formats

- **MP3** — reads the `TCON` ID3 tag using `mutagen`
- **AIFF** — reads genre metadata using `TinyTag`

Both formats are handled independently since they store genre data differently under the hood.

---

## Technical Highlights

- **mutagen** for MP3 ID3 tag parsing (`TCON` frame)
- **TinyTag** for AIFF metadata extraction
- **`os.walk()`** for recursive directory traversal
- Automatic genre directory creation with `os.makedirs()`
- Graceful fallback — unknown or untagged files go to an `Unknown` folder instead of being skipped or causing errors
- Format-agnostic design — easily extendable to support additional audio formats

---

## Usage

```bash
pip install mutagen tinytag
python organize_by_genre.py
```

You will be prompted to enter:
- The directory where your music files are located
- The directory where you want the organized output

---

## Known Gaps

- No dry-run / preview mode (moves files immediately)
- No duplicate filename handling
- Only supports MP3 and AIFF currently — WAV, FLAC, and other formats return `Unknown`
- No logging of moved files

These would be natural next steps for a more robust version.

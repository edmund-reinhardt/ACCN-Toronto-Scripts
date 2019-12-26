# metadata-to-filename
Extracts date from filename and metadata from .mp3 files and uses this data to rename the files

## Usage
* Open `run.py` with Python (tested with Python `3.7`).
* You should see a folder selection window.
* Select the folder that directly contains the .mp3 files you would like renamed
* All the .mp3 files in the folder that you selected will be renamed.

### File naming scheme
Example old filename:
```
-130113_000.mp3
```
Example new filename:
```
2013-01-13 AM - Romans 10 - Doug Savin.mp3
```
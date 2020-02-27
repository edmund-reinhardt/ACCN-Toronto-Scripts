# acc-website-scripts

## Update RSS XML with sermons detected from mp3 files
Will take an individual or directory-full of mp3 files and update the RSS xml file to list them all


## Upload sermons to website
compares the mp3 files on the web site with the local directory, and uploads them
* in the future, the rss xml file will be updated as well

### Usage
* Run `sync.bat` windows batch file
* This opens `sync_sermons.py` with the local Python (tested with Python `3.8`) 
* All the .mp3 files in the local folder specified in sync_sermons.py that do not already exists in the remote
folder specified in sync_sermons.py will be uploaded



## Rename sermons to archive them on Google Drive
Extracts date from filename and metadata from .mp3 files and uses this data to rename the files

### Usage
* Run the `rename.bat` windows batch file.
* This opens `rename_old.py` with Python (tested with Python `3.7` and `3.8`) 
* You should see a folder selection window.
* Select the folder that directly contains the .mp3 files you would like renamed
* All the .mp3 files in the folder that you selected will be renamed.
* The renamed files can be moved to Google Drive as an archive and free up web space

#### File naming scheme
Example old filename:
```
-130113_000.mp3
```
Example new filename:
```
2013-01-13 AM - Romans 10 - Doug Savin.mp3
```

#### Google Drive archives
* all years from 2011 to 2015 is stored on the Google Drive of accntoronto.sermons12@gmail.com
* all years from 2016 to 2018 is stored on the Google Drive of accntoronto.sermons16@gmail.com
* all years from 2019 to ... is stored on the Google Drive of accntoronto.sermons19@gmail.com
* once files are renamed via rename.bat, copy them to the appropriate Google Drive and 
ask the web master to point to them from the sermons archive page on the web site


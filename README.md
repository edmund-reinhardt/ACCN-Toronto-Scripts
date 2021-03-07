# acc-website-scripts
[![Build Status](https://travis-ci.com/edmund-reinhardt/ACCN-Toronto-Scripts.svg?branch=master)](https://travis-ci.com/edmund-reinhardt/ACCN-Toronto-Scripts)

## Purpose
This project contains a set of python scripts to update the sermons on a church website.  The functions performed are detecting which sermons are not yet on the website and uploading them and at the same time maintaining the RSS file that drives podcasts for both Android and Apple mobile devices.  This RSS file can also be generated from scratch from a directory.  Also to migrate older sermons off of the expensive website storage to less expensive cloud storage, there is a rename function that will rename all of the files meaningfully according to the information stored in the ID3 tags of the MP3 files.  All of the functions take advantage of this ID3 information to do the right thing.

## Installation

* Install python >= 3.8
* Open a terminal and navigate 
to the project directory
* Create a virtual environment 
named `my_venv` in the project directory:
```shell script
python -m venv my_venv
```
* Activate the virtual environment to 
use the specific version of Python and 
pip from the virtual environment with a 
command similar to `my_venv\Scripts\activate.bat`.
* Install the required dependencies to 
the virtual environment:
```shell script
pip install -r requirements.txt
```
* create a file ```accweb\credentials.py``` that will hold three variables SERVER, USERNAME and PASSWORD 
which are the required credentials to access the website's file system via FTP 

## Generate RSS XML with sermons detected from mp3 files
Will take an individual or directory-full of mp3 files and update the RSS xml file to list them all. 
This is the way to initially generate the accntoronto_rss.xml file that drives the podcasts on 
both Google Play Music and Apple Podcasts. 

### Usage
* Run the `gen_rss.bat` windows batch file.
* This opens `podcast_xml.py` with Python (tested with Python `3.8`) 
* You should see a folder selection dialog. Choose the folder that contains the .mp3 files you are interested in.
* All the .mp3 files in the folder that you selected will be referenced in the accntoronto_rss.xml which is .
an RSS 2.0 file which is accepted by Google Play Music and Apple Podcasts to drive podcasts there.
* This will have to be uploaded to the target web site.  

## Upload sermons to website
compares the mp3 files on the web site with the local directory, and uploads them.  The rss xml file that drives podcasts will be updated as well with an additional <item> tag for each new mp3 file and uploaded to the web site.

### Usage
* Run `sync.bat` windows batch file
* This opens `sync_sermons.py` with the local Python (tested with Python `3.8`) 
* All the .mp3 files in the local folder specified in sync_sermons.py that do not already exists in the remote
folder specified in sync_sermons.py will be uploaded
* At the beginning of a new year, sync_sermons.py will have to have the year updated at the bottom of the file


## Rename sermons to archive them on Google Drive
Extracts date from filename and metadata from .mp3 files and uses this data to rename the files

### Usage
* Run the `rename.bat` windows batch file.
* This opens `rename_old.py` with Python (tested with Python `3.7` and `3.8`) 
* You should see a folder selection dialog. Choose the folder that contains the .mp3 files you would like renamed
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


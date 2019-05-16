"""
This extracts the metadata and filename and then makes and prints a new filename
This is the unstructured version of our work thus far
"""
import eyed3
from os.path import join
from os.path import basename

path = join("acc_web", "2018", "-180107_000.mp3")
print(path)

# Extracting filename from path
filename = basename(path)

# Loading file identified by path into an audio file object called metadata
metadata = eyed3.load(path)

print(filename)

print(metadata.tag.artist)

print(metadata.tag.album)

# Creates formatted date containing parts of filename
# f is used to integrate expressions into the string directly
date = f"20{filename[1:3]}-{filename[3:5]}-{filename[5:7]}"

if filename[8:11] == "000":
    date += " AM"
elif filename[8:11] == "001":
    date += " PM"

print(date)

scripture = metadata.tag.album
speaker = metadata.tag.artist

filename = (date + " - " + scripture + " - " + speaker)

print(filename)

"""
Which pieces of data do we want?
Date
Speaker (Contributing artists or artist)
Scripture (Album)
AM/PM

File name format:   YYMMDD_Time_Scripture_Speaker
"""
# file.rename(join("acc_web","2018","-180107_000.mp3"))
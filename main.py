"""
The conclusion is that it is possible using eyeD3 to extract the metadata from an mp3 file.
"""
import eyed3
from os.path import join

# Loading file identified by path into an audio file object called metadata
metadata = eyed3.load(join("acc_web", "2018", "-180107_000.mp3"))

# Example of extracted metadata
print(metadata.tag.artist)
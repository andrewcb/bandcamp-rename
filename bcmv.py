#!/usr/bin/python

import sys
import os
import re
import collections
import argparse

re_track_separator = re.compile(" - [0-9]")

def commonPrefix(files):
    (v, c) = collections.Counter([re_track_separator.split(p)[0] for p in files]).most_common(1)[0]
    return c>1 and v or None

def commonAlbumName(files):
    # find a common album name for compliations; i.e.,
    #  "Some Artist - Compilation Title - 01 Some Song"
    #  "Some Other Artist - Compilation Title - 02 Another Song"
    # assumption: there will not be more than one ' - ' separator in the artist/album segment
    (v, c) = collections.Counter([re_track_separator.split(p)[0].split(" - ")[-1] for p in files]).most_common(1)[0]
    return c>1 and v or None


def calculateRenamings(files):
    "Calculate a list of (old name, new name) tuples"
    prefix = commonPrefix(files)
    if prefix != None:
        for file in (f for f in files if f[:len(prefix)] == prefix):
            newname = file[len(prefix)+3:]
            yield (file, newname)
    else:
        albumName = commonAlbumName(files)
        if albumName != None:
            for file in files:
                albumIndex = file.find(albumName)
                if albumIndex >= 3:
                    artistName = file[:albumIndex-3]
                    numberAndTitle = file[albumIndex+len(albumName)+3:]
                    (number, title) = numberAndTitle.split(" ", 1)
                    yield (file, "%s %s - %s"%(number, artistName, title))


def processDir(dir, dry_run):
    "Process the files in a directory"
    files = os.listdir(dir)

    for (file, newname) in calculateRenamings(files):
        if dry_run:
            print "renaming: \"%s\" -> \"%s\""%(file, newname)
        if not dry_run:
            os.rename(os.path.join(dir,file), os.path.join(dir,newname))
                

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Abbreviate the names of Bandcamp-downloaded audio files"
    )
    parser.add_argument("dirs", metavar="dir", nargs="+", help="Directories containing unzipped albums")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    for dir in args.dirs:
        processDir(dir, dry_run=args.dry_run)

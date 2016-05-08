# bandcamp-rename
A script for abbreviating the names of audio files downloaded from Bandcamp

## The problem

When the [Bandcamp](http://bandcamp.com) music download service makes audio files of purchased music for download, it names them in an exceedingly long-winded filename; each audio file in the directory containing the album has in its filename not only the track number and song title, but also the artist name and album title. If you already put the tracks in directories holding that information, the result is a lot of long, cumbersome filenames, much of whose length is redundant information.  Which is where this script comes in.

## The solution

This project contains one script, `bcmv` (pronounced “Bandcamp Rename”), which, given a directory containing an album downloaded from Bandcamp, will rename all the music files to more sensible names, by stripping the artist and album names from the start, leaving only the track numbers and titles. Files not starting with the artist and album names will be left unmodified. 

For example, if the directory `/music/FourTet/Morning-Evening` contains the following files (exactly as they are in the ZIP file Bandcamp prepares for [this release](https://fourtet.bandcamp.com/album/morning-evening)):
```
cover.jpg
Four Tet - Morning-Evening - 01 Morning Side.mp3
Four Tet - Morning-Evening - 02 Evening Side.mp3

```

Running `bcmv /music/FourTet/Morning-Evening` will rename them, resulting in:
```
cover.jpg
01 Morning Side.mp3
02 Evening Side.mp3
```

`bcmv` can now also handle compilation albums, where the artist differs between files, and can rename them so that the track number is first; i.e., if a directory contains:
```
Makthaverskan - DIYPOP FEST2016 - 01 Asleep.mp3
Otoboke Beaver - DIYPOP FEST2016 - 03 Akimahenka.mp3
Trust Fund - DIYPOP FEST2016 - 02 Mother's day.mp3
```

Running `bcmv` on it will rename these to

```
01 Makthaverskan - Asleep.mp3
02 Trust Fund - Mother's day.mp3
03 Otoboke Beaver - Akimahenka.mp3
```

which has the further effect of placing the files in track number order, as whoever created the compilation intended.

## Installing

The **bcmv** script's filename in the repository is `bcmv.py`; this is to allow unit testing. 
Copy `bcmv.py` into your path (optionally renaming it to lose the `.py` extension), and `chmod +x` 

All of bcmv's code is contained in the file `bcmv.py`.

## Dependencies

**bcmv** is written in Python (version 2.7) and uses only standard libraries.

## Tests

There are unit tests in the accompanying `bcmvtests.py` file.

## Author

**bcmv** was written by [Andrew Bulhak](http://dev.null.org/acb/), shortly after buying the entire Of Montreal and Alison's Halo back-catalogues on Bandcamp and being faced with the prospect of manually cleaning up the filenames.

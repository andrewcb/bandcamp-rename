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

## Dependencies

**bcmvv** is written in Python (version 2.7) and uses only standard libraries. All its code is contained within the one script. To install, just copy the `bcmv` file to somewhere in your path and `chmod +x` it.

## Author

**bcmv** was written by [Andrew Bulhak](http://dev.null.org/acb/), shortly after buying the entire Of Montreal and Alison's Halo back-catalogues on Bandcamp and being faced with the prospect of manually cleaning up the filenames.

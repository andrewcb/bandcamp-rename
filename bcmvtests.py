import unittest
import bcmv

class TestBandcampRename(unittest.TestCase):
    def test_commonPrefix(self):
        self.assertEqual(bcmv.commonPrefix(["Foo - Bar - 01 Baz", "Foo - Bar - 02 Xyzzy", "Foo - Bar - 03 Quux"]), "Foo - Bar")

    def test_commonPrefix_falsePositives(self):
        self.assertEqual(bcmv.commonPrefix([
            "Makthaverskan - DIYPOP FEST2016 - 01 Asleep.mp3", 
            "Trust Fund - DIYPOP FEST2016 - 02 Mother's day.mp3",
            "Haiku Salut - DIYPOP FEST2016 - 11 Foreign Pollen.mp3", 
            "Chorusgirl - DIYPOP FEST2016 - 19 Whiteout.mp3"
            ]), None)

    def test_commonAlbumName(self):
        self.assertEqual(bcmv.commonAlbumName([
            "Makthaverskan - DIYPOP FEST2016 - 01 Asleep.mp3", 
            "Trust Fund - DIYPOP FEST2016 - 02 Mother's day.mp3",
            "Haiku Salut - DIYPOP FEST2016 - 11 Foreign Pollen.mp3", 
            "Chorusgirl - DIYPOP FEST2016 - 19 Whiteout.mp3"
            ]), "DIYPOP FEST2016")


    def test_renamings_oneArtistAlbum(self):
        input = [
            "Laurie Spiegel - The Expanding Universe - 01 Patchwork.mp3",
            "Laurie Spiegel - The Expanding Universe - 02 Old Wave.mp3",
            "Laurie Spiegel - The Expanding Universe - 03 Pentachrome.mp3",
            "Laurie Spiegel - The Expanding Universe - 04 A Folk Study.mp3",
            "Laurie Spiegel - The Expanding Universe - 05 Drums.mp3",
            "Laurie Spiegel - The Expanding Universe - 06 Appalachian Grove I.mp3",
            "Laurie Spiegel - The Expanding Universe - 09 The Expanding Universe.mp3",
            "Laurie Spiegel - The Expanding Universe - 10 East River Dawn.mp3",
            "Laurie Spiegel - The Expanding Universe - 11 The Unquestioned Answer.mp3",
            "Laurie Spiegel - The Expanding Universe - 12 The Orient Express.mp3",
            "Laurie Spiegel - The Expanding Universe - 13 Clockworks.mp3",
            "Laurie Spiegel - The Expanding Universe - 14 Dirge I.mp3",
            "Laurie Spiegel - The Expanding Universe - 17 Music for Dance II.mp3",
            "Laurie Spiegel - The Expanding Universe - 18 Kepler's Harmony of the Worlds.mp3",
            "Laurie Spiegel - The Expanding Universe - 19 Wandering in Our Times.mp3",
            "Laurie Spiegel - The Expanding Universe - UW09booklet.pdf",
            "cover.jpg"
        ]

        self.assertEqual([x for x in bcmv.calculateRenamings(input)], [
            ('Laurie Spiegel - The Expanding Universe - 01 Patchwork.mp3', '01 Patchwork.mp3'), 
            ('Laurie Spiegel - The Expanding Universe - 02 Old Wave.mp3', '02 Old Wave.mp3'), 
            ('Laurie Spiegel - The Expanding Universe - 03 Pentachrome.mp3', '03 Pentachrome.mp3'), 
            ('Laurie Spiegel - The Expanding Universe - 04 A Folk Study.mp3', '04 A Folk Study.mp3'), 
            ('Laurie Spiegel - The Expanding Universe - 05 Drums.mp3', '05 Drums.mp3'), 
            ('Laurie Spiegel - The Expanding Universe - 06 Appalachian Grove I.mp3', '06 Appalachian Grove I.mp3'), 
            ('Laurie Spiegel - The Expanding Universe - 09 The Expanding Universe.mp3', '09 The Expanding Universe.mp3'), 
            ('Laurie Spiegel - The Expanding Universe - 10 East River Dawn.mp3', '10 East River Dawn.mp3'), 
            ('Laurie Spiegel - The Expanding Universe - 11 The Unquestioned Answer.mp3', '11 The Unquestioned Answer.mp3'), 
            ('Laurie Spiegel - The Expanding Universe - 12 The Orient Express.mp3', '12 The Orient Express.mp3'), 
            ('Laurie Spiegel - The Expanding Universe - 13 Clockworks.mp3', '13 Clockworks.mp3'), 
            ('Laurie Spiegel - The Expanding Universe - 14 Dirge I.mp3', '14 Dirge I.mp3'), 
            ('Laurie Spiegel - The Expanding Universe - 17 Music for Dance II.mp3', '17 Music for Dance II.mp3'), 
            ("Laurie Spiegel - The Expanding Universe - 18 Kepler's Harmony of the Worlds.mp3", "18 Kepler's Harmony of the Worlds.mp3"), 
            ('Laurie Spiegel - The Expanding Universe - 19 Wandering in Our Times.mp3', '19 Wandering in Our Times.mp3'), 
            ('Laurie Spiegel - The Expanding Universe - UW09booklet.pdf', 'UW09booklet.pdf')])

    def test_renamings_multiArtistAlbum(self):
        input = [
            "Makthaverskan - DIYPOP FEST2016 - 01 Asleep.mp3", 
            "Trust Fund - DIYPOP FEST2016 - 02 Mother's day.mp3",
            "Haiku Salut - DIYPOP FEST2016 - 11 Foreign Pollen.mp3", 
            "Chorusgirl - DIYPOP FEST2016 - 19 Whiteout.mp3"
        ]
        self.assertEqual([x for x in bcmv.calculateRenamings(input)], [
            ( "Makthaverskan - DIYPOP FEST2016 - 01 Asleep.mp3", "01 Makthaverskan - Asleep.mp3"),
            ( "Trust Fund - DIYPOP FEST2016 - 02 Mother's day.mp3", "02 Trust Fund - Mother's day.mp3"),
            ( "Haiku Salut - DIYPOP FEST2016 - 11 Foreign Pollen.mp3", "11 Haiku Salut - Foreign Pollen.mp3" ),
            ( "Chorusgirl - DIYPOP FEST2016 - 19 Whiteout.mp3", "19 Chorusgirl - Whiteout.mp3" )
        ])

if __name__ == '__main__':
    unittest.main()
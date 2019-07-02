import lyricsgenius
genius = lyricsgenius.Genius("UBF9aPm6i-ZLY3PLi0QGns2_QF7SD8Gje3EWww0Uk9VWgRmyjjVR4QFAoisVYGsw")
artist = genius.search_artist("Oxxxymiron", max_songs=200, sort="title")
artist.save_lyrics()
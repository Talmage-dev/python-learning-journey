""" Day 10: Object-Oriented Programming (OOP) - Part 1 """

# Practice Exercise 3: Create a Playlist Class

class Playlist:
    def __init__(self):
        self.songs = []
    
    def add_song(self, title, artist):
        self.songs.append({"Title": title, "Artist": artist})

    def remove_song(self, title):
        self.songs = [song for song in self.songs if song["Title"] != title]
        # Instead of looping through and removing the songs that match the title
        # Create a new list of all the songs that don't match the title
    
    def get_song_count(self):
        return len(self.songs)
    
    def display_playlist(self):
        for song in self.songs:
            print(f"{song["Title"]} by {song["Artist"]}")

# Test
playlist = Playlist()
playlist.add_song("Somebody To Love Me", "Dua Lipa and Troye Sivan")
playlist.add_song("Oh No (Pt.2)", "L.A.B")
playlist.add_song("Pysical", "Dua Lipa")
playlist.display_playlist()
print(f"Total songs: {playlist.get_song_count()}")

playlist.remove_song("Pysical")
playlist.display_playlist()
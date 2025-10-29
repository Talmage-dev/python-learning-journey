class Song:
    """Node for Playlist"""
    def __init__(self, title, artist):
        self.title = title                  # Song title - (data)
        self.artist = artist                # Artist name - (data)
        self.next = None                    # Next song - (pointer)
        
class Playlist:
    """Linked list of songs"""
    def __init__(self, name):
        self.name = name                    # Playlist name
        self.head = None                    # First song(node) 
        self.current = None                 # Currently playing
    
    def add_song(self, title, artist):
        """Add song to end of playlist"""
        new_song = Song(title, artist)      # Create song(node)

        if self.head is None:               # If there is nothing in the 1st position
            self.head = new_song            # Make it the first song(node)
            self.current = new_song         # Start playing it
            return
        
        current = self.head                 # if playlist isn't empty, start at the begining
        while current.next:                 # while there is a pointer
            current = current.next          # keep looking until there is no pointer (None)
        current.next = new_song             # Add to end

    def play_next(self):
        """Move to next song"""
        if self.current and self.current.next:      # If there's a next song
            self.current = self.current.next        # Move to it
            return f"Now playing {self.current.title} by {self.current.artist}"      # Play song 
        return "End of playlist" 

    def current_song(self):
        """Show current song"""
        if self.current:                    
            return f"{self.current.title} by {self.current.artist}"     # Play song      
        return "No song playing"
    
    def show_playlist(self):
        """Display all songs"""
        print(f"\n=== {self.name} ===")
        current = self.head                 # Start at the begining
        position = 1                        # Track position
        while current:                      # While there's a song
            marker = "▶︎ " if current == self.current else " "           # Mark current
            print(f"{marker}{position}. {current.title} - {current.artist}")
            current = current.next          # Next song(node)
            position += 1

# Test
playlist = Playlist("Classics")
playlist.add_song("Bohemian Rhapsody", "Queen")
playlist.add_song("Stairway to Heaven", "Led Zeppelin")
playlist.add_song("Hotel California", "Eagles")

playlist.show_playlist()
print(playlist.current_song())
print(playlist.play_next())
playlist.show_playlist()
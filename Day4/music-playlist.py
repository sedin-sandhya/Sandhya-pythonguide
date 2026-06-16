# Build a music player playlist using a Doubly Linked List. 
# Each node holds song name, artist, and duration. Support: 
# Add a song to the end of the playlist 
# Remove the currently playing song 
# Play next track / previous track 
# Display the full queue with [playing] marker 

class Node:

    def __init__(self, name, artist, duration):
        self.name = name
        self.artist = artist
        self.duration = duration

        self.prev = None
        self.next = None
    
class Playlist:

    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None
        self.count = 0

    def add_song(self, name, artist, duration):
        new_song = Node(
            name,
            artist, 
            duration
        )

        if self.head is None:

            self.head = new_song
            self.tail = new_song
            self.current = new_song
        else:

            new_song.prev = self.tail
            self.tail.next = new_song
            self.tail = new_song
        
        self.count += 1

    def format_duration(self, seconds):

        minutes = seconds // 60
        seconds = seconds % 60

        return f"{minutes}:{seconds:02d}"
    
    def next_track(self):

        if self.current is None:
            print("Playlist Empty")
            return
        
        if self.current.next is None:
            print("End of playlist")
            return

        self.current = self.current.next

        print(f"Now playing:{self.current.name} - {self.current.artist}")

    def prev_track(self):

        if self.current is None:
            print("Playlist empty")
            return

        if self.current.prev is None:
            print("Already at Beggining")
            return
        
        self.current = self.current.prev

        print(f"Now playing:{self.current.name} - {self.current.artist}")

    def remove_current(self):

        if self.current is None:
            print("No song playing")
            return
        
        removed = self.current

        if removed.prev is None and removed.next is None:
            self.head = None
            self.tail = None
            self.current = None

        elif removed.prev is None:
            self.head = removed.next
            self.head.prev = None
            self.current = self.head

        elif removed.next is None:
            self.tail = removed.prev
            self.tail.next = None
            self.current = self.head
        
        else:
            removed.prev.next = removed.next
            removed.next.prev = removed.prev
            self.current = removed.next

        self.count -= 1

        print(
            f"Removed: {removed.name}"
        )
    
    def show_queue(self):

        if self.head is None:
            print("Playlist empty")
            return


        print("\nQueue:\n")

        temp = self.head
        index = 1


        while temp:

            playing = ""

            if temp == self.current:
                playing = " [playing]"


            print(
                f"{index}. {temp.name} — "
                f"{temp.artist} "
                f"({self.format_duration(temp.duration)})"
                f"{playing}"
            )

            temp = temp.next
            index += 1

def main():
    p = Playlist()
    p.add_song("Kesariya", "Arijit", 262)
    p.add_song("Raataan", "Jubin", 218)
    p.add_song("Tum Hi Ho", "Arijit", 261)
    p.add_song("Believer", "Imagine Dragons", 204)
    p.next_track()
    p.next_track()
    p.remove_current()
    p.show_queue()


if __name__ == "__main__":
    main()
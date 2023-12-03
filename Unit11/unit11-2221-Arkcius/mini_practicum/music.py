class Time:
    __slots__ = ['hours', 'minutes', 'seconds']

    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

def get_time(time):
    return '{}:{:02}:{:02}'.format(time.hours, time.minutes, time.seconds)

#song class
class Song:
    __slots__ = ["title","artist","running_duration"]
    
    #init for song class
    def __init__(self,title,artist,run):
        self.title = title
        self.artist = artist
        self.running_duration = run

class Album:
    #album slots for title artists #tracks tracks and total time
    __slots__ = ["title","artists","total_tracks","total_run","tracks"]

#everything besides title set to empty or zero
    def __init__(self,title:str):
        self.title = title
        self.artists = []
        self.tracks = []
        self.total_run = Time(0,0,0)
        self.total_tracks = 0

#adds a song to the album        
def add_song(song,album):
    #increases total tracks and adds song to tracks00
    album.total_tracks += 1
    album.tracks.append(song)
    #if no artists adds the artist to artist list
    if len(album.artists) == 0:
        album.artists.append(song.artist)
    #else checks if artist already in list and if so doesnt add them

    else:
        for elements in album.artists:
            if elements == song.artist:
                break
            else:
                album.artists.append(song.artist)
    #gets the seconds minutes and hours of total + new song
    sec = album.total_run.seconds + song.running_duration.seconds
    minn = album.total_run.minutes + song.running_duration.minutes
    hour = album.total_run.hours + song.running_duration.hours
    #checks if seconds and minutes over 60 and if so
    #makes it so they get minused 60 and the one goes to next up
    if sec >= 60:
        sec -= 60
        minn += 1
    if minn >= 60:
        minn -=60
        hour += 1
    #makes new album total runtime
    album.total_run = Time(hour,minn,sec)

#prints a song in format of title artist runtime    
def print_song(song):
    print(song.title,":",song.artist,":",get_time(song.running_duration))

#prints an entire album
def print_album(album):
    #prints title total runtime and number of tracks
    print("Title: ",album.title)
    print("Total Run Time: ",get_time(album.total_run))
    print("Number of Tracks: ",album.total_tracks)
    print("Artists")
    #prints all artists on track
    for elements in album.artists:
        print("\t",elements)
    print()
    #prints all the songs in the album in song artist runtime format
    print("Tracks")
    print("Song:Artist:RunTime")
    for elements in album.tracks:
        print_song(elements)

#main
def main():
    song1 = Song("musica","me",Time(0,3,21))
    song2 = Song("musical","also me",Time(0,2,21))
    song3 = Song("musicalas","me",Time(0,3,11))
    album = Album("hello")
    add_song(song1,album)
    add_song(song2,album)
    add_song(song3,album)
    print_album(album)
    

main()


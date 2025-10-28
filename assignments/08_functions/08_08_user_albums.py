def make_album(artist, title, songs = None):
    """Return album dictionary."""
    album = {'artist': artist, 'title': title, 'songs': songs}
    return album

while True:
    print("\nEnter album information.")
    print("(enter 'q' at any time to quit")

    artist = input("Artist name: ")
    if artist == 'q':
        break
    title = input("Title name:")
    if title == 'q':
        break
    song = input("Song number (optional): ")
    if song == 'q':
        break
    album = make_album(artist, title, song)
    print(album)
def make_album(artist, title, songs = None):
    """Return album dictionary."""
    album = {'artist': artist, 'title': title, 'songs': songs}
    return album

print(make_album("Michael Jackson", "Thriller"))
print(make_album("The Beatles", "Let it Be", 12))
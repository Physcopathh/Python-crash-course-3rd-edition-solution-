def make_album(artist_name, album_title, recitations=None):
    album = {'Artist-Name' : artist_name, 'Album-title' : album_title}
    if recitations != None:
        album['Recitations'] = recitations
    return album

while True:
    album_artist = input('Hey boss tell me your album-artist\n (if you want to quit enter \'q\')')
    if album_artist == 'q':
        break

    album_name = input('Hey boss tell me your album-name')
    print(make_album(album_artist,album_name))
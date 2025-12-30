def make_album(artist_name, album_title, recitations=None):
    album = {'Artist-Name' : artist_name, 'Album-title' : album_title}
    if recitations != None:
        album['Recitations'] = recitations
    return album

album1 = make_album('Asmar', 'At local')
album2 = make_album('Yassir Al Dosri', 'Al-Haram')
album3 = make_album('Mohammad Al Lahudin', 'At heart', ['Surah Baqarah','Surah Nisa','Surah Alaq'])

print(album1)
print(album2)
print(album3)
from yandex_music import Client


TOKEN: str = ''


def main():
    client = Client(TOKEN).init()

    tracks = []
    liked_tracks = client.users_likes_tracks()
    for e in liked_tracks:
        tracks.append(f'{e["id"]}:{e["album_id"]}')
    compositions = client.tracks(tracks)

    for c in compositions:
        print(f'{c.artists_name()[0]} - {c.title}')


if __name__ == '__main__':
    main()
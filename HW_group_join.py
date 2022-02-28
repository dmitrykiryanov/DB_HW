import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://dmitry_kiryanov_py48:12345@localhost:5432/homework_db_py48')
connection = engine.connect()

# количество исполнителей в каждом жанре

res = connection.execute("""SELECT name, COUNT(artist_id) FROM genre
              JOIN artist_genre ON genre.id = artist_genre.genre_id
              GROUP BY name;
""").fetchall()
print(f'количество исполнителей в каждом жанре: {res}')

# количество треков, вошедших в альбомы 2019-2020 годов

res = connection.execute("""SELECT COUNT(track.id) FROM track
              JOIN album ON track.album_id = album.id
              WHERE year BETWEEN 2019 AND 2020;
""").fetchall()
print(f'количество треков, вошедших в альбомы 2019-2020 годов: {res}')

# средняя продолжительность треков по каждому альбому

res = connection.execute("""SELECT a.name, AVG(duration) FROM album a
              JOIN track ON a.id = track.album_id
              GROUP BY a.name
""").fetchall()
print(f'средняя продолжительность треков по каждому альбому: {res}')

# все исполнители, которые не выпустили альбомы в 2020 году

res = connection.execute("""SELECT a.name FROM artist a
              JOIN artist_album aa ON a.id = aa.artist_id
              JOIN album ON aa.album_id = album.id
              WHERE a.name NOT IN (SELECT a.name FROM artist
                                    WHERE year = 2020);
""").fetchall()
print(f'все исполнители, которые не выпустили альбомы в 2020 году: {res}')

# названия сборников, в которых присутствует конкретный исполнитель

res = connection.execute("""SELECT c.name FROM collection c
              JOIN track_collection tc ON c.id = tc.collection_id
              JOIN track t ON tc.track_id = t.id
              JOIN album a ON t.album_id = a.id
              JOIN artist_album aa ON a.id = aa.album_id
              JOIN artist ON aa.artist_id = artist.id
              WHERE artist.name = 'Inna';
""").fetchall()
print(f'названия сборников, в которых присутствует конкретный исполнитель Inna: {res}')

# название альбомов, в которых присутствуют исполнители более 1 жанра

res = connection.execute("""SELECT a.name FROM album a
              JOIN artist_album aa ON a.id = aa.album_id
              JOIN artist ON aa.artist_id = artist.id
              JOIN artist_genre ag ON artist.id = ag.artist_id
              GROUP BY a.name
              HAVING COUNT(genre_id) > 1;
""").fetchall()
print(f'название альбомов, в которых присутствуют исполнители более 1 жанра: {res}')

# наименование треков, которые не входят в сборники

res = connection.execute("""SELECT name FROM track
                LEFT JOIN track_collection tc ON track.id = tc.track_id
                WHERE tc.track_id IS NULL;
""").fetchall()
print(f'наименование треков, которые не входят в сборники: {res}')

# исполнителя(-ей), написавшего самый короткий по продолжительности трек

res = connection.execute("""SELECT artist.name FROM artist
                JOIN artist_album aa ON artist.id = aa.artist_id
                JOIN album a ON aa.album_id = a.id
                JOIN track t ON a.id = t.album_id
                WHERE duration = (SELECT MIN(duration) FROM track);
""").fetchall()
print(f'исполнитель, написавший самый короткий по продолжительности трек: {res}')

# название альбомов, содержащих наименьшее количество треков

res = connection.execute("""SELECT name FROM (
            SELECT album.name, COUNT(t.id) cnt FROM album
                        JOIN track t ON album.id = t.album_id
                        GROUP BY album.name) final_sort
                WHERE cnt = (SELECT MIN(cnt) FROM
                        (SELECT album.name, COUNT(t.id) cnt FROM album
                        JOIN track t ON album.id = t.album_id
                        GROUP BY album.name) cnt_track
                        );
                 
""").fetchall()
print(f'название альбомов, содержащих наименьшее количество треков: {res}')

import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://dmitry_kiryanov_py48:12345@localhost:5432/homework_db_py48')
connection = engine.connect()

# # Исполнители
#
# connection.execute("""INSERT INTO artist
#             VALUES(1, 'Nirvana'),
#                   (2, 'Imagine Dragons'),
#                   (3, 'Inna'),
#                   (4, 'Adele'),
#                   (5, 'Shouse'),
#                   (6, 'Trevor Daniel'),
#                   (7, 'Rompasso'),
#                   (8, 'Calvin Harris');
# """)
#
# # Жанры
#
# connection.execute("""INSERT INTO genre
#             VALUES(1, 'Rock'),
#                   (2, 'Pop'),
#                   (3, 'House'),
#                   (4, 'Hip-Hop'),
#                   (5, 'Drum&Bass'),
#                   (6, 'Dj remix');
# """)
#
# # Альбомы
#
# connection.execute("""INSERT INTO album
#             VALUES(1, 'Nevermind', 1991),
#                   (2, 'Night Visions', 2012),
#                   (3, '25', 2015),
#                   (4, 'Hot', 2009),
#                   (5, 'Singl', 2019),
#                   (6, 'Nicotine', 2018),
#                   (7, 'Angetenar', 2018),
#                   (8, '18 Months', 2018);
# """)
#
# # Треки
#
# connection.execute("""INSERT INTO track
#              VALUES(1, 'Smells Like Teen Spirit', 5.01, 1),
#                    (2, 'In Bloom', 4.14, 1),
#                    (3, 'Radioactive', 3.08, 2),
#                    (4, 'Amsterdam', 4.01, 2),
#                    (5, 'Underdog', 3.29, 2),
#                    (6, 'Hot', 3.38, 4),
#                    (7, 'Love', 3.40, 4),
#                    (8, 'Love Tonight', 8.13, 5),
#                    (9, 'Hello', 4.55, 3),
#                    (10, 'I miss you', 5.49, 3),
#                    (11, 'Falling', 2.39, 6),
#                    (12, 'Tesla', 2.26, 7),
#                    (13, 'Paradise', 2.51, 7),
#                    (14, 'Feel So Close', 3.26, 8),
#                    (15, 'Mansion', 2.07, 8);
# """)
#
#
# # Исполнители/жанры
#
# connection.execute("""INSERT INTO artist_genre
#              VALUES(1, 1, 1),
#                    (2, 1, 2),
#                    (3, 2, 3),
#                    (4, 2, 4),
#                    (5, 3, 5),
#                    (6, 4, 6),
#                    (7, 5, 7),
#                    (8, 6, 8),
#                    (9, 2, 8);
# """)
#
# # Альбомы/исполнители
#
# connection.execute("""INSERT INTO artist_album (id, album_id, artist_id)
#              VALUES (1, 1, 1),
#                     (2, 2, 2),
#                     (3, 3, 4),
#                     (4, 4, 3),
#                     (5, 5, 5),
#                     (6, 6, 6),
#                     (7, 7, 7),
#                     (8, 8, 8);
# """)
#
# # Сборники
#
# connection.execute("""INSERT INTO collection
#              VALUES(1, 'Top 100', 2020),
#                    (2, 'Club Music', 2018),
#                    (3, 'Rock Legends', 2015),
#                    (4, 'Pop music', 2019),
#                    (5, 'All time hits', 2017),
#                    (6, 'Best singls', 2020),
#                    (7, 'New Hits', 2021),
#                    (8, 'Radio Hits', 2015);
# """)
#
# # Сборники/треки
#
# connection.execute("""INSERT INTO track_collection
#              VALUES (1, 3),
#                     (1, 5),
#                     (1, 1),
#                     (2, 8),
#                     (2, 3),
#                     (3, 5),
#                     (3, 8),
#                     (4, 1),
#                     (4, 3),
#                     (5, 8),
#                     (6, 4),
#                     (6, 1),
#                     (7, 8),
#                     (8, 2),
#                     (8, 1),
#                     (9, 6),
#                     (9, 1),
#                     (10, 4),
#                     (11, 7),
#                     (11, 2),
#                     (12, 2),
#                     (12, 8),
#                     (13, 7),
#                     (13,2),
#                     (14, 8),
#                     (15, 1),
#                     (15, 8);
#
#
# """)

# connection.execute("""DELETE FROM track_collection
#                         WHERE track_id = 5;
# """)

# connection.execute("""UPDATE album
#                         SET year = 2020
#                         WHERE id = 7;
# """)

# # Альбомы, вышедшие в 2018 году
#
# res = connection.execute("""SELECT name, year FROM album
#               WHERE year = 2018;
# """).fetchall()
# print(f'Альбомы, выпущенные в 2018 году: {res}')
#
# # Название и длительность самого продолжительного трека
#
# res = connection.execute("""SELECT name, duration FROM track
#               ORDER BY duration DESC;
# """).fetchall()
# print(f'Самый долгий трек: {res[0]}')
#
# # название треков, продолжительность которых не менее 3,5 минуты
#
# res = connection.execute("""SELECT name, duration FROM track
#               WHERE duration >= 3.5;
# """).fetchall()
# print(f'Треки, продолжительность которых не менее 3,5 минуты: {res}')
#
# # названия сборников, вышедших в период с 2018 по 2020 год включительно
#
# res = connection.execute("""SELECT name, year FROM collection
#               WHERE year BETWEEN 2018 AND 2020
# """).fetchall()
# print(f'Сборники, выпущенные с 2018 по 2020 включительно: {res}')
#
# # исполнители, чье имя состоит из 1 слова
# res = connection.execute("""SELECT name FROM artist;
# """).fetchall()
# names = []
# for name in res:
#     if ' ' not in name[0]:
#         names.append(name[0].strip(','))
# print(f'Исполнители, чье имя состоит из 1 слова: {names}')
#
# # названия треков, которые содержат слово "мой"/"my"
#
# res = connection.execute("""SELECT name FROM track
#               WHERE name LIKE '%%my%%';
# """).fetchall()
# print(f'Треки,которые содержат слово "мой"/"my" : {res}')

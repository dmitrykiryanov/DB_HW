create table if not exists artist (
	id serial primary key,
	name varchar(40) unique not null
);
create table if not exists album (
	id serial primary key,
	name varchar(40) not null,
	year integer not null,
	artist_id integer references artist(id)
);
create table if not exists track (
	id serial primary key,
	name varchar(40) not null,
	duration numeric not null,
	album_id integer references album(id)
);
alter table album drop constraint album_artist_id_fkey;
alter table album drop column artist_id;
create table if not exists artist_album (
	id serial primary key,
	album_id integer not null references album(id),
	artist_id integer not null references artist(id)
);
create table if not exists genre (
	id serial primary key,
	name varchar (40) not null
);
create table if not exists artist_genre (
	id serial primary key,
	genre_id integer not null references genre(id),
	artist_id integer not null references artist(id)
);
create table if not exists collection (
	id serial primary key,
	name varchar (40) not null,
	year integer not null check (year > 0)
);
create table if not exists track_collection (
	track_id integer references track(id),
	collection_id integer references collection(id),
	constraint pk primary key (track_id, collection_id)
);
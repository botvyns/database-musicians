import sqlite3

conn = sqlite3.connect('musicians.db')

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS band (
	band_id integer primary key,
	band_name text, 
	label_id integer,
	stage_id integer,
	FOREIGN KEY (label_id) REFERENCES record_label(label_id),
	FOREIGN KEY (stage_id) REFERENCES eskadron_fest_stage_name(stage_name))
	 """)

c.execute("""CREATE TABLE IF NOT EXISTS eskadron_fest_stage_name (
	stage_id integer primary key,
	stage_name text, 
	performance_start text)
	""")

c.execute("""CREATE TABLE IF NOT EXISTS record_label (
	label_id integer primary key,
	label_name text, 
	ceo_name text,
	country text)
	""")

c.execute("""CREATE TABLE IF NOT EXISTS member (
	member_id integer primary key,
  member_name text, 
	role text, 
	band_id int,
	FOREIGN KEY (band_id) REFERENCES band(band_id))
	""")

c.execute("""CREATE TABLE IF NOT EXISTS album (
	album_id integer primary key,
	album_name text, 
	year integer,
	band_id integer,
	FOREIGN KEY (band_id) REFERENCES band(band_id))
	""")

c.execute("""CREATE TABLE IF NOT EXISTS instrument (
	instrument_id integer primary key,
	instrument_name text)
	""")

c.execute("""CREATE TABLE IF NOT EXISTS instrument_album (
	instrument_id integer,
	album_id integer,
	FOREIGN KEY (instrument_id) REFERENCES instrument(instrument_id),
	FOREIGN KEY (album_id) REFERENCES album(album_id))
	""")

bands = [(1, 'White Ward', 1, 3), (2, 'Drudkh', 2, 1), (3, 'Cukor Bila Smerť', 3, 2)]

for band in bands:
	c.execute("INSERT INTO band VALUES (?, ?, ?, ?)", (band))
	conn.commit()

stages = [(1, 'Old joy', '16:00'), (2, 'Mystery', '16:30'), (3, 'Post-black', '17:00')]

for stage in stages:
	c.execute("INSERT INTO eskadron_fest_stage_name VALUES (?, ?, ?)", (stage))
	conn.commit()

labels = [(1, 'Debemur Morti Productions', 'Phil Void', 'France'), (2, 'Season of Mist', 'Michael Berberian', 'France'), (3, 'Koka Records', 'Volodymyr Nakonetchny', 'Ukraine')]

for label in labels:
	c.execute("INSERT INTO record_label VALUES (?, ?, ?, ?)", (label))
	conn.commit()

albums = [
	(1, 'False Light', 2022, 1),
	(2, 'Blood In Our Wells', 2010, 2), 
	(3, 'Lilei I Amarillisy', 1989, 3), 
	(4, 'Love Exchange Failure', 2019, 1), 
	(5, 'Autumn Aurora', 2010, 2), 
	(6, 'Futility Report', 2017, 1)
	]

for album in albums:
	c.execute("INSERT INTO album VALUES (?, ?, ?, ?)", (album))
	conn.commit()

members = [
	(1,'Svitlana Nianio','singer-songwriter', 3), 
	(2, 'Jevhen Taran', 'musician', 3), 
	(3, 'Yuriy Kazaryan', 'guitars', 1),
	(4, 'Adriy Pechatkin', 'vocals', 1), 
	(5, 'Yevhenii Karamushko', 'drums', 1), 
	(6, 'Mykola Jack', 'guitar', 1), 
	(7, 'Dima Dudko', 'saxophone', 1), 
	(8, 'Roman Saenko',  'guitars, bass', 2), 
	(9, 'Thurious', 'vocals', 2), 
	(10, 'Krechet', 'bass', 2), 
	(11, 'Vlad', 'drums, keyboards', 2)
	]

for member in members:
	c.execute("INSERT INTO member VALUES (?, ?, ?, ?)", (member))
	conn.commit()

instruments = [
	(1, 'saxophone'), 
	(2, 'trumpet'),
	(3, 'piano'),
	(4, 'guitar'),
	(5, 'drums'),
	(6, 'keyboard'),
	(7, 'cello')
]

for instrument in instruments:
	c.execute("INSERT INTO instrument VALUES (?, ?)", (instrument))
	conn.commit()


instruments_albums = [
	(1, 1),
	(1, 4), 
	(1, 6), 
	(2, 1), 
	(3, 1), 
	(3, 3), 
	(4, 1), 
	(4, 2), 
	(4, 4), 
	(4, 5), 
	(4, 6), 
	(5, 1), 
	(5, 2), 
	(5, 4), 
	(5, 5), 
	(5, 6), 
	(6, 4), 
	(6, 3), 
	(7, 3)
]

for instrument_album in instruments_albums:
 	c.execute("INSERT INTO instrument_album VALUES (?, ?)", (instrument_album))
 	conn.commit()

conn.close()
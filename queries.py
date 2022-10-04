import sqlite3

def first_query():
	conn = sqlite3.connect('musicians.db')
	c = conn.cursor()

	c.execute("SELECT member_name, role FROM member WHERE band_id = 3")

	query = c.fetchall()

	print("*****************")
	for item in query:
		print(item)

	conn.commit()
	conn.close()


first_query()

# ('Svitlana Nianio', 'singer-songwriter')
# ('Jevhen Taran', 'musician')

def second_query():
	conn = sqlite3.connect('musicians.db')
	c = conn.cursor()

	c.execute("SELECT band_name, album_name FROM band INNER JOIN album ON band.band_id = album.band_id")

	second_query = c.fetchall()

	print("------------------")
	for item in second_query:
	 	print(item)

	conn.commit()
	conn.close()

second_query()

# ('White Ward', 'False Light')
# ('Drudkh', 'Blood In Our Wells')
# ('Cukor Bila Smerť', 'Lilei I Amarillisy')
# ('White Ward', 'Love Exchange Failure')
# ('Drudkh', 'Autumn Aurora')
# ('White Ward', 'Futility Report')

def update_tables():
	conn = sqlite3.connect('musicians.db')
	c = conn.cursor()

	c.execute("UPDATE member SET member_name = 'No second member' WHERE member_id = 2")
	conn.commit()

	first_query()

	c.execute("UPDATE album set album_name = 'No album' WHERE band_id = 1")
	conn.commit()

	second_query()

	conn.close()

update_tables()

# ('Svitlana Nianio', 'singer-songwriter')
# ('No second member', 'musician')
# ------------------
# ('White Ward', 'No album')
# ('Drudkh', 'Blood In Our Wells')
# ('Cukor Bila Smerť', 'Lilei I Amarillisy')
# ('White Ward', 'No album')
# ('Drudkh', 'Autumn Aurora')
# ('White Ward', 'No album')
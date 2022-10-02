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

def update_table():
	conn = sqlite3.connect('musicians.db')
	c = conn.cursor()

	c.execute("UPDATE member SET member_name = 'No second member' WHERE member_id = 2")
	conn.commit()

	first_query()

	c.execute("UPDATE album set album_name = 'No album' WHERE band_id = 1")
	conn.commit()

	second_query()

	conn.close()

update_table()
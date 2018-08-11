import sqlite3

with open('data.csv','w+') as write_file:
	conn=sqlite3.connect('db.sqlite3')
	cursor=conn.cursor()
	write_file.write("trans id")
	write_file.write(",")
	write_file.write("quantity")
	write_file.write(",")
	write_file.write("time")
	write_file.write(",")
	write_file.write("item id")
	write_file.write(",")
	write_file.write("client id")
	write_file.write("\n")
	for row in cursor.execute('SELECT * FROM Inventory_transaction'):
		trans_id=row[0]
		quantity=row[1]
		time=row[2]
		client_id=row[3]
		item_id=row[4]
		write_file.write("%d"%trans_id)
		write_file.write(",")
		write_file.write("%d"%quantity)
		write_file.write(",")
		write_file.write(time)
		write_file.write(",")
		write_file.write("%d"%item_id)
		write_file.write(",")
		write_file.write("%d"%client_id)
		write_file.write("\n")
		
		


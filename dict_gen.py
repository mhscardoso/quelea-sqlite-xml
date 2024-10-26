import sqlite3

con = sqlite3.connect("in/ARA.sqlite")

cur = con.cursor()

print("{")

for row in cur.execute("""SELECT * FROM book"""):
	print(f"\t\"{row[-1]}\": \"\"")

print("}")

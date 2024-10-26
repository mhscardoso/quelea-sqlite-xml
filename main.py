import sqlite3

# Para mudar o nome dos arquivos
# mude estas variáveis.
sqlite_filename = 'in/ARA.sqlite'
xml_filename = 'out/ARA.xml'

base = {
	"Gênesis": "Gn",
	"Êxodo": "Êx",
	"Levítico": "Lv",
	"Números": "Nm",
	"Deuteronômio": "Dt",
	"Josué": "Js",
	"Juízes": "Jz",
	"Rute": "Rt",
	"1 Samuel": "1Sm",
	"2 Samuel": "2Sm",
	"1 Reis": "1Rs",
	"2 Reis": "2Rs",
	"1 Crônicas": "1Cr",
	"2 Crônicas": "2Cr",
	"Esdras": "Ed",
	"Neemias": "Ne",
	"Ester": "Et",
	"Jó": "Jó",
	"Salmos": "Sl",
	"Provérbios": "Pv",
	"Eclesiastes": "Ec",
	"Cânticos": "Ct",
	"Isaías": "Is",
	"Jeremias": "Jr",
	"Lamentações": "Lm",
	"Ezequiel": "Ez",
	"Daniel": "Dn",
	"Oséias": "Os",
	"Joel": "Jl",
	"Amós": "Am",
	"Obadias": "Ob",
	"Jonas": "Jn",
	"Miquéias": "Mq",
	"Naum": "Na",
	"Habacuque": "Hc",
	"Sofonias": "Sf",
	"Ageu": "Ag",
	"Zacarias": "Zc",
	"Malaquias": "Ml",
	"Mateus": "Mt",
	"Marcos": "Mc",
	"Lucas": "Lc",
	"João": "Jo",
	"Atos dos Apóstolos": "At",
	"Romanos": "Rm",
	"1 Coríntios": "1Co",
	"2 Coríntios": "2Co",
	"Gálatas": "Gl",
	"Efésios": "Ef",
	"Filipenses": "Fp",
	"Colossenses": "Cl",
	"1 Tessalonicenses": "1Ts",
	"2 Tessalonicenses": "2Ts",
	"1 Timóteo": "1Tm",
	"2 Timóteo": "2Tm",
	"Tito": "Tt",
	"Filemom": "Fm",
	"Hebreus": "Hb",
	"Tiago": "Tg",
	"1 Pedro": "1Pe",
	"2 Pedro": "2Pe",
	"1 João": "1Jo",
	"2 João": "2Jo",
	"3 João": "3Jo",
	"Judas": "Jd",
	"Apocalipse": "Ap"
}

header = """<?xml version="1.0" encoding="utf-8"?>
<XMLBIBLE xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="zef2005.xsd" version="2.0.1.18" status="v" biblename="Almeida Revista Atualizada" revision="3" type="x-bible">
"""
con = sqlite3.connect(sqlite_filename)
cur = con.cursor()

def start_book(file, book_name, book_number, book_base):
	file.writelines(f"  <BIBLEBOOK bnumber=\"{book_number}\" bname=\"{book_name}\" bsname=\"{book_base}\">\n")

def end_book(file):
	file.writelines("  </BIBLEBOOK>\n")

def start_chapter(file, chapter_number):
	file.writelines(f"    <CHAPTER cnumber=\"{chapter_number}\">\n")

def end_chapter(file):
	file.writelines("    </CHAPTER>\n")

def verse(file, verse_number, verse_text):
	file.writelines(f"      <VERSE vnumber=\"{verse_number}\">{verse_text}</VERSE>\n")


last_chapter = 1
last_verse = 1

with open(xml_filename, "w") as file:
	file.writelines(header)

	rows = cur.execute("""SELECT * FROM verse""").fetchall()

	for row in rows:
		if row[3] <= last_verse:

			if row[0] != 1:
				end_chapter(file)

			if row[2] <= last_chapter:

				if row[1] != 1:
					end_book(file)

				new_book_info = cur.execute(f"SELECT id, name FROM book WHERE id = {row[1]}").fetchone()
				new_book_base = base[new_book_info[1]]

				start_book(file, new_book_info[1], new_book_info[0], new_book_base)


			start_chapter(file, row[2])

		verse(file, row[3], row[4])

		last_verse = row[3]
		last_chapter = row[2]


	end_chapter(file)
	end_book(file)

	file.write("</XMLBIBLE>")

con.close()

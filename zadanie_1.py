import sqlite3

con = sqlite3.connect('mydb_Belyatskaya.db')

cursor = con.cursor()

cursor.execute('''create table top10_films
(id integer primery key autoinctement,
name varchar(100),
top varchar(50),
year date,
director varchar(100),
genre varchar(50)
);''')

data = [('The Shawshank Redemption', 9.3, 1994, 'Frank Darabont','Tragedy'), ('The Godfather', 9.2, 1972, 'Francis Ford Coppola', 'Epic'), ('The Dark Knight', 9.0, 2008, 'Christopher Nolan', 'Action Epic'), ('The Godfather Part II', 9.0, 1974, 'Francis Ford Coppola', 'Epic'), ('12 Angry Men', 9.0, 1957, 'Sidney Lumet', 'Psychological Drama'), ('Schindler`s List', 9.0, 1993, 'Steven Spielberg', 'Historical Epic'), ('The Lord of the Rings: The Return of the King', 9.0, 2003, 'Peter Jackson', 'Adventure Epic'), ('Pulp Fiction', 8.9, 1994, 'Quentin Tarantino', 'Dark Comedy'), ('The Lord of the Rings: The Fellowship of the Ring', 8.9, 2001, 'Peter Jackson', 'Fantasy Epic'), ('Il buono, il brutto, il cattivo', 8.8, 1966, 'Sergio Leone', 'Quest')]
cursor.executemany('insert into top10_films (name, top, year, director, genre) values (?, ?, ?, ?, ?)', data)
con.commit()
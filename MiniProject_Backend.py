#backend
import sqlite3

def MovieData():
    con=sqlite3.connect("movie1.db") 
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, Movie_ID text,Movie_Name text,Release_Date text,Director text,Cast text,Budget text,Duration text,Rating text)")
    con.commit()
    con.close()
    
def AddMovieRec(Movie_ID,Movie_Name,Release_Date,Director,Cast,Budget,Duration,Rating):
    con=sqlite3.connect("movie1.db")    
    cur=con.cursor()
    cur.execute("INSERT INTO book VALUES (NULL, ?,?,?,?,?,?,?,?)", (Movie_ID,Movie_Name,Release_Date,Director,Cast,Budget,Duration,Rating))
    con.commit()
    con.close()

def ViewMovieData():
    con=sqlite3.connect("movie1.db")    
    cur=con.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    con.close()    
    return rows

def DeleteMovieRec(id):    
    con=sqlite3.connect("movie1.db")    
    cur=con.cursor()
    cur.execute("DELETE FROM book WHERE id=?", (id,))
    con.commit()
    con.close()  

def SearchMovieData(Movie_ID="",Movie_Name="",Release_Date="",Director="",Cast="",Budget="",Duration="",Rating=""):  
    con=sqlite3.connect("movie1.db")    
    cur=con.cursor()
    conditions = []
    params = []
    if Movie_ID:
        conditions.append("Movie_ID=?")
        params.append(Movie_ID)
    if Movie_Name:
        conditions.append("Movie_Name=?")
        params.append(Movie_Name)
    if Release_Date:
        conditions.append("Release_Date=?")
        params.append(Release_Date)
    if Director:
        conditions.append("Director=?")
        params.append(Director)
    if Cast:
        conditions.append("Cast=?")
        params.append(Cast)
    if Budget:
        conditions.append("Budget=?")
        params.append(Budget)
    if Duration:
        conditions.append("Duration=?")
        params.append(Duration)
    if Rating:
        conditions.append("Rating=?")
        params.append(Rating)
    if conditions:
        query = "SELECT * FROM book WHERE " + " OR ".join(conditions)
    else:
        query = "SELECT * FROM book"
    cur.execute(query, params)
    rows=cur.fetchall()
    con.close()    
    return rows

def UpdateMovieData(id,Movie_ID="",Movie_Name="",Release_Date="",Director="",Cast="",Budget="",Duration="",Rating=""):
    con=sqlite3.connect("movie1.db")    
    cur=con.cursor()
    cur.execute("UPDATE book SET Movie_ID=?,Movie_Name=?,Release_Date=?,Director=?,Cast=?,Budget=?,Duration=?,Rating=? WHERE id=?",(Movie_ID,Movie_Name,Release_Date,Director,Cast,Budget,Duration,Rating,id))
    con.commit()
    con.close()


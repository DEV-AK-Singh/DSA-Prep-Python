import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

def initialize_database():
    try:
        cursor.execute("""
            CREATE TABLE movies (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                duration TEXT NOT NULL
            )
        """)
        conn.commit()
        print("Table created successfully")
    except sqlite3.OperationalError as e:
        print("Table already exists =>", e)

def add_movie(data):
    cursor.execute("INSERT INTO movies (name, duration) VALUES (?, ?)", data)
    conn.commit()

def get_movie(id):
    cursor.execute("SELECT * FROM movies WHERE id = ?", (id,))
    return cursor.fetchone()

def delete_movie(id):
    cursor.execute("DELETE FROM movies WHERE id = ?", (id,))
    conn.commit()

def update_movie(id, data):
    cursor.execute(f"UPDATE movies SET name = ?, duration = ? WHERE id = {id}", data)
    conn.commit()

def list_movies():
    cursor.execute("SELECT * FROM movies")
    for row in cursor.fetchall():
        print(row)

def main():
    initialize_database()
    while True:
        print("1. Add movie")
        print("2. Get movie")
        print("3. Delete movie")
        print("4. Update movie")
        print("5. List movies")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter movie name: ")
            duration = input("Enter movie duration: ")
            add_movie((name, duration))
        elif choice == "2":
            id = int(input("Enter movie id: "))
            print(get_movie(id))
        elif choice == "3":
            id = int(input("Enter movie id: "))
            delete_movie(id)
        elif choice == "4":
            id = int(input("Enter movie id: "))
            name = input("Enter movie name: ")
            duration = input("Enter movie duration: ")
            update_movie(id, (name, duration))
        elif choice == "5":
            list_movies()
        elif choice == "6":
            break
        else:
            print("Invalid choice!")
    conn.close()  

if __name__ == "__main__":
    main()    
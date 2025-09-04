import sqlite3

conn = sqlite3.connect('youtube_videos.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
             id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )
''')


def list_all_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()

def update_video(new_name, new_time, video_id):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
    conn.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    conn.commit()


def main():
    while True:
        print("\n Youtube Manager App with DB")
        print("1. List Videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. Exit App")

        choice = input("Enter your Choice: ")

        match choice:
            case '1':
                list_all_videos()

            case '2':
                name = input("Enter video name: ")
                time = input("Enter video time: ")
                add_video(name, time)

            case '3':
                video_id = input("Enter video ID to update: ")
                name = input("Enter video name: ")
                time = input("Enter video time: ")
                update_video(name, time, video_id)

            case '4':
                video_id = input("Enter video ID to delete: ")
                delete_video(video_id)

            case '5':
                break
            case _:
                print("Invalid choice!!")

            
    conn.close()

if __name__ == "__main__":
    main()
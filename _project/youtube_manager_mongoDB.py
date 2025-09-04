from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongo url", tlsAllowInvalidCertificates=True)

db = client["pyProject"]
video_collection = db["videos"]

print(video_collection)

def list_videos():
    for video in video_collection.find():
        print(f"ID: {video['_id']}, Name: {video['name']}, Time: {video['time']}")

def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})

def update_video(video_id, new_name, new_time):
    video_collection.update_one(
        {'_id': ObjectId(video_id)},
        {"$set": {"name": new_name, "time": new_time}}
    )

def delete_video(video_id):
    video_collection.delete_one({"_id": ObjectId(video_id)})

def main():
    while True:
        print("\n Youtube Manager App")
        print("1. List all Videos")
        print("2. Add a new Video")
        print("3. Update a Video")
        print("4. Delete a Video")
        print("5. Exit App")

        choice = input("Enter your choice: ")

        match choice:
            case '1':
                list_videos()
            case '2':
                name = input("Enter the video name: ")
                time = input("Enter the video time: ")
                add_video(name,time)
            case '3':
                video_id = input("Enter the video id to update: ")
                name = input("Enter the video name: ")
                time = input("Enter the video time: ")
                update_video(video_id, name, time)
            case '4':
                video_id = input("Enter the video id to delete: ")
                delete_video(video_id)
            case '5':
                break
            case _:
                print("Invalid choice!!")                


if __name__ == "__main__":
    main()
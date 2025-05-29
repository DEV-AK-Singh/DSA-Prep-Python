def add_video(videos):
    title = input("Enter video title: ")
    url = input("Enter video URL: ")
    videos.append((title, url)) 
    print("Video added successfully!")

def update_video(videos):
    title = input("Enter video title: ")
    url = input("Enter video URL: ")
    for i, video in enumerate(videos):
        if video[0] == title:
            videos[i] = (title, url)
            print("Video updated successfully!")
            return
    print("Video not found!")

def remove_video(videos):
    title = input("Enter video title: ")
    for i, video in enumerate(videos):
        if video[0] == title:
            del videos[i]
            print("Video removed successfully!")
            return
    print("Video not found!")

def list_videos(videos):
    for i, video in enumerate(videos):
        print(f"{i+1}. {video[0]} - {video[1]}")
        print("\n")
        print("\n")
            
def main():
    videos = []
    while True:
        print("1. Add video")
        print("2. Update video")
        print("3. Remove video")
        print("4. List videos")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_video(videos)
        elif choice == "2":
            update_video(videos)
        elif choice == "3":
            remove_video(videos)
        elif choice == "4":
            list_videos(videos)
        elif choice == "5":
            break
        else:
            print("Invalid choice!") 

if __name__ == "__main__":
    main()            
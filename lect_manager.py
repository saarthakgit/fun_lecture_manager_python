import json

def list_videos(videos):
    for index, video in enumerate(videos, start=1):
        print(f"{index} - {video['Lecture']} ~ Duration: {video['Duration']} ")
    print("\n")


def save(videos):
    with open("lectures.txt","w") as file:
        json.dump(videos,file)


def load_data():
    try:
        with open("lectures.txt","r") as file:
            data=json.load(file)
            return data
    except FileNotFoundError:
        return []
    
def add_new(videos):
    video=input("Enter Lecture Name: ")
    duration=input("Enter Lecture Duration: ")
    videos.append({"Lecture":video,"Duration":duration})
    save(videos)
    print("Success!")

def update(videos):
    indices=[]
    for index,video in enumerate(videos,start=1):
        indices.append(index)
    while True:
        try:
            lecnum=int(input("Enter lecture number to update: "))
            if lecnum in indices:
                while True:
                    what=input("What do you want to update? D-Duration,N-Name: ").lower()
                    if what=="d":
                        new=input("Enter new duration:")
                        video=videos[lecnum-1]
                        video["Duration"]=new
                        print("Success!")
                        print(f"Updated Value --> {index} - {video['Lecture']} ~ Duration: {video['Duration']} ")
                        break
                    elif what=="n":
                        new=input("Enter new name:")
                        video=videos[lecnum-1]
                        video["Lecture"]=new
                        print("Success!")
                        print(f"Updated Value --> {index} - {video['Lecture']} ~ Duration: {video['Duration']} ")
                        break
                    else:
                        print("Invalid choice")
                        continue
                break
                
            else:
                print("Invalid Lecture Number || No such lecture")
                continue
        except ValueError:
            print("ENTER A NUMBER!")

def delete_completed(videos):
    delete = int(input("Enter lecture number to delete: "))
    indices=[]
    for index,video in enumerate(videos,start=1):
        indices.append(index)
    if delete in indices:
        videos.remove(videos[delete-1])
        print("Success!!   UPDATED_LIST-->")
        list_videos(videos)



def main():
    videos=load_data()
    print(videos)
    while True:
        print('''
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            
                        +  Lecture Manager  +
                        ||Choose an option||
                1.List pending lectures
                2.Add a new lecture
                3.Update/Change exisiting lecture details
                4.Delete Completed Lecture
                5.Exit
            

            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            
        ''')
        choice=input("Enter choice:")

        match choice:
            case "1":
                list_videos(videos)
            case "2":
                add_new(videos)
            case "3":
                update(videos)
            case "4":
                delete_completed(videos)
            case "5":
                print("Goodbye, Happy Learning!")
                break
            case _:
                print("Enter a Valid choice!")


if __name__ == "__main__":
    main()
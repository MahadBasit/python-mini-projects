while True:
    mode = input("Do you want to Read, Write or Delete a note (Type R for Reading, W for Writing and D for Deletion): ").upper()
    if mode in ("W", "R", "D"):
        break


if mode == 'R':
    notelist = []
    try:
        with open("notes.txt", ) as file:
            lines = file.readlines()
            for line in lines:
                notelist.append(line.rstrip())
            
            for i in notelist:
                print(i)

    except FileNotFoundError:
        print("File not found")

elif mode == "W":
    with open("notes.txt", "a") as file:
        while True:
            notes = input("What do you want to write (Type here): ")
            if len(notes) != 0:
                file.write(f'{notes}\n')
            else:
                continue
            cont = input("Do you want to contniue?(Y for Yes, N for No): ").upper()
            if cont == 'N':
                break

else:
    notelist = []
    try:
        with open('notes.txt') as file:
            lines = file.readlines()
            for line in lines:
                notelist.append(line.rstrip())

            print("Which line to Delete: ")
            for i, note in enumerate(notelist):
                print(i, note)

            dl = input("Enter the index of line to Delete: ")
            notelist.pop(int(dl))

            with open('notes.txt', 'w') as file:
                for i in notelist:
                    file.write(f'{i}\n')

    except FileNotFoundError:
        print("File not found")
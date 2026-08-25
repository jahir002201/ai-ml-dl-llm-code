with open("students.txt", "r") as file:

    print("Initial cursor:", file.tell())

    content = file.read(7)

    print("Read:", content)

    print("Current cursor:", file.tell())

    file.seek(0)

    print("Cursor after seek:", file.tell())

    print("\nFull file:")
    print(file.read())
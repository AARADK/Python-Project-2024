def initialize():
    with open("initpass.txt", "rt") as source_file:
        lines = source_file.read()

    with open("passwd.txt", "w") as destination_file:
        destination_file.write(lines)
    
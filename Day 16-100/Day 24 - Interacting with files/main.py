with open("C:\\Users\Ingrid\Desktop\my_file.txt") as f:
    contents = f.read()
    print(contents)

with open("C:\\Users\Ingrid\Desktop\my_file.txt", mode="a") as f:
    f.write("\nSome new text.")
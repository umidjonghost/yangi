

file = open("example.txt", "r")
content = file.read()
print(content)
file.close()

with open("example.txt", "r") as file:
    content = file.read()
    print(content)


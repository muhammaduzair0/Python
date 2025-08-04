# Syntax of file open & close


file = open("youtube.txt", "w")

try:
    file.write("Hello Python")
finally:
    file.close()

with open("youtube.txt", "w") as file:
    file.write("Hello Python 101")
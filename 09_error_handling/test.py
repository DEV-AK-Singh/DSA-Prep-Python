file = open("text.txt", "r")
try:
    print(file.read())
except Exception as e:
    print(e)
finally:
    file.close()
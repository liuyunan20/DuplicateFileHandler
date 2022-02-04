# read test.txt
f1 = open("test.txt", "r", encoding="utf-8")
first_letters = f1.readlines()
for line in first_letters:
    print(line[0])

f1.close()

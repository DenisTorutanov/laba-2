k = int(input('Введите число: '))
with open("text.txt", "r") as f:
   content = f.read()
i = 0
while i < len(content):
    while len(content) > i and not content[i].isdigit():
        i += 1
    count = 0
    while len(content) > i and content[i].isdigit():
        count += 1
        i +=1
    if count > k and count % 2 !=0:
        print(content[i-count:i], end = " ")


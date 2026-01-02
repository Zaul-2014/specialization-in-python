file = open('Data.txt', 'r')

count = 0

content = file.read()

list = content.split('\n')

for i in list:
  if i:

    count = count + 1

print("Number of lines : " ,count)
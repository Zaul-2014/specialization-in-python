with open('Data.txt', 'r') as file:
  Data = file.readlines()
  for lines in Data:
    word = lines.split()
    print(word)

file.close()
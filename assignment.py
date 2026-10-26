# Ans to the qustion no 1 

numbers = input(). split()

numbers = [int(number) for number in numbers]
result = []

for number in numbers:
  if number % 4 == 0 and number % 8!= 0:
    result.append(number)

print(result)


# Ans to the qustion no 2

def adder(x, y):
  return x + y

def compute_ratio(x,y):
   # adder function added
  try:
    result= adder(x,y)/ (x*y)

  except ZeroDivisionError:
    print("Error: Division not possible")

  else:
    print(result)



x, y = input().split()
x,y = int(x),int(y)

compute_ratio(x, y)


# Ans to the qustion no 3
with open ("./sample_data/data.txt", "w") as file:
  file.write("Python is wonderful language for maching learning")

with open("./sample_data/data.txt", "r" ) as file:
  strings = file.read()
  print(strings)

  #word ber korbo
  words= strings.split()
  print(words)

#total character
  total_character = list(map(len, words))
  print(total_character)

  # shobceye boro length
  longest_length = max(total_character)
  print(longest_length)


  for word in words:
    if len(word) == boro_word:
      print(word)
      break

    print(boro_word)

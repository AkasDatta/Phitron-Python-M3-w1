# Ans to the question no 1 

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


# Ans to the question no 3
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




# Ans to the question no 4

sentence = input("Enter sentence: ")

words = sentence. split()

vowels = ["a", "e","i", "o","u"]

vowel_words = []

# vowel_words = list(map(lambda x : x[0].lower(),x))
for x in words:
  if x[0].lower() in vowels:
    vowel_words.append(x)

print(vowel_words)



# Ans to the question no 5

word = input("Enter word: ")

word = word.lower()
# reverse
reverse_word =""

for letter in word:
  reverse_word= letter + reverse_word

print(reverse_word)

# palendrome check korbo
if word == reverse_word:
  print("Palendome")

else:
  print("Not Palendrome")
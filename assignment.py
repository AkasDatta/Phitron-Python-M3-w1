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
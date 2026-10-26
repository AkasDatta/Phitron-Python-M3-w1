# Ans to the qustion no 1 

numbers = input(). split()

numbers = [int(number) for number in numbers]
result = []

for number in numbers:
  if number % 4 == 0 and number % 8!= 0:
    result.append(number)

print(result)
# Define `plus()` function to accept a variable number of arguments
def plus(*args):
  total = 0
  for i in args:
    total += i
  return total

# Calculate the sum
print(plus(20,30,40,50))
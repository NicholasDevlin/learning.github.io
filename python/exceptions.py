import sys

try:
  x = int(input("x : "))
  y = int(input("y : "))
except ValueError:
  print("Error: value input")
  sys.exit(1)

try:
  result = x / y
except ZeroDivisionError:
  print("can't divided by zero")
  sys.exit(1)


print(f" {x} / {y} = {result}")
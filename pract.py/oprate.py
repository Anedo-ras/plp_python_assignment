operate = input("Enter the oparetor (+,-,/,*)")
num1 = float(input("enter the first number"))
num2 = float(input("enter the second number"))

if operate == "+":
  result = num1+num2
  print(result)
elif operate == "-":
  result = num1 - num2
  print(result)
elif operate == "*":
  result = num1 * num2
  print(result)
elif operate == "/":
  result = num1 / num2
  print(result)
else:
  print("is not valid")
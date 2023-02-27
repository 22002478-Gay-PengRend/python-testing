num1 = float(input("Key in a floating number: "))
num2 = float(input("Key in another floating number: "))
sign = input("Key in either + or - or * or /: ")

if sign == "+":
    ans = num1 + num2
elif sign == "-":
    ans = num1 - num2
elif sign == "*":
    ans = num1 * num2
elif sign == "/":
    ans = num1 / num2
else:
    print("Invalid input")

print("Final answer is", ans)

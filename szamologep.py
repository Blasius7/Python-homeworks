a = float(input("Üss be egy számot! "))
b = float(input("Üss be egy másikat! "))
mod = input("Adj egy műveletet! ")

if mod == "+":
    print(a + b)
elif mod == "-":
    print(a - b)
elif mod == "*":
    print(a * b)
elif mod == "/":
    print(a / b)
else:
    print("Nem értek halandzsául...")

#J. Looping Constructs
"""Use Case 1: Table Generator
 Write a program that takes a number from the user and prints the multiplication table from 1 to 10 for that number."""
Number=int(input("Enter a  number:"))
print(f"The Multiplication of {Number} ")
for i in range(1,11):
   print(Number,"*",i,"=",i*Number)
else :
    print ("Enter a valid number")

#Use Case 2: Sum of Even and Odd Numbers
"""Write a program that asks the user for a positive integer n.
 Using a loop, calculate and print:
Sum of all even numbers from 1 to n
Sum of all odd numbers from 1 to n """

number=int(input("Enter a  number:"))
even=0
odd=0
for i in range(1,number+1):
    if i%2==0:
        even+=i

    else :
        odd+=i
print(f"The Sum of {number} is {even}")
print(f"The Sum of {number} is {odd}")

#Use Case 3 (Bug Fixing): Infinite Loop Issue
"""Fix the code below so that it prints numbers from 1 to 10 and stops correctly.
Incorrect code:
i = 1
 while i <= 10:
 print(i)
Expected behavior:
 The program must increment i and stop when 10 is printed. """

i=1
while i <= 10:
    print(i)
    i+=1
    if i==11:
        break
#K. Collection Types
"""Use Case 1: Product Price Lookup
Create a dictionary with at least 5 products and their prices.
Ask the user to enter a product name.
If found, print the price.
If not found, print: "Product not available." (Hint: use dictionary_var.get(key) function) """
Product_dict = {"Laptop":97000, "Fridge": 20000, "Mobile":45000, "WM" :37000, "TV":32000}
product =input("Enter a product name:")
price= Product_dict.get(product)
if price is not None:
    print(f"The price of {product} is {price}")
else :
    print("The product is not available")
# Use Case 2: City Entry and Duplicate Removal
    """Ask the user to enter city names repeatedly.
     Stop when the user types "exit".
    Requirements:
    Store every entered city name in a list (even if it's repeated).
    Also store the cities in a set to maintain only unique values. """
    """Finally print:
    The complete list of entered cities (with duplicates).
    The set of unique cities (duplicates removed)."""
    city_list = []

    while True:
        city = input("Enter a city name (or 'exit' to stop): ")
        if city.lower() == "exit":
            break
        else:
            city_list.append(city)

    city_set = set(city_list)

    print("Complete list:", city_list)
    print("Unique cities:", city_set)
#Use Case 3 (Bug Fixing): List Index Error
"""Fix the following code so that it prints all items correctly without an index error:
Incorrect code:
items = ["Pen", "Book", "Mouse", "Keyboard"]
 i = 0
 while i <= len(items):
 print(items[i])
 i = i + 1
Expected behavior:
 The loop should print all the items exactly once and exit without an error. """
items = ["Pen", "Book", "Mouse", "Keyboard"]
i = 0
while i <= len(items)-1:
    print(items[i])
    i = i + 1



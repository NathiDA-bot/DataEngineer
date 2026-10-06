import Function.PyFunction.Fun as f

f.printing("nathi")
f.files()
files=f.dir("C:\\Users\\NathiyaChandrababu")
print(files)
op=f.square(100)
print("The Square Root is ",op)
Final_Shopping_Bill= f.discount(900,5,50)
print(Final_Shopping_Bill)

User1=f.mail_id("nathiya", "Chandrababu","@ibm.com")
print(User1)
User2=f.mail_id("kayal", "Chandrababu")
print(User2)


try:
    food_ordered =int(input("Please enter the food ordered "))
    f.food_Counter(food_ordered)
except ValueError:
    print("Please enter a valid integer")
except Exception as e:
    print(f"The Error Message is {e}")
    print("Sorry , Try Again ")

else:
    print("The food Is successfully Delivered")
finally :
    print("Thank You for Using our App, Come Again")

#Use case 2: Salary Calculation HR Pay roll Automation
basic_salary = float(input("Enter basic salary: "))
bonus=f.calculate_bonus(basic_salary,2.5)
print("The Bonus is",bonus)
Incentives=f.calculate_incentives(1000,2000,3000)
print("The Sum of Incentives for the month",Incentives)
Gross_salary=f.gross_salary(basic_salary,bonus,Incentives)
print("The gross salary is",Gross_salary)
pf=f.calculate_pf(Gross_salary)
print("The PF is",pf)
tax=f.calculate_tax(Gross_salary,10)
print("The tax is",tax)
net_salary= f.calculate_net_salary(Gross_salary,pf,tax)
print("The net salary is",net_salary)


#Usecase3: Number Utility Tool
"""Create functions:
is_even(num) → returns True/False
find_max(*numbers) → returns highest number from arguments
perform_operation(num, operation) →
If operation = "square" → return num*num
If operation = "cube" → return numnumnum
If unknown → return "Invalid operation"


Test the functions with at least 5 numbers.
"""
Num=int(input("Enter a number:"))
Iseven= f.iseven(Num)
print("The Iseven is ",Iseven)
Max_Num=input("Enter one or more numbers:")
Max_Num=Max_Num.split()
Max_Num =[int(n) for n in Max_Num]
Result= f.find_highest(*Max_Num)
print("The Highest number  is ",Result)



Num=int(input("Enter a number:"))
oper=input("Enter operationas square/cube:")
op=f.perform_operation(Num,oper)
print("The Operation is",op)
#Callimg Function
f.find_square()
"""
Create a function generate_invoice(**products).
Each key is a product name and each value is its price.
Print all product names with prices and also print the total amount.

"""

f.generate_invoice(
    Laptop=50000,
    Mouse=1000,
    Keyboard=2000
)


#Use Case
"""
Usecase 1: Weather Station Stats - Arbitrary arguments (*args)
You are building software for a weather station. 
Throughout the day, temperature sensors send a batch of readings 
back to your system. Because the number of active sensors changes depending on the location, your function must accept any number 
of numerical readings and calculate key summary statistics. """

f.temp_sumarry(23,45,34,32,29,28,27)
"""
You are working as a software developer for an HR analytics firm (like Aon Hewitt / HRworkways). Different IT companies structure their annual employee payouts differently based on available compensation components:

CTS pays Base Salary + Bonus Percentage + Fixed Incentives.
INFY pays Base Salary + Bonus Percentage (No incentives).
HCL pays Base Salary only (No bonus, no incentives).
Because each company provides a different combination
 of compensation parameters, write a single function using **kwargs (arbitrary keyword arguments) 
 to dynamically compute the total gross salary based on whichever components are passed in.
"""

cts= f.calculate_gross_salary(base_salary= 60000,bonus_percentage=10,incentives=5000,pf=2000)
print(cts)
hcl= f.calculate_gross_salary(base_salary= 6000)
print(hcl)

f.calculate_salary(Nathi=500000,ninja=90000,sathish=10000000,vembu=12000000)
f.shopping_cart(
    laptop=50000,
    mouse=1000,
    keyboard=2000
)
f.calculate_bonus(
    Nathi=60000,
    Arun=45000,
    Priya=50000
)
def count_vowel (word):
    count=0
    for char in word :
        if char.lower() in 'aeiou':
            count+=1
    return count
print(count_vowel('Nathiya'))

def find_max(numbers):
    return max(numbers)
num=input("Enter one or more number")

numbers = [int(value) for value in num.split()]
print(find_max(numbers))
"""
Challenge: Write second_largest(numbers) to return the
 second-largest distinct number in a list. """

def second_largest(numbers):
    sorted_numbers = sorted(set(numbers),reverse=True)
    return sorted_numbers[1]

print(second_largest([12,4,6 ,12 ,8]))

def count_word(sentence):
    word= sentence.split()

    count=0
    for w in word :

        if len(w)>4 :
            count+=1
    return count

print(count_word('Nathiya is a goods girls '))

def count_letter(sentence, target) :
   word= sentence.split()
   count=0
   for char in word :
        if char.lower() == target.lower() :
            count+=1
   return count
print(count_letter('Nathiya is an AI engineer, she is a independent woman','is'))

"""
Use Case 6: Import vs from import
Create simple functions like add(a,b) and div(a,b) that  returns sum and division of 2 input.
Create a package/sub package/generic_functions.py and place this function .
"""


from Function.PyFunction.Fun import temp_sumarry as ts
ts(45,67,89)

"""
Use Case 7: global vs local variable
Create a functions add(a,b) that stores the result of a+b to variable c 
and make the variable c as global variable that should be accessible outside of the 
function after executing the function. """
def add(a,b):
    global c
    c=a+b
    return c

print(add(5,6))
print("the c i global variable",c)


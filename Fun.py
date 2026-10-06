#No input No output
from unittest import addModuleCleanup


def add():
    print("Hello World")
    a=10
    print(a)
def sub():
    print("Hello World")
    print("Am subtracting a-b")
#Only INput
def printing(name) :
    print("Hello " + name)
#No Input Only Output
def files():
    print("These are the Files in my Current Working Directory")
    import os

    path = os.getcwd()

    files = os.listdir(path)
    print(files)

#input And Output
def dir(path):
    import os
    files = os.listdir(path)
    return files

def square(num : int):
    result = num * num
    return result


# Function Definition
def discount(amount,Discount,ShippingCost):
   Discount_Amount= amount*(Discount/100)
   Final= amount-Discount_Amount+ShippingCost
   return Final
def mail_id(fname, lname, domain="@inceptez.com"):
    return fname + '.' + lname + domain

#usecase 1:Food Delivery Counter
"""Create a program to apply discount of 10% if the min amt is 600 and max cap of discount is 100 rupees."""

def food_Counter(Cart_Value):
        min_amount=600
        discount_apply= .10
        max_discount =100
        Cart_Value = int(Cart_Value)
        discount_applied= Cart_Value *discount_apply
        if Cart_Value >=min_amount :
            if discount_applied <= max_discount :
                Final_amount= Cart_Value -( Cart_Value *discount_apply)
                print(f"The final amount is {Final_amount} and u r Saving is Rs {discount_applied}")
                return Final_amount
            else :
                Final_amount=Cart_Value-100
                print(f"The final amount is {Final_amount} and u r Saving is Rs 100")
                return Final_amount
        else :
            print(f"Add the Cart value  of {Cart_Value - min_amount} Rs to get the offer" )
            return Cart_Value - min_amount
#Use Case 2:Employee Salary Calculation : Payroll Automation :
"""Demonstrates input/output functions, default arguments, arbitrary args, returning values, and composing multiple functions.
What Problem It Solves:
Companies calculate employee salary differently depending on bonus percentage, incentives, PF, tax, etc.
How Function-Based Programming Helps:
We create multiple small reusable functions (bonus calc, tax calc, net salary calc)
Then compose them together.
"""
def calculate_bonus(salary, bonus_percentage):
    bonus = salary * bonus_percentage / 100
    return bonus
def calculate_incentives(*incentives):
    return sum(incentives)
def gross_salary(salary,bonus,incentives):
    gross_salary= salary+bonus+incentives
    return gross_salary
def calculate_pf(gross_salary,pf=12):
    pf=gross_salary*pf/100
    return pf
def calculate_tax(gross_salary,tax=10):
    tax=gross_salary*tax/100
    return tax
def calculate_net_salary(gross_salary, pf, tax):
    net_salary = gross_salary - pf - tax
    return net_salary

#Use Case :3 Number Utility Tool:
def iseven(num):
    if num % 2 == 0:
        return True
    else :
        return False
def find_highest(*numbers):
    maximum=max(numbers)
    print(maximum)
    return maximum

"""
If operation = "square" → return num*num
If operation = "cube" → return numnumnum
If unknown → return "Invalid operation"""

def perform_operation(num,operation):
    if operation.lower() =="square" :
        return num*num
    elif operation.lower() =="cube" :
        return num*num*num
    else :
        return "Invalid Operation"

"""
Create a function generate_invoice(**products).
Each key is a product name and each value is its price.
Print all product names with prices and also print the total amount.
"""

def generate_invoice(**products):
    total= 0
    for product, price in products.items():
        total += price
    print("The total amount is ",total)
"""
You are building software for a weather station.
 Throughout the day, temperature sensors send a batch of readings 
 back to your system. Because the number of active sensors changes
  depending on the location, your function must accept any number of numerical readings and calculate key summary statistics.
"""
def temp_sumarry(*readings: object) -> None:
    from statistics import mean
    total=mean(readings)
    max_temp=max(readings)
    min_temp=min(readings)
    avg_temp=sum(readings)/len(readings)
    print(f"The average temperature is {avg_temp} degrees C")
    print(f"The minimum temperature is {min_temp} degrees C")
    print(f"The maximum temperature is {max_temp} degrees C")
    print(f"The Mean Temp is {total} degrees C")
"""
You are working as a software developer for an HR analytics firm (like Aon Hewitt / HRworkways). Different IT companies structure their annual employee payouts differently based on available compensation components:

CTS pays Base Salary + Bonus Percentage + Fixed Incentives.
INFY pays Base Salary + Bonus Percentage (No incentives).
HCL pays Base Salary only (No bonus, no incentives).
Because each company provides a different combination of compensation parameters, write a single function using **kwargs (arbitrary keyword arguments) to dynamically compute the total gross salary based on whichever 
components are passed in. """

def calculate_gross_salary(**salary_details):
    base_salary= salary_details.get("base_salary",0)
    bonus_percentage= salary_details.get("bonus_percentage",0)
    incentives= salary_details.get("incentives", 0)
    print(bonus_percentage)
    bonus= base_salary * bonus_percentage / 100
    gross_salary = base_salary + bonus + incentives

    return gross_salary

def mail_id(fname, lname, domain="@inceptez.com"):
    return fname + '.' + lname + domain
 # Uses default domain
mail_id("user", "one")

def mail(*name):
    return name[0]+"."+name[1] +"@incepetez.com"

def mail_id1(**name): # Receives dictionary
    return name["fname"] + '.' + name["lname"] + '@gmail.com'

def calculate_salary(**employees):
    total = 0
    for key,value in employees.items():
        print(key,":",value)
        total += value

    HIghest_Salary=max(employees.values())
    print("The total Salary is ",total)
    for key, value in employees.items():
        if value==HIghest_Salary :
            print("Highest salary :", key,":",value)


def shopping_cart(**items):
    total =0
    for item, price in items.items():
        print(item,":",price)
        total += price
    if total> 50000 :
            discount= total* 10/100
            Final_amount = total - discount
            print("The discount amount is",discount)
            print("The Final Amount is ",Final_amount)
    else :
            print("The Final Amount is ",total)


def calculate_bonus(**employees):
    bonus=0
    bonuses=[]
    for employee,salary in employees.items():
        if salary >= 60000 :
            bonus= salary * 10/100
            print(f"The bonus amount for {employee} is",bonus)
        else:
            bonus= salary * 5/100
            print(f"The bonus amount for {employee} is",bonus)
        bonuses.append(bonus)
    highest_bonus= max(bonuses)
    print(f"The highest bonus amount is {highest_bonus} ")








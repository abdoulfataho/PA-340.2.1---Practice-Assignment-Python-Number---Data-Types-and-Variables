# 1. Add two integers
int1 = 5
int2 = 10
sum_int = int1 + int2
print("Sum of integers:", sum_int)

# 2. Add two floats
float1 = 5.5
float2 = 10.5
sum_float = float1 + float2
print("Sum of floats:", sum_float)

# 3. Add an integer and a float
int3 = 7
float3 = 3.5
sum_int_float = int3 + float3
print("Sum of integer and float:", sum_int_float)  # The result is a float

# 4. Divide the larger integer by the smaller integer
int4 = 20
int5 = 4
if int4 > int5:
    division_result = int4 / int5
else:
    division_result = int5 / int4
print("Division result:", division_result)


# 1. Divide the larger float by the smaller float
float1 = 15.5
float2 = 5.5
if float1 > float2:
    division_result = float1 / float2
else:
    division_result = float2 / float1
print("Division result of floats:", division_result)

# 2. Cafe products and sales calculation
coffee_price = 3.50
cappuccino_price = 4.00
espresso_price = 2.75

# Order quantities
coffee_qty = 3
cappuccino_qty = 4
espresso_qty = 2

# Calculate subtotal
subtotal = (coffee_price * coffee_qty) + (cappuccino_price * cappuccino_qty) + (espresso_price * espresso_qty)
SALES_TAX = 0.07
totalSale = subtotal + (subtotal * SALES_TAX)
print("Subtotal:", subtotal)
print("Total Sale with tax:", totalSale)

# 3. Calculate the area of a circle
radius = 63
pi = 3.14
area_of_circle = pi * (radius ** 2)
print("Area of the circle:", area_of_circle)
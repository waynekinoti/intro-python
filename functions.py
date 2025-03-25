# functions
from variables import area_of_triangle, result


def greet():
    print('Hello functions')


def area_circle(radius):
    result = 22 / 7 * radius ** 2
    result = round(result, 2)
    # print(result)


def volume_cylinder(height, radius, precision=2):
    v = 22 / 7 * radius ** 2 * height
    v = round(v, precision)
    # print(f"radius is {radius}, height is {height}, volume is {v}")


def area_triangle(a, b, c):
    """calculates the area of a triangle then returns the result"""
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    # print(f"area is {area}")
    return area


# 4 == 4 * 3 * 2 * 1

def factorial(num):
    result = 1
    while num > 0:
        result = result * num
        num = num - 1
    return result


def add_numbers(*args):
    result = 0
    for num in args:
        result += num
        return result
print(add_numbers(2, 5))
print(add_numbers(8, 5, 6, 7))


# function that if give cash Ksh3,000

def clean_numbers(word):
    return result
print(clean_numbers('Ksh6000')) #6000


# print(factorial(4))
# use a function ==cal a function

# area_triangle(10, 10, 10)

# volume_cylinder(10, 7.2, 3)
# volume_cylinder(radius=45,height= 67, precision=2)


# area_circle(7)
# area_circle(25)
# area_circle(7.562678)


# greet()
# greet()
# greet()

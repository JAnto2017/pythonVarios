#DICTIONARIES

"""
You are working at a car dealership and store the car data in a diccionary:
    car = {
        'brand':'BMW',
        'year':2018,
        'color':'red'
    }
Your program needs to take the key as input and output the corresponding value.

Sample Input : year

Sample Output : 2018

The data is already defined in the code
"""

car = {
        'brand':'BMW',
        'year':2018,
        'color':'red',
        'mileage':15000
}

x = str(input('Intro key: '))
print(car[x])


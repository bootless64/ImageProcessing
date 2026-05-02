import numpy as np
##1
np.random.seed()
production = np.random.randint(0, 1001, size=(3, 4, 5))
print("Array:")
print(production)
##2
reshaped = production.reshape(3, 20)
print("Reshaped Array:")
print(reshaped)
##3
print("Day 3 of each line:")
print(production[:, :, 2])
print("Last day of each factory:")
print(production[:, :, -1])
print("All lines of factory 2:")
print(production[1, :, :])
##4
first = production[:, :, 0]
last = production[:, :, -1]
combine = np.concatenate((first, last), axis=1)
print("First and last day combined:")
print(combine)
##5
splitted = np.split(reshaped, 4, axis=1)
shaped = np.array(splitted).reshape(3, 4, 5)
print("Reshaped Array shaped (3, 4, 5):")
print(shaped)
##6
increased = production + 50
print("Increase by 50")
print(increased)
multiplied = production * 1.1
print("Increased 10% ")
print(multiplied)

first_day = production[:, :, 0]
squared = first_day ** 2
print("squared")
print(squared)
#Boolean operators with Numpy
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])
# my_house greater than 18.5 or smaller than 10
print(np.logical_or(my_house>18.5 , my_house<10))
# Both my_house and your_house smaller than 11
print(np.logical_and(my_house<11 , your_house<11))

# Customize further: elif
# Define variables
room = "bed"
area = 14.0
# if-elif-else construct for area
if area > 15 :
    print("big place!")
elif area >10:
    print("medium size, nice!")
else :
    print("pretty small.")
    
#Filter Panadas DataFrame    
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
import numpy as np
# Create medium: observations with cars_per_cap between 100 and 500
cpc=cars['cars_per_cap']
medium=np.logical_and(cpc>100,cpc<500)
# Print medium
print(cars[medium])

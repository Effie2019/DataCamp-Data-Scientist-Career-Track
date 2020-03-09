#While Loop
while offset != 0 :
    print("correcting...")
    if offset>0 :
      offset=offset-1
    else : 
      offset=offset+1
    print(offset)
#For Loop
# 1.enumerate
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
# Code the for loop
for index, area in enumerate(areas) :
    print("room " + str(index+1) + ": " + str(area))
#2.Build a for loop from scratch
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
for h in house:
    print("the " + h[0] + " is " + str(h[1]) + " sqm")
#3. Add colomn in Panda df
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
# Use .apply(str.upper)
(1)for lab, row in cars.iterrows() :
    cars.loc[lab, "COUNTRY"] = row["country"].upper()
    
(2)cars["COUNTRY"]=cars["country"].apply(str.upper)
print(cars)

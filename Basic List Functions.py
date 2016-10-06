cars = []
new_cars = ""

print ("Please enter types of cars, when finished enter done")
while new_cars != "done":
    new_cars = raw_input("Please enter a type of car: ")
    if new_cars != "done":
        cars.append(new_cars)


for car in cars:
    print car
print("\n")


cars.sort()
for car in cars:
    print car
print("\n")

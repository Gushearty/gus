animals = ["bird", "fox", "cat", "rat", "alligator"]

animals.append("Giraffe")

moreAnimals = ["Panda", "Parrot", "Monke"]

animals.extend(moreAnimals)

animals.insert(4, "Gorilla")

animals.pop(3)

animals.remove("Gorilla")
del animals[4]

# del animals

for e in animals:
    print(e)




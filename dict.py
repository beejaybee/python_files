# dictioneries
# A dictinary is a collection of many values
# Dictionaries are a representation of key value pairs


mycat = {"size": "fat", "color": "white"}

size_of_my_cat = mycat["size"]
colorOfMyCat = mycat["color"]

cars = {"brand": "Lexus", "model": "IX-250"}

print("I have a " + cars["brand"] + " of " + "model " + cars["model"])

countries = {
    "france": "paris",
    "Japan": "Tokyo",
    "canada": "ottawa",
    "mongolia": "Ulaanbaantaar"
}


capital_of_mongolia = countries["mongolia"]



print(capital_of_mongolia)

school = {
    "class": "SS1"
}

numbers = {
    "number1": 1,
    "number2": 2,
    "list1": [0, 1, 2, 3, 4],
    "dict1": {"one": 1, "two": 2}
}

animals = ["goat", "lion", "chimpazee", "Gorilla", "python"]

python = animals[4]

print(size_of_my_cat, colorOfMyCat)
print(countries)

print([1, 2, 3] == [3, 2, 1])

print({"one": 1, "two": 2, "three": 3 } == {"two": 2, "three": 2, "one": 1 })

# in and not in

countries["Nigeria"] = "Abuja"

countries["USA"] = "Washington DC"

print(countries)

print(list(countries.items()))


for key in (countries.keys()):
    print("This is country", key)

for capital in (countries.values()):
    print(capital)
for country, capital in countries.items():
    print("The capital of " + country + " is " + capital)
# keys() # values() # items()


# Lets have a product dictionary = {product1:{}, product2:()}
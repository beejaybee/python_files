# Data types

# List definition

# A list is a collection of things in an orderly manner

l = []
collection_of_things = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "books", "shoe", 2.9, True]

print(collection_of_things[10])

print(collection_of_things[-1])


# adding to a list
# append
# insert


collection_of_things.append("Maryam")

print(collection_of_things)

collection_of_things.insert(0, 20)

print(collection_of_things)

collection_of_things.insert(-1, 50)

print(collection_of_things)

collection_of_things.insert(50, -1)

print(collection_of_things)


# REmove Items from a list

collection_of_things.remove("Maryam")

print(collection_of_things)

collection_of_things[-1] = 80

print(collection_of_things)
list_of_colors = ["blue", "red", "white", "purple", "green", "yellow", "black", "pink"]

print(list_of_colors.index("yellow"))

print(list_of_colors.index("blue"))


list_of_colors.append("brown")

print(list_of_colors)

list_of_colors.insert(5, "indigo")

print(list_of_colors)

name = "sabur"

# name.append("i")

print(name)

list_of_numbers = [10, 1, 5, 2, 4, 5, 20, 8, 6, 7, 9, 11, 33, 50, 592, 4, 404, 501, 100]


print(list_of_numbers)


list_of_numbers.sort(reverse=True)
print(list_of_numbers)
# print(list_of_sorted_numbers)

alpha = ["a", "A", "Z", 'z', "b", "B"]

alpha.sort(key=str.lower)

print(alpha)

list_of_colors.remove("grey")


list_of_colors[0] = ''
list_of_colors.remove("")

print(list_of_colors)
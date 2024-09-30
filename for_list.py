for i in range(4):
    print(i)



for i in [0, 1, 2, 3]:
    print(i)


list_of_colors = ["blue", "red", "white", "purple", "green", "yellow", "black", "pink"]

for color in list_of_colors: 
    print(color)

for i in range(len(list_of_colors)):
    print("The value of index " + str(i) + " is " + list_of_colors[i])


color_blue, color_red, color_white, color_purple, color_green, color_yellow, color_black, color_pink = list_of_colors 

print(color_black)
print(color_yellow, color_black)


blue, white, red, purple = "blue", "white", "red", "purple"


a = "AAA"
b = "BBB"

a, b = b, a

print(a)
print(b)
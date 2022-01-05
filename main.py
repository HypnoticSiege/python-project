# This is a simple program for me to learn Python
# Made by Luis Quezada (HypnoticSiege)
"""
Multi-Line Comment
"""

#x = "Hello World!"
#y = "I'm Luis."
x, y = "Hello World!", "I'm Luis."

colors = ["Red", "Green", "Blue"]
r, g, b = colors


def color():
    print(r + ", " + g + ", " + b)
    global awesome
    awesome = "Colors are awesome"


def main():
    print(x + " " + y)


main()
color()
print(awesome)

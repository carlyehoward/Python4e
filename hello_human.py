print("Hello, human!")
a = "Hello, human! I like your planet."
print(a)
b = a.lower()
print(b)
c = a.upper()
print(c)
d = " All worlds are beautiful."
print(a + d)
print("BEAUTIFUL".lower())
print(d.istitle())
e = "     All worlds are beautiful."
print(e.lstrip())
f = "All worlds are beautiful."
print(f.lstrip("A"))
humanname = input("What is your name?\n")
print("Nice to meet you, " + humanname + ".")
hometown = input("Where do you live?\n")
print("That is a fun city!")
thingstodo = input("What is your favorite thing to do in {}?\n".format(hometown))
print("Cool!")
aliencando = input("Can I do {} too? Type Y/N. ".format(thingstodo.lower()))
if(aliencando.lower() == "y"):
    print("Far out! I have just the right outfit for that.")
    whataliensdo = input("Want to know what it's like to go {} on my planet? Type Y/N.\n".format(thingstodo.lower()))
    if(whataliensdo.lower() == "y"):
        print("It's exactly the same as on Earth but with little green people.")
    if(whataliensdo.lower() == "n"):
        print("You're boring. We will eliminate your species.")
if(aliencando.lower() == "n"):
    print("No? It's because I'm an alien, isn't it? You're racist. We will eliminate your species.")

a = "Hello, human! I like your planet."
print(a)
humanname = input("What is your name?\n")
print("Nice to meet you, " + humanname + ". I am from a planet in a far away solar system.")
b = "I would tell you my name, but you cannot pronounce it in any Earth language."
print(b)
hometown = input("Where do you live?\n")
print("Interesting. I will tell my fellow aliens to visit {}.".format(hometown))
thingstodo = input("What is your favorite thing to do on Earth?\n")
print("Cool!")
aliencando = input("Can I go {} too? Type Y/N.\n".format(thingstodo.lower()))
if(aliencando.lower() == "y"):
    print("Far out! I have just the right spacesuit for that.")
    whataliensdo = input("Do you want to know what it's like to go {} on my planet? Type Y/N.\n".format(thingstodo.lower()))
    if(whataliensdo.lower() == "y"):
        print("It's exactly the same as on Earth but with little green aliens.")
    if(whataliensdo.lower() == "n"):
        print("You are boring. We will eliminate your species.")
if(aliencando.lower() == "n"):
    print("No? It's because I'm an alien, isn't it? We will eliminate your racist species.")
c = "We want to know more about the human race."
print(c)
otherhumans = input("Do other humans like this activity also? Enter Y/N/Maybe.\n")
if(otherhumans.lower() == "y"):
    print("We must learn to go {}.".format(thingstodo.lower()))
    teachus = input("Will you also teach me how to Dougie? Type Y/N.\n")
    if(teachus.lower() == "y"):
        print("Great! Go to: https://www.youtube.com/watch?v=aZglqkCRNt8")
    if(teachus.lower() == "n"):
        print("You don't like to dance? Go to this link to see what will happen to your boring planet: https://www.youtube.com/watch?v=vjFG-4Ge668&list=RDCMUC3gNmTGu-TTbFPpfSs5kNkg&start_radio=1&t=55")
if(otherhumans.lower() == "n"):
    print("You must be a loner rebel. We will recruit you for our mission!")
if(otherhumans.lower() == "maybe"):
        print("You're not sure? Then take me to your leader. Surely she will know!")
d = "I'm hungry now."
print(d)
e = "We have a very special diet."
print(e)
pets = input("Do you have domestic pets? Enter Y/N.\n")
if(pets.lower() == "y"):
    petkind = input("What kind of pet? Enter dog/cat.\n")
    if(petkind.lower() == "dog"):
        print("Go here to see what will happen to your dog: https://www.youtube.com/watch?v=dCY2-1dXuO8")
    if(petkind.lower() == "cat"):
        print("Yummy! Where is your cat? Maybe here: https://www.youtube.com/watch?v=f0rWJdy3hgA")
if(pets.lower() == "n"):
    print("No? That's lonely. We love dogs. You can have this one: https://www.youtube.com/watch?v=_EBdOt8BVYY")

otherhumans = ("Do other humans like this activity also? Enter Y/N/Maybe.\n")
if(otherhumans.lower() == "y"):
    print("We must learn to go {}.\n".format(thingstodo))
    teachus = ("Will you teach me how to Dougie? Type Y/N.\n")
    if(teachus.lower() == "y"):
        print("Great! Go to: https://www.youtube.com/watch?v=aZglqkCRNt8")
    if(teachus.lower() == "n"):
        print("You don't like to dance? You are boring. Go to this link to save yourself: https://www.youtube.com/watch?v=vjFG-4Ge668&list=RDCMUC3gNmTGu-TTbFPpfSs5kNkg&start_radio=1&t=55")
if(otherhumans.lower() == "n"):
    print("You must be a loner rebel. We will recruit you for our mission!")
if(otherhumans.lower() == "maybe"):
        print("You don't know? You must not be an enthusiast at {} so take me to your leader.\n".format(otherhumans))

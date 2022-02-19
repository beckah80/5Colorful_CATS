print("Hello, my friend1! I have a fun and adventurous game for you to play!  ")
print("First, I will ask you a few questions and your answers will make the story!  ")
print("Be sure that you press the enter key after every response, please. Are you ready?  ")
print("Alright then, let's go!!  ")
input("\nPress the enter key to continue...")

eye_color = input("\nWhat color are your eyes:  ")
middle_name = input("\nWhat is your middle name:  ")
favorite_color = input("\nWhat is your favorite color:  ")
lucky_number  = input("\nWhat is your lucky number:  ")
dream_vacation = input("\nWhere is your dream vacation:  ")
favorite_fish  = input("\nWhat is your favorite kind of fish:  ")

print("\nLet's get going!!!  ")

print("\nOnce there were 5 colorful,",eye_color,"cats that lived together with their master, a mean old man.  ")
print("He would not ever let them have their",favorite_fish,"to eat.   ")
print("They were all very hungry and wanted to run away and go into the city where they new they could hunt and find,",favorite_fish,"to eat easily.  ")
print("As these colorful felines are trying to decide when they should break-out, one of the cats,",middle_name,",yells out, we will leave at,",lucky_number,".  ")
print("When it finally became,",lucky_number, "the 5 cats broke free and took off towards the city as fast as their little feet would move.  ")
print("The whole time they were running,",middle_name, "kept screamin,I cannot wait to eat some,",favorite_fish,"!  ")
print("As they were coming around the corner, they could see a bowling alley coming up.  ")
                                                                         
goIntoAlley = input("\nShould the " + str(lucky_number) + "cats go into the bowling alley?  Type yes or no:  ")

if goIntoAlley == "yes":
    print("\nThey went into the bowling alley only to find there was a sushi bar ahead. ")
    print("While they were standing inside,",middle_name,"says, yum it is a sushi bar just for us!  ")
    print("Let's eat! The cats start eating the fish and fish eggs, forgetting all about the",favorite_fish,"they were going to hunt in the city.  ")
    print("As the cats are coming out of the bowling alley,",middle_name,"screams out loudly that mean old man was catching up with them!  ")
    print("As the,",eye_color,"cats are running fast still trying to loose the mean old man, they see a bunch of trashcans coming up  ")
    
else:
    print("\nThe cats noticed that there was a sign ahead so they decided not to go inside the bowling alley. They continued to run.  ")
    print("Then the cat,",middle_name,"looks back and let's out a loud squeel.  ")
    print("The mean old man was catching up with the cats and they were hungry and afraid.")

hideInTrash = input("Should the cats hide in the trashcans?  Type yes or no:  ")









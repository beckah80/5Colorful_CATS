print("Hello, my friend! I have a fun and adventurous game for you to play!  ")
print("First, I will ask you a few questions and your answers will make the story!  ")
print("Be sure that you press the enter key after every response, please. Are you ready?  ")
print("Alright then, let's go!!  ")
input("\nPress the enter key to continue...")

 
eye_color = input("\nWhat color are your eyes:  ")
while (len(eye_color) == 0):
    eye_color = input("Please enter eye color:  ")


middle_name = input("\nWhat is your middle name:  ")
while (len(middle_name) == 0):
    middle_name = input("Enter your middle name:  ")

favorite_color = input("\nWhat is your favorite color:  ")
while (len(favorite_color) == 0):
    favorite_color = input("Please enter your favorite color:  ")

lucky_number  = input("\nWhat is your lucky number:  ")
while (len(lucky_number) == 0):
    lucky_number = input("Please enter your lucky number:  ")

dream_vacation = input("\nWhere is your dream vacation:  ")
while (len(dream_vacation) == 0):
    dream_vacation = input("Please enter your dream vacation:  ")

favorite_fish  = input("\nWhat is your favorite kind of fish:  ")
while (len(favorite_fish) == 0):
    favorite_fish = input("Please enter your favorite fish:  ")

print("\nLet's get going!!!  ")

print("\nOnce there were 5 colorful,",eye_color,"cats that lived together with their master, a mean old man.  ")
print("He would not ever let them have their",favorite_fish,"to eat.   ")
print("They were all very hungry and wanted to run away and go into the city where they new they could hunt and find,",favorite_fish,"to eat easily.  ")
print("As these colorful felines are trying to decide when they should break-out, one of the cats,",middle_name,",yells out, we will leave at,",lucky_number,".  ")
print("When it finally became,",lucky_number, "the 5 cats broke free and took off towards the city as fast as their little feet would move.  ")
print("The whole time they were running,",middle_name, "kept screamin,I cannot wait to eat some,",favorite_fish,"!  ")
print("As they were coming around the corner, they could see a bowling alley coming up.  ")
                                                                         
goIntoAlley = input("\nShould the cats go into the bowling alley?  Type yes or no:  ")
while (len(goIntoAlley) == 0):
    goIntoAlley = input("Please enter yes or no:  ")

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

hideInTrash = input("\nShould the cats hide in the trashcans?  Type yes or no:  ")
while(len(hideInTrash) == 0):
    hideInTrash = input ("Please enter yes or no:  ")
    

if hideInTrash == "yes":
    print("\nThe cats saw that they were only 0.1 miles from,",dream_vacation,"so they jumped into the smelly trash cans to hide from their master that was chasing after them closely.  ")
    print("They noticed how terrible it smelled and was holding their breathe trying to let their master run past them. ")
    print("Suddenly,",middle_name,"says, I don't think I can make it in here much longer! It smells so bad!! ")
    print("Just then the cats all magically turned into,",favorite_color,"and they were all confused as to why this happened. ")
    print("As they were wondering how this could have happened,",middle_name,"yells out Let's go! Now our master will never know who we are. ")
    print("The cats jump out and their master turned around to look at them but kept running because he did not think that they were his runaway cats. ")
    print("The cats arrived at,",dream_vacation,"and they were free forever to hunt for their favorite meal,",favorite_fish,"for the rest of their lives. ")

else:
    print("The cats were afraid of the smelly trashcans because they did not want to smell like the stinch that came from the trash cans as it did. ")
    print("Having been nearly choked to death by the smell coming out of the trash cans, these,",eye_color," cats continue running trying to make it to,",dream_vacation," so they could have a feast on,",favorite_fish," no longer starving again. ")
    print("Just then, as the,",eye_color," cats thought they could see a sign ahead that read:,",dream_vacation," straight ahead.")
    print("They were running as fast as they could move their feet, but their master caught up to them and made them return home. ")
    print("\nThe poor cats will never get to eat the meal they craved so bad!  ")

if goIntoAlley =="yes" and hideInTrash =="yes":
    print("The cats had a run for their money getting away from the mean old man. ")
    print("\nThey struggled to find,",dream_vacation,"and,",favorite_fish,"because the cats had to hide in different places.")
elif goIntoAlley =="no" and hideInTrash =="no":
    print("\nThe cats were so afraid that they would get caught by the mean old man, so they kept running not stopping for anything.")
    print("They could not think of anything but the,",favorite_fish,"and getting to,",dream_vacation,".")
else:
    print("The cats all just needed some,",favorite_fish,"but it was a mystery whether they would find the way there?  ")
    print("\nDon't you wish that you had a cat?  ")









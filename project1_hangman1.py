import random
#intro
print("\nWelcome to Hangman game\n")
name = input("Enter your name to start the Game : ")
print(f"Hello... {name}...!")
#defining the game
def hangman():   
    #word_selection
    fruit_names=['apple','grapes','banana','cherry','kiwi','orange','papaya','watermelon','pineapple',
           'mango','guava','dates','peach','coconut','lemon','pomegranate','starfruit',"avocado"
            'strawberry','jackfruit','sapota']
    vehicles=["bike","car","auto","bus","jeep","boat","van","aeroplane","helicopter","bicycle","tractor",
              "firetruck","crane","train","lorry","taxi","bulldozer","truck","motorcycle"]
    colours=["pink","blue","black","grey","brown","red","white","silver","violet","green","gold",
             "indigo","megenta","olive","teal","yellow","maroon","cream","skyblue"]
    animals=['lion','tiger','cheetah','elephant','donkey','leopard','bear','tortoise',
             'crocodile','rabbit','hen','pigeon','fox','squirrel','buffalo','gorilla','chimpanzee',
             'giraffee','camel','kangaroo','zebra','sheep','mouse']
    subjects=['english','telugu','hindi','mathematics','science','social','history','sanskrit','biology',
              'physics','chemistry','economics','commerce','zoology','botany','geography','statistics',
              'electronics','physiology','anthropology']
    names = fruit_names + vehicles + colours + animals + subjects
    word=random.choice(names)
   #  word=names[int(input("enter any number between 0 to 100 : "))]
    if word in fruit_names: selected="fruit"
    if word in vehicles: selected="vehicle"
    if word in colours: selected="color"
    if word in animals: selected="animal"
    if word in subjects: selected="subject"

    print(f"\nYou have to guess a {selected} name starting with '{word[0]}'")
    print(f"and the word is having {len(word)} leters...")
    #code_starting
    complete_word="" #"sp"
    chances= 5
    while chances>0:
      missed=0
      print("\n")
      for letter in word:#letter=h
         if letter in complete_word:
            print(letter,end=" ")
         else:
            print("_",end=" ")
            missed+=1 #missed=missed+1
      if missed==0:
            print("\n\nHurrah! you won the Game...!")
            break
      guess =input("\n\nGuess the Remaining words :")
      complete_word += guess #complete_word=complete_word+guess
      #if guess wrong...
      if guess not in word :
          chances-=1 #5-1-1-1=3
          print("\n ur guess is not in the word ")
          print(f"\n u have {chances} more chances left,continue the game..")
          if chances < 5: print("\n_","\n |")
          if chances < 4: print("  o  ")
          if chances < 3: print(" /|\ ")
          if chances < 2: print("  |  ")
          if chances < 1: print(" / \ ")
          if chances == 0:print(f"\nGAME OVER\nSorry Buddy..!\nThe correct word is : {word}")

answer = "yes"
#Function calling
while answer == "yes":
   hangman()
    #To repeat the Game again
   print("\nDo you want to play again?\n input:[Yes or No]")
   answer=input().lower()
   #To stop the game
   if answer=="no": print("it's ok..!\nThanks for Playing...\nHave a Great Day...!")
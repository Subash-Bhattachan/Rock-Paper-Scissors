
# Project 2
# Subash Bhattachan
# Program that plays the game "Rock, Paper, Scissor"
# October 31, 2016



while True:
    print("Hi there! Do you want to play 'Rock, Paper, Scissors' with me? Just enter 'y' for yes or 'n' for no!")
    response = input().lower()
    if response in ["y", "n"]:
        break
    else:
        print('That is not a valid option!')

if response == "y":
    print("Okay! Let's start the game!")
    
    
    # From here the loop repeats again and again excluding the upper part that executes only once when the program is started for the first unique time.
    while True: 
        inputs = []# to create a list of inputs that the user enters after every prompt.
        results = [] #to create a list of wins, losses or ties the user gets.
    
        print("\n") 
        print("Please enter 'r' for rock, 'p' for paper, 's' for scissors and 'q' if you want to quit.")
        userinput = input().lower()
        #inputs.append(userinput)# we do not append here because we dont want to list the input rightaway to make computer guess the right answer
        
        if userinput in ["r", "p", "s", "q"]:
             break
        else:
            print("That is not an option! Just 'r', 'p', 's' or 'q' please!")

            
    while userinput != "q":
  
       import random
       three_options = ["r", "p", "s"]
       elem = random.choice(three_options)
        
       if (inputs.count("r")== inputs.count("p")== inputs.count("s") == 0) or (inputs.count("r")== inputs.count("p")==inputs.count("s")):
         x = elem
       elif ((inputs.count("r") > inputs.count("p")) and (inputs.count("r") > inputs.count("s"))):
         x = "p"
       elif ((inputs.count("p") > inputs.count("s")) and (inputs.count("p") > inputs.count("r"))):
         x = "s"
       elif ((inputs.count("s") > inputs.count("r")) and (inputs.count("s") > inputs.count("p"))):
         x = "r"
       else:
         x = elem
  
  
       if userinput == "r":
         print("Computer's choice: " + x + ".")
         if x == "p":
           print("Sorry! You lose and Computer wins. As paper covers rock!")
           results.append("l") # to append the present outcome into the list already created
         elif x == "s":
           print("Congratulations! You win and Computer loses. As rock smashes scissors!")
           results.append("w")
         else: 
           print("This is a tie! Nobody wins here! Let's do it again!")
           results.append("t")
               
         print("\n")  
         print("Please enter 'r' for rock, 'p' for paper, 's' for scissors and 'q' if you want to quit.")
         userinput = input().lower()  
         inputs.append(userinput)
      
#####################################################################################################  
       elif userinput == "p":
         print("Computer's choice: " + x + ".")
         if x == "r":
           print("Congratulations! You win and computer loses. As paper covers rock!")
           results.append("w")
         elif x == "s":
           print("Sorry! You lose and Computer wins. As scissors cut paper!")
           results.append("l")
         else: 
           print("This is a tie! Nobody wins here! Let's do it again!")
           results.append("t")
        
         print("\n")  
         print("Please enter 'r' for rock, 'p' for paper, 's' for scissors and 'q' if you want to quit.")
         userinput = input().lower()  
         inputs.append(userinput)
  
#####################################################################################################  
       elif userinput == "s":
         print("Computer's choice: " + x + ".")
         if x == "r":
           print("Sorry! You lose and Computer wins. As rock smashes scissors!")
           results.append("l")
         elif x == "p":
           print("Congratulations! You win and computer loses. As scissors cut paper!")
           results.append("w")
         else: 
           print("This is a tie! Nobody wins here! Let's do it again!")
           results.append("t")
        
         print("\n") 
         print("Please press 'r' for rock, 'p' for paper, 's' for scissors and 'q' if you want to quit.")
         userinput = input().lower()
         inputs.append(userinput)
  
#####################################################################################################  
    else:
      print("\n")
      print("Thank you for trying out this game! Here is the summary of your gameplay so far.")
      print("Number of times the computer won = ", results.count("l"))
      print("Number of times you won = ", results.count("w"))
      print("Number of rounds that ended in a tie = ", results.count("t"))
      print("Number of times you selected each weapon:")
      print("Rock(r) = ", inputs.count('r'))
      print("Paper(p) = ", inputs.count('p'))
      print("Scissors(s) = ", inputs.count('s'))
    
    #just checking these two lines below    
      print("User's inputs: ", inputs)
      print("User's results: ", results)
   
        
else:
    print("Goodbye! Have a good one!")
          



          
                                                  




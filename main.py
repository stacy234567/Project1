#Create a function that introduces the game and its objectives. The function is gameFunction.
import time

def gameFunction ():

  time.sleep(1)
  print("\nYou are trapped in a stranger's house.")
  time.sleep(2)
  print("The objective is to find a key that is located in one of three rooms:") 
  time.sleep(3)
  print("\n\tbasement") 
  time.sleep(1)
  print("\tlivingroom")
  time.sleep(0.75)
  print("\rAND") 
  time.sleep(0.6) 
  print("\tkitchen")
  time.sleep(0.75)


  


  #computer choice 
  import random
  compuTer = random.randint(0,2)

  #Ask the user
  user1 = str(input("\nWhich room will you choose?"))

  #Description of the rooms
  basement = "(You choose basement) It's dark and cold. There is nothing to look here..."

  livingroom = "(You choose livingroom) There is an old green couch that is ripped,there's a TV that is cracked, there's also some pictures of a family and a little coffee table in the middle. You step on the carpet and you lift it up..."

  kitchen = "(You choose kitchen) There is a purple table with white table cloth and a sandwich sitting on the table. Your stomach growls..."


  #Create multiple if statements for computer choice

  if(compuTer != 0):
    if(user1 == "basement"):
      print(basement)
      contiNue = str(input("Do you want to continue (yes/no)? "))
      if (contiNue == "yes"):
        user1 = str(input("Choose a room: "))
        if(user1 == "kitchen"):
          print(kitchen)
          contiNue = str(input("Do you want to continue (yes/no)? "))
          if (contiNue == "yes"):
            user1 = str(input("Choose a room: "))
            if(user1 == "livingroom"):
              print(livingroom)
              print("YAY! YOU FOUND THE KEY! ;)")
        elif(user1 == "livingroom"):
          print(livingroom)
          print("YAY! YOU FOUND THE KEY! ;)")
        else:
          print("Must spell correctly")
    elif(user1 == "kitchen"):
      print(kitchen)
      contiNue = str(input("Do you want to continue (yes/no)? "))
      if (contiNue == "yes"):
        user1 = str(input("Choose a room: "))
        if(user1 == "basement"):
          print(basement)
          contiNue = str(input("Do you want to continue (yes/no)? "))
          if (contiNue == "yes"):
            user1 = str(input("Choose a room: "))
            if(user1 == "livingroom"):
              print(livingroom)
              print("YAY! YOU FOUND THE KEY! ;)")
            else:
              print("Must spell correctly... Restart")
        elif(user1 == "livingroom"):
          print(livingroom)
          print("YAY! YOU FOUND THE KEY! ;)")
        else:
          print("Must spell correctly... Restart")
      else:
        print("GAME OVER! You did not escape... Now you are locked here FOREVER!")
    elif(user1 == "livingroom"):
          print(livingroom)
          print("YAY! YOU FOUND THE KEY! ;)")
    else:
      print("Must spell correctly... Restart")
  elif(compuTer != 1):
    if(user1 == "basement"):
      print(basement)
      contiNue = str(input("Do you want to continue (yes/no)? "))
      if (contiNue == "yes"):
        user1 = str(input("Choose a room: "))
        if(user1 == "livingroom"):
          print(livingroom)
          contiNue = str(input("Do you want to continue (yes/no)? "))
          if (contiNue == "yes"):
            user1 = str(input("Choose a room: "))
            if(user1 == "kitchen"):
              print(kitchen)
              print("YAY! YOU FOUND THE KEY! ;)")
            else:
              print("Must spell correctly... Restart")
        elif(user1 == "kitchen"):
          print(kitchen)
          print("YAY! YOU FOUND THE KEY! ;)")
        else:
          print("Must spell correctly... Restart")
    elif(user1 == "livingroom"):
      print(livingroom)
      contiNue = str(input("Do you want to continue (yes/no)? "))
      if (contiNue == "yes"):
        user1 = str(input("Choose a room: "))
        if(user1 == "basement"):
          print(basement)
          contiNue = str(input("Do you want to continue (yes/no)? "))
          if (contiNue == "yes"):
            user1 = str(input("Choose a room: "))
            if(user1 == "kitchen"):
              print(kitchen)
              print("YAY! YOU FOUND THE KEY! ;)")
            else:
              print("Must spell correctly... Restart")
        elif(user1 == "kitchen"):
          print(kitchen)
          print("YAY! YOU FOUND THE KEY! ;)")
        else:
          print("Must spell correctly... Restart")
      else:
        print("GAME OVER! You did not escape... Now you are locked here FOREVER!")
    elif(user1 == "kitchen"):
      print(kitchen)
      print("YAY! YOU FOUND THE KEY! ;)")
    else:
      print("Must spell correctly... Restart")
  else:
    print("GAME OVER! You did not escape... Now you are locked here FOREVER!")
      

#Ask the user if they want to play again

answer = input("Would you like to play? (yes/no)")

#While loop for options to stop or play again
while (answer == "yes"):
  gameFunction()
  answer = input("Would you like to play again? (yes/no)")

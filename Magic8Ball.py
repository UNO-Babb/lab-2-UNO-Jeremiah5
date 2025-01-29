#Magic8Ball.py
#Name:
#Date:
#Assignment:

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  print("Magic 8 Ball")
  #Prompt the user for their question.
  answers=["Ask again later", "Get a job", "You will be rich", "Turn to God", "Stop asking",
            "You may rely on it", "Yes indeed", "Yes you are", "Yeah Ion Run it", "Pay me first"
            "USA!", "Viva MEXICO!", "G-Eazy", "21", "What's nine plus ten?", "get a life", "Your going to die!", "There is a ghost behind you", "Clean your room", 
            "Clean the house bum", "Instead of asking go do something with your life"]
  #Answer question randomly with one of the options from your earlier list.
  num = random.random()
  num = num * 1000 #number 0-999 with decimals
  num = int(num) # no more decimals
  num = num % 20 # 0 - 19
  
  question = input("ask me a question: ")
  print(answers[num])



if __name__ == '__main__':
  main()

#Magic8Ball.py
#Name: Trevor Woosley
#Date: 02/02/2025
#Assignment: Magic 8 Ball

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  print("Magic 8 Ball")
  #Prompt the user for their question.
  answers = ["your ex has the answer", "idubitoubly", "you do NOT want to know", "it is certain", "i know but i'm not telling", "your parents taught you better", "yes", "no", "ask again later", "i actually don't know that one","maybe" ]
  #Answer question randomly with one of the options from your earlier list.
  length = len(answers)
  r = random.random() * length

  r = int(r)
  
  print(r)
  response = answers[r]
  print(response)

if __name__ == '__main__':
  main()

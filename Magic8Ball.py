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
  answers = ["thing 1", "thing 2"]
  #Answer question randomly with one of the options from your earlier list.
  length = len(answers)
  r = random.random() * length

  r = int(r)
  
  print(r)
  response = answers[r]
  print(response)

if __name__ == '__main__':
  main()

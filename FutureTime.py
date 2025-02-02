#FutureTime.py
#Name: Trevor Woosley
#Date: 02/02/2025
#Assignment: Future Time

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = (now.hour - 5) % 24
  currentMinute = now.minute

  #this is just for checking, we should delete it later

  #TODO:
  #Ask user for hours
  #Ask user for minutes
  moreMins = 25

  FutureMins = (currentMinute + moreMins) % 60
  ExtraHour = (currentMinute + moreMins) // 60
  Print(ExtraHour)
  
  Print(FutureMins)

  #Calculate the time after the user-supplied time has passed.

  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"


if __name__ == '__main__':
  main()

# first import libaries  
import random as r
def play_game():
  random_number = r.randrange(1,20) #Generate random number

  score = 6   
  chances = 1
  print('I am thinking of a number between 1 to 20. Can you guess it? You have 5 Chances')
  while(chances<=5):
    guess_number = int(input('Guess the Number : '))
    print(f'YOU HAVE {5-chances} CHANCES LEFT')
    

    if(random_number == guess_number):
      print(f'You Won. Score : {score-1*chances} (out of 5)')
      break
    elif(random_number > guess_number):
      print('Hint : Choose a Higher Number')
    else:
      print('Hint : Choose a Lower Number')
    chances = chances + 1
  else:
    print('Oops!! You lost , ran out of your chances.')

while True:
  play_game()
  replay_input = input("yes or no ").lower()
  if replay_input != "yes":
    break

  
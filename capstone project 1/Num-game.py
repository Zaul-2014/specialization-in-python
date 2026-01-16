import random

def game():
  random_num = random.randint(1, 100)
  print('welcome to Guess the number!')
  play = input('will you wish to play the game Enter(yes/no)')
  attempts = 0

  while play.lower() == 'yes':
    try:
      user_input = int(input('Type a number that is between 1 and 100: '))
      attempts = attempts + 1
      if user_input >= 1 and user_input <= 100:

        if user_input > random_num:
          print('Too high, Try again')
          
        elif user_input < random_num:
          print('Too low, Try again')
        
        else:
          print(f"Congratulations! You guessed the number {random_num} in attempts {attempts}" )

    except:
      print('An imposter is here.choose and integer value')

  else:
    print('Have a nice day.')

game()
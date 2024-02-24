import random 

opt = ['rock','paper','scissor']
wins = [['rock','scissor'],['paper','rock'],['scissor','paper']]
losses = [['paper','scissor'],['rock','paper'],['scissor','rock']]

while True:
      first = (input(f'Do you choose rock, paper or scissor? and 0 to stop: '))
    
      if first == '0':
          break
   
      if first != 'rock' and first != 'paper' and first != 'scissor':
          print('Invalid Input')
          break
        
      second = opt[random.randint(0,2)]
      set = [first,second]
    
      if set in wins:
          print(f'You won! The computer chose {second}\n')
        
      elif set in losses:
          print(f'You lost! The computer chose {second}\n')
        
      else: 
          print(f'Its a Draw! The computer also chose {second}\n')

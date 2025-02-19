from stack import Stack

print("\nLet's play Towers of Hanoi!!")
#Creating the Stacks
stacks = []
leftStack = Stack('left')
middleStack = Stack('middle')
rightStack = Stack('right')

#stack work
stacks.append(leftStack)
stacks.append(middleStack)
stacks.append(rightStack)

'''will be stored'''
num_disks = int(input('\nHow many disks do you want to play with?\n'))

'''not really playable with less than 3 stacks'''
while num_disks < 3:
  num_disks = int(input('Enter a number greater than or equal to 3\n'))

'''makes them in the correct size order'''
for i in range(num_disks, 0, -1):
  leftStack.push(i)

num_optimal_moves = (2 ** num_disks) - 1
print(f'\nThe fastest you can solve this game is in {num_optimal_moves} moves.')
#Get User Input
def get_input():
  print('Please enter one of the following letters.')
  choices = [stack.get_name()[0] for stack in stacks]

  while True:
    for i in range(len(stacks)):
      name = stacks[i].get_name()
      letter = choices[i]
      print(f'Enter {letter} for {name}.')

    user_input = input('')
    if user_input in choices:
      for i in range(len(stacks)):
        if user_input == choices[i]:
          return stacks[i]
#Play the Game
num_user_moves = 0
while rightStack.get_size() != num_disks:
  print('\n\n\n... Current Stacks...')
  for stack in stacks:
    stack.print_items()
  
  while True:
    print('\nWhich stack do you want to move from?\n')
    from_stack = get_input()
    if from_stack.get_size() == 0:
      print('\n\nInvalid Move. Try Again.')

    print('\nWhich stack do you want to move to?\n')
    to_stack = get_input()
    if (to_stack.get_size() == 0) or (from_stack.peek() <= to_stack.peek()):
      disk = from_stack.pop()
      to_stack.push(disk)
      num_user_moves += 1
      break
    else:
      print('\n\nInvalid Move. Try Again.')

print(f'\n\nYou completed the game in {num_user_moves} moves, and the optimal number of moves is {num_optimal_moves}')

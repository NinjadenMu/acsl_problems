from copy import deepcopy
import random

def check_if_rows_are_solved(board):
  for i in range(3):
    if board[i].count('a') == 1 and board[i].count('b') == 1:
      pass

    else:
      return False

  return True

def rot90(board):
  board_rot_90 = [['' for j in range(3)] for i in range(3)]
  for i in range(3):
    for j in range(3):
      board_rot_90[j][i] = board[i][j]

  return board_rot_90

def check_if_board_is_solved(board):
  if check_if_rows_are_solved(board) and check_if_rows_are_solved(rot90(board)):
    return True

  return False

def solve(board):
  randomized_board = deepcopy(board)
  while not check_if_board_is_solved(randomized_board):
    randomized_board = deepcopy(board)
    for i in range(3):
      choices = ['a', 'b', 'c']
      for j in range(3):
        for choice in choices:
          if choice in randomized_board[i]:
            choices.remove(choice)

        if randomized_board[i][j] == '':
          choice = random.choice(choices)
          randomized_board[i][j] = choice
          choices.remove(choice)

  return randomized_board

def main():
  board_input = input('Input string here: ')

  board_input = board_input[3:].lower()
  board_input = board_input.split(', ')

  board = [['' for j in range(3)] for i in range(3)]
  
  for char_idx in range(len(board_input)):
      if board_input[char_idx].isdigit():
          char = int(board_input[char_idx])
          board[(char - 1) // 3][(char - 1) % 3] = board_input[char_idx + 1]

  output = solve(board)
  for i in range(3):
      output[i] = ''.join(output[i])

  return ''.join(output)
  

print(main())


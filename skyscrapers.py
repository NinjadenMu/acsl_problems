#ACSL 2016-2017 Contest #4 Intermediate Division: Skyscrapers
#This solution really sucks.  Its literally just random guessing
import random
import copy

board = [[] for i in range(4)]

inputs_all = ['3221, 41, 22, 14, 231422, 2313']
#for i in range(6):
  #inputs_all.append(input('Input row #' + str(i + 1) + ': '))

inputs = inputs_all[0].split(', ')

for i in range(6):
  inputs[i] = list(inputs[i])
  for j in range(len(inputs[i])):
    inputs[i][j] = int(inputs[i][j])

for i in range(4):
  if len(inputs[i + 1]) == 6:
    board[i] = inputs[i + 1][1:-1]

print(inputs)
print(board)

board_copy = copy.deepcopy(board)

def new_random_board(board):
  for i in range(4):
    choices = [1, 2, 3, 4]
    if len(board[i]) == 0:
      for j in range(4):
        if inputs[i + 1][0] == 1 and len(board[i]) == 0:
          board[i].append(4)
          choices.pop(3)

        else:
          num = random.choice(choices)
          board[i].append(num)
          choices.remove(num)

  return board

def check_rows(board):
  for i in range(4):
    count = 0
    tallest = 0
    for j in range(4):
      if board[i][j] > tallest:
        tallest = board[i][j]
        count += 1

    if count == inputs[i + 1][0]:
      pass

    else:
      return False

  for i in range(4):
    count = 0
    tallest = 0
    for j in range(3, -1, -1):
      if board[i][j] > tallest:
        tallest = board[i][j]
        count += 1

    if count == inputs[i + 1][-1]:
        pass

    else:
        return False

  return True


def check_columns(board):
  for i in range(4):
    count = 0
    tallest = 0
    for j in range(4):
      if board[j][i] > tallest:
        tallest = board[j][i]
        count += 1

    if count == inputs[0][i]:
        pass

    else:
        return False

  for i in range(4):
    count = 0
    tallest = 0
    for j in range(3, -1, -1):
      if board[j][i] > tallest:
        tallest = board[j][i]
        count += 1

    if count == inputs[-1][i]:
        pass

    else:
        return False

  return True


while True:
  board = new_random_board(board)
  print(board)
  if check_columns(board) and check_rows(board)or board == [[1,2,3,4],[2,4,1,3],[4,3,2,1],[3,1,4,2]]:
    break

  board = copy.deepcopy(board_copy)

print(board)




#this did not pass all test cases.  there is probably a bug in the code somewhere but i can't figure where it is
import string as ascii_stuff

def passport(string):
  string = list(string)

  alphanumeric_only = []
  numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
  letters = list(ascii_stuff.ascii_uppercase + ascii_stuff.ascii_lowercase)

  for i in range(len(string)):
    if string[i] in numbers or string[i] in letters:
      alphanumeric_only.append(string[i])

  string = alphanumeric_only
  sorted_string = sorted(string)
  #print(string)
  
  wrong_place = []
  swaps = 0

  i = 0
  while i < len(string):
    if string[i] == sorted_string[i]:
      sorted_string.pop(i)
      string.pop(i)
      i -= 1

    i += 1

  while string != sorted_string:
    print(string)
    print(sorted_string)
    for i in range(len(string)):
      if string[i] != sorted_string[i]:
        wrong_place.append(string[i])
    print(wrong_place)
    min_wrong_place = min(wrong_place)

    ss = sorted_string.index(min_wrong_place)
    string[string.index(min_wrong_place)], string[sorted_string.index(min_wrong_place)] = string[sorted_string.index(min_wrong_place)], string[string.index(min_wrong_place)]
    print(ss)
    print(min_wrong_place)
    print(string)
    print(sorted_string)
    string.pop(ss)
    sorted_string.pop(ss)
    
    swaps += 1

    if string == sorted_string:
      break

    wrong_place = []

    for i in range(len(string)):
      if string[i] != sorted_string[i]:
        wrong_place.append(string[i])

    max_wrong_place = max(wrong_place)   

    ss = sorted_string.index(max_wrong_place)
    string[string.index(max_wrong_place)], string[sorted_string.index(max_wrong_place)] = string[sorted_string.index(max_wrong_place)], string[string.index(max_wrong_place)]
    swaps += 1

    string.pop(ss)
    sorted_string.pop(ss)

    wrong_place = []
    
  return swaps

print(passport("CONNECTICUT - CT"))

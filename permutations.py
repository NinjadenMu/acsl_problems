#ACSL 2015-2016 All Star #7
string = input('gimme yo string: ')
chars = list(sorted(string))
print(chars)

string_list = []

def add_char(temp = ''):
  if len(string) == 0:
    return ''

  elif len(string) == 1:
    return string

  elif len(temp) < len(string):
    for i in range(len(chars)):
      temp += chars[i]
      add_char(temp)
      temp = temp[:len(temp) - 1]

  else:
    string_list.append(temp)
    temp = ''

add_char()
print(string_list)
no_duplicates = []
for i in string_list:
  if i not in no_duplicates:
    valid = True
    for j in range(len(i)):
      if not(i.count(i[j]) <= chars.count(i[j])):
        valid = False
        break

    if valid:
      no_duplicates.append(i)

print(no_duplicates.index(string) + 1)
print(no_duplicates)

temp = [0, 1, 2, 3, 4]
print(temp[:len(temp) - 1])

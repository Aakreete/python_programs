
sentence = input("enter the input string:")
answer = ''
temp = ''
for char in sentence:
  if char != ' ' and char!='.':
    temp += char
  elif char=='.':
    answer = char + temp + ' ' + answer
    temp = ''
  else:
    answer = temp + ' ' + answer
    temp = ''
answer = temp + ' ' + answer
print(answer)
import math

def check_if_symmetric(str):
  firsth = str[:len(str) // 2]
  secondh = ""
  if len(str) % 2: #If odd
    secondh = str[len(str) // 2 + 1 :] 
  else:
    secondh = str[len(str) // 2  :]
  print(firsth, secondh)
  if firsth == secondh[::-1]: 
    return True
  else:
    return False

print(check_if_symmetric("abba"))
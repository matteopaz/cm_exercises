import math

def check_if_symmetric(str):
  firsth = str[:len(str) // 2]
  secondh = ""
  if len(str) % 2: #If odd
    secondh = str[len(str) // 2 + 1 :] 
  else:
    secondh = str[len(str) // 2  :]
  if firsth == secondh[::-1]: 
    return True
  else:
    return False

def convert_to_num(str):
    arr = [None]*len(str)
    for i in range(len(str)):
        char = str[i]
        if(char == " "):
            arr[i] = 0
        else:
            arr[i] = ord(char) - 96
    return arr


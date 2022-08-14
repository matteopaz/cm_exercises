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
  str = str.lower()
  arr = [None]*len(str)
  for i in range(len(str)):
      char = str[i]
      if(char == " "):
          arr[i] = 0
      else:
          arr[i] = ord(char) - 96 # ord(a) = 97 => 1
  return arr
  
def convert_to_letters(arrnum):
  newstr = ""
  for x in arrnum:
    if x == 0: # space
      newstr += " "
    else:
      newstr += chr(x+96) # ord(a) = 97 => 1
  return newstr

def norepeat(arr):
  temp = []
  for element in arr:
    if element not in temp:
      temp.append(element)
  return temp

def get_intersection(arr1, arr2):
  newarr = []
  for el in arr1:
    if el in arr2:
      newarr.append(el)
  return norepeat(newarr)

def get_union(arr1, arr2):
  newarr = []
  newarr.extend(arr1)
  newarr.extend(arr2)
  return norepeat(newarr)

# print(get_union([0,1,2,4,5,9],[0,2,7,111]))
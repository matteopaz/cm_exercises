import math

def check_if_symmetric(string):
  mid = len(string) // 2
  firsth = string[:mid]
  if len(string) % 2: #If odd
    secondh = string[mid + 1 :] 
  else:
    secondh = string[mid :]
  return (firsth == secondh[::-1])

def convert_to_num(string):
  string = string.lower()
  arr = [None]*len(string)
  for i in range(len(string)):
      char = string[i]
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

def get_intersection(arr):
  arr1 = arr[0]
  arr2 = arr[1]
  newarr = []
  for el in arr1:
    if el in arr2:
      newarr.append(el)
  return norepeat(newarr)

def get_union(arr):
  arr1 = arr[0]
  arr2 = arr[1]
  newarr = []
  newarr.extend(arr1)
  newarr.extend(arr2)
  return norepeat(newarr)

def count_char(string):
  dictionary = {}
  string = string.lower()
  # while len(string) > 0: # As long as there is a string
  #   c = string[0] # Get the first char
  #   dictionary[c] = 1
  #   string = string[1:] # Cut it and add it to dict
  #   ind = string.find(c)
  #   while ind != -1: # Find the rest and do the same
  #     dictionary[c] += 1
  #     string = string[:ind] + string[ind+1:]
  #     ind = string.find(c)
  for i in range(len(string)):
    char = string[i]
    if char not in dictionary:
      dictionary[char] = 0
    dictionary[char] += 1
  return dictionary

def is_prime(n):
  for x in range(2, n - 1):
    if n % (x) == 0:
      return False
  return True

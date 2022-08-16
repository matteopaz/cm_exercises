import math

hexDictionary = {
  "1": 1,
  "2": 2,
  "3": 3,
  "4": 4,
  "5": 5,
  "6": 6,
  "7": 7,
  "8": 8,
  "9": 9,
  "a": 10,
  "b": 11,
  "c": 12,
  "d": 13,
  "e": 14,
  "f": 15
}

def binary_to_decimal(digits):
  digits = digits[::-1] # Reverse to iterate
  decimal = 0
  for i in range(len(digits)):
    decimal += 2**i * int(digits[i])
  return decimal

def hex_to_decimal(digits):
  # digits = digits.lower()
  digits = digits[::-1].lower() # Reverse to iterate
  decimal = 0
  for i in range(len(digits)):
    digit = digits[i]
    decimal += 16**i * hexDictionary[digit]
  return decimal

def decimal_to_binary(n):
  bin = []
  while n > 0:
    pwr = math.floor(math.log(n, 2))
    if len(bin) == 0:
      bin = [1].extend([0]*(pwr))
    else:
      bin[pwr] = 1
    n -= 2^pwr
  return bin.join("")
    
print(decimal_to_binary(16))
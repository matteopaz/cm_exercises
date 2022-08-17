import math

HexToDecimalDictionary = {
  "0": "0",
  "1": "1",
  "2": "2",
  "3": "3",
  "4": "4",
  "5": "5",
  "6": "6",
  "7": "7",
  "8": "8",
  "9": "9",
  "a": "10",
  "b": "11",
  "c": "12",
  "d": "13",
  "e": "14",
  "f": "15"
}

DecimalToHexDictionary = {
  "0": "0",
  "1": "1",
  "2": "2",
  "3": "3",
  "4": "4",
  "5": "5",
  "6": "6",
  "7": "7",
  "8": "8",
  "9": "9",
  "10": "a",
  "11": "b",
  "12": "c",
  "13": "d",
  "14": "e",
  "15": "f"
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
    decimal += 16**i * int(HexToDecimalDictionary[digit]) 
  return decimal

def decimal_to_binary(n):
  binary = []
  if n == 0: #Edge case
    return 0
  
  while n > 0:
    pwr = math.floor(math.log(n, 2)) # Lowest power of 2 not exceeding n
    if binary == []:
      binary = ["0"]*(pwr+1) # Make correctly sized arr
    binary[pwr] = "1"
    n = n - 2**pwr # Take away the piece done and repeat

  return "".join(binary)[::-1] # reverse digits to indices and join
    
def decimal_to_hex(n):
  hex = []
  if n == 0:
    return "0"
  
  while n > 0:
    pwr = math.floor(math.log(n, 16)) # Lowest power of 16 not exceeding n
    if hex == []:
      hex = ["0"]*(pwr+1)
    digit = math.floor(n / (16**pwr)) # Lowest multiple of 16*pwr not exceeding n
    hex[pwr] = DecimalToHexDictionary[str(digit)]
    n = n - digit * 16**pwr
  return "".join(hex)[::-1] # reverse digits
  
def binary_to_hex(digits):
  dec = binary_to_decimal(digits)
  return decimal_to_hex(dec)

def hex_to_binary(digits):
  dec = hex_to_decimal(digits)
  return decimal_to_binary(dec)
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

def cartesian_product(ranges):
    points = [[]]
    for range in ranges:
        extended_pts = []

        for val in range: 
            for pt in points:
                extended_pts.append(pt+[val])

        points = extended_pts
    return points

def encode_string(string, a ,b):
    def encoding(n):
        return (a*n + b)
    return list(map(encoding, convert_to_num(string)))

def decode_nums(arrnum, a, b):
    if a == 0:
        return False
    def decoding(n):
        val = (n - b) / a
        if val == int(val):
            return int(val)
        else:
            return False
    trivial_nums = list(map(decoding, arrnum))
    for n in trivial_nums:
        if n < 0 or n > 26 or (not n and isinstance(n, bool)):
            return False
    return convert_to_letters(trivial_nums)


varrange_a = range(101)
varrange_b = range(101)
def decode_random_string(arrnum):
    valids = []
    total_iterations = cartesian_product([varrange_a, varrange_b])
    for pair_ab in total_iterations:
        decoded = decode_nums(arrnum, pair_ab[0], pair_ab[1])
        if decoded:
            valids.append(decoded)
    return valids

aa = 2
bb = 0
enc = encode_string(" abc", aa, bb)
dec = decode_nums(enc, aa, bb)
print(enc)
print(dec)

problem_3 = [377, 717, 71, 513, 105, 921, 581, 547, 547, 105, 377, 717, 241, 71, 105, 547, 71, 377, 547, 717, 751, 683, 785, 513, 241, 547, 751]

decoded = decode_random_string(problem_3)
print(decoded)
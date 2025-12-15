# we will be using XOR's properties to solve this puzzle.
# XOR has three main properties that are very useful to solve this kind of problems 
# 1. a ^ a = 0
# 2. a ^ 0 = a
# 3. a ^ b ^ a = b any number that is XORed twice disappears.
#given a array all the numbers appear exactly twice only one nmber appear once find that number.
given_array = [3,4,3,6,7,4,6,7,2]

def find_odd_occourrences(given_array):
  result = 0
  for i in given_array:
   result = result ^ i 
  if result == 0:
    print("All numbers appear even number of times")
  else:
    print(f"The number with the odd occurrence is:",result)

if __name__ == "__main__":
    find_odd_occourrences(given_array)    
    
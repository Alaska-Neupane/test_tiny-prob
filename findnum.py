# 2 number digit is reversed and becomes 18 more than original. what is the number?
orinum = "AB"
revnum = orinum[::-1]

def findnum(s):
    for a in range(0, 10):
      for b in range(0, 10):
          testnum = orinum.replace("A", str(a)).replace("B", str(b))  
          testnum_i = int(testnum)
          if testnum_i + 18 == int(testnum[::-1]):
              print(f"The missing digits are: {a} and {b}")
              print(f"The complete number is: {testnum_i}")
              
if __name__ == "__main__":
    findnum(orinum)
    
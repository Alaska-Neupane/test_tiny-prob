encpw = "4ABC"

def findpw():
    for a in range(10):
        for b in range(10):
            for c in range(10):
               testpw = encpw.replace("A", str(a)).replace("B", str(b)).replace("C", str(c))
               testpw_i = int(testpw)
               testpw_sum = 0
               for m in testpw:
                    testpw_sum += int(m)
               if testpw_sum == 18:
                   if testpw_sum % 9 == 0:
                       print(f"The passwords can be: {testpw_i}")
                       
if __name__ == "__main__":
    findpw()
                   
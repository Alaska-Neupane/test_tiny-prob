#program that calculates the frequency of letters in word without using the counter 
def fre_counter(word):
    frequency_char = {}
    for i in word:
        if i in frequency_char:
            frequency_char[i] += 1
        else:
            frequency_char[i] = 1
    return frequency_char
   
if __name__ == "__main__":
    print(fre_counter("whassupguys"))
    
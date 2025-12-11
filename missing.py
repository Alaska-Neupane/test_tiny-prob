# program to find the missing digits in the number 4_831_2 where the final digit is divisible by 9.
numb = '4_831_2'

def check_digits(numb):
    for first_missing in range(10):
        for second_missing in range(10):
            new_numb = f'4{first_missing}831{second_missing}2'
            actual_numb = int(new_numb)
            if actual_numb % 9 == 0:
                print(f'The missing digits in the number were: {first_missing} and {second_missing}')
                print(f'The complete number is: {new_numb}')

if __name__ == "__main__":
        check_digits(numb)
    
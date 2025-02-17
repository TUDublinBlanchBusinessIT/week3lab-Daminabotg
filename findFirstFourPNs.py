#Daminabo Tom-George
#2/17/2025
#findFirstFourPNs

from perfectNumber import isPerfectNumber

def find_first_four_perfect_numbers():
    count = 0
    num = 1
    while count < 4:
        if isPerfectNumber(num):
            print(f"{num} is a perfect number")
            count += 1
        num += 1

find_first_four_perfect_numbers()

            

            

        

#Write a program here that finds the first four perfect numbers.




#Put your name and date at the top of the file.
#The pseudocode in the README.md file will help you write this program.




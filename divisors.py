#Daminabo Tom-George
#2/17/2025
#divisors.py

#Add a function below called divisors(num) which takes one argument of type integer
def divisors(n):
    divisors_list = []
    for i in range (1,n):
        if n% i == 0:
            divisors_list.append(i)
    return divisors_list


print(divisors(30))

            

        








#and returns a list of all the divisors(factors) of that that number -
#A divisor or factor is a number which divides evenly leaving no remainder

#define the funciton header called divisors expecting one argument

    #set up an empty list to hold your result
 
    
    #loop i from 1 to the number you are checking (take care not to include the number itself)

        #if the remainder when dividing the number by i is equal to zero then i is a divisor so...

            #apend i to the list you set up

 
    #return the list


#to test the divisors function uncomment the following line it should give [1,2,3,5,6,10,15]
#print(divisors(30))

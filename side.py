from random import randint

def fun(a):
    chosen_numb = randint(1,a)
    in_numb = 0
    while in_numb != chosen_numb:
        try:
            in_numb = int(input("Please! enter a  number: "))        
        
        except ValueError: 
            print("Please! Enter a number.")
        
        if a >= in_numb>= chosen_numb:
            print("Number is greater")
        elif 1 <= in_numb <= chosen_numb: 
            print("Number is smaller")
        elif 1> in_numb or in_numb > a:
            print(f"Please! enter a number between 1 and {a}") 
    
    print(f"Congratulations! Your number {chosen_numb} is correct")


fun(10)
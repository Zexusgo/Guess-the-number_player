from random import randint 

def guess(x):
    high = x
    low = 0
    comp_no = 0
    max_attempt = 5
    attempt = 0
    while attempt < max_attempt:
        comp_no = randint(low,high)
        User_in = input(f"If gussessed {comp_no} is too high (H), and if gusssessed number is too low (L) or correct (C): ").lower()
        
        while User_in not in ['h','l','c']:
            print("Please, input only H, L or C")
            User_in = input(f"If gussessed {comp_no} is too high (H), and if gusssessed number is too low (L) or correct (C): ").lower()
       
        if User_in == "h":
            high = comp_no - 1
        elif User_in == "l":
            low = comp_no + 1
        elif User_in == "c":
            print("Bingo! It's the correct number")
            break
        
            
        if low > high:
            print(f"Please check the {low} lower bound.")
            break
        
        attempt += 1
        print(f"Number of attempt made {attempt} out of {max_attempt}")

        if attempt == max_attempt:
            print("Better luck next time!.")

guess(10)
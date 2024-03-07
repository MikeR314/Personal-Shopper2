# Shopping budget tool to assist users, manage spending, calculate remaining funds and warn if they are overspent

# First find out the user's total budget, and spend so far
budget = float(input("What is your total shopping budget : "))
total_spend = float(input("How much have you spent so far : "))
remaining = budget - total_spend
print(f"You have £{remaining} left")

# Provide warning if overspent, and end suggestions there
if remaining < 0 :
    print("You have overspent. Please don't buy anything else!")
    
# Provide warning if close to budget, and end suggestions there
elif remaining < 20 :
    print("You are getting close to your budget, you should consider stopping")
    
# Otherwise ask if they would like some help on what to spend
else :
    print("You have plenty of money left to spend")
    
    # Use .lower() to ensure answer is lower case
    suggestion = input("Would you like some suggestions on what to buy (y/n)? : ").lower()
        
    # Use a while loop to go back if the answer isn't y or n
    while suggestion != "y" and suggestion != "n" :
        print("That is not a valid option")
        suggestion = input("Would you like some suggestions on what to buy (y/n)? : ").lower()
    
    # Terminate if they don't want suggestions
    if suggestion == "n":
        print("OK. Good luck with your spending")
        
    # Otherwise ask more questions to get ideas - use .lower() again
    elif suggestion == "y":
        print("\nOK, let's start with some questions to see what you're into and get some ideas\n")
        jewellery = input("Do you wear jewellery (y/n)? : ").lower()
        flowers = input("Do you like flowers (y/n)? : ").lower()
        tv = input("Do you enjoy watching TV (y/n)? : ").lower()
        if tv == "y":
            netflix = input("Do you already have a Netflix subscription (y/n)? : ").lower()
        sports = input("Do you like sports (y/n)? : ").lower()
        if sports == "y":
            football = input("Do you watch football (y/n) : ").lower()
            if football == "y":
                team = input("Which team do you support? : ")
        if jewellery != "y" and flowers != "y" and tv != "y" and sports != "y":
            print("Wow, you're a tricky one. Maybe an Amazon voucher would work for you")
        else :
            print("\nOk here are some suggestions for you: \n")
            # If jewellery is yes give some options
            if jewellery == "y":
                # Give a fancy option if they have lots of money to spend, and a budget option if not
                if remaining > 100:
                    print("There is some lovely jewellery at Tiffany & Co")
                else :
                    print("You can get some bargain jewellery on Etsy")           
                  
            # Give some info if and only if they like flowers
            if flowers == "y":
                print("There is a sale on at the local florist")        
            
            # Give some suggestion on TV if they like TV, and if they have Netflix
            if tv == "y":
                if netflix == "y":
                    print("Maybe you could upgrade Netflix, or consider another service such as Amazon Prime")
                else :
                    print("A subscription to Netflix is a great idea")        
        
        
            if sports == "y":
                # If yes, find out which team to provide a suggestion
                if football == "y":
                    print(f"You can buy {team} shirts at their online store")
                # If not, give a non-football specific sport recommendation
                else :
                    print("You can buy general sports clothing at Sports Direct")

            # Give a closing statement for everyone
            print("\nI hope this helped you keep track of your spending, and gave you good ideas for what to buy")      

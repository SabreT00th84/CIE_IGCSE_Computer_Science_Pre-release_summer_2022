from datetime import datetime, timedelta
def list_str (list):
    if len(list) > 1:
        return ", ".join(list[:len(list) - 1]) + f" and {list[len(list) - 1]}"
    elif len(list) == 1:
        return f"{list[0]}"
    else:
        return "no one"
    
member_names = ["Donald Trump", "Bob Robertson", "Julia Roebuck"]
sponser_names = ["Boris Johnson"]
messages = ["Donald Trump?! What are you doing here?!"]
join_dates = ["7/1/2021", "12/5/2021", "2/1/2022"]
paid = ["Bob Robertson", "Julia roebuck"]
not_paid = ["Donald Trump"]
expired = []
volunteers = ["Julia Roebuck", "Bob Robertson"]
entrance = []
gift_shop = ["Julia Roebuck"]
decorating = ["Bob Robertson"]
thank_you = "\nThank you for using our program!"
run = True

print("Welcome to the Seaview Pier automated membership program")
while run == True:
    user_choice = input("\nPlease select a menu option:\n(A) apply for a membership\n(S) sponser a plank of the pier\n(R) report\n(Q) quit\n: ").upper()
    if user_choice == "A":
        name = input("\nPlease enter your full name\n: ")
        print(f"\nWelcome to Seaview Pier {name}!\nYou will be working with {list_str(member_names)}.")
        member_names.append(name)
        join_dates.append(datetime.now().strftime("%d/%m/%Y"))
        pay = input("\nPay the $75 joining fee\n(N) now\n(L) later\n: ").upper()
        if pay == "N":
            paid.append(name)
            print("Thank you for paying now!")
        else:
            not_paid.append(name)
        volunteer = input( "\nWould you like to volunteer? \n(Y) yes\n(N) no\n: ").upper()
        if volunteer == "Y":
            volunteers.append(name)
            print("\nHow would you like to volunteer?")
            role = input("(E) at the pier entrance gate\n(G) at the gift shop\n(P) by painting and decorating\n: ").upper()
            if role == "E":
                entrance.append(name)
            elif role == "G":
                gift_shop.append(name)
            elif role == "P":
                decorating.append(name)
        else:
            volunteers.append(False)  
        print("\nAll memberships will expire one year after application")
    elif user_choice == "S":
        valid = ""
        print("\nThank you for chhosing to sponsor the pier! We rely heavily on your donations. A brass plaque with a short message of your choice will be put on a wooden plank of the pier.")
        name = input("\nPlease enter your full name\n: ")
        sponser_names.append(name)
        while valid != "Y":
            message = input("\nPlease enter the message you would like to display on your brass plaque\n: ")
            valid = input(f"\nPlease confirm your message:\n{message}\n(Y) yes, continue\n(N) no, correct it\n: ").upper()
        messages.append(message)
        pay = input("\nPlease pay the $200 donation\n(P) pay \n(Q) quit\n: ").upper()
        if pay == "P":
            print("Thank you for your donation!")
        else:
            print(thank_you)
            run = False
    elif user_choice == "R":
        print("\n")
        year_limit = datetime.today() - timedelta(weeks = 52)
        for date in join_dates:
            join_date = datetime.strptime(date, "%d/%m/%Y")
            if join_date < year_limit:
                expired.append(member_names[join_dates.index(date)])
        print(f"volunteers: {list_str(volunteers)}")
        print(f"\t entrance: {list_str(entrance)}")
        print(f"\t gift shop: {list_str(gift_shop)}")
        print(f"\tdecorating: {list_str(decorating)}")
        print(f"expired memberships: {list_str(expired)}")
        print(f"members who haven't yet paid: {list_str(not_paid)}")
    elif user_choice == "Q":
        print(thank_you)
        run = False
    else:
        print("\nInvalid choice, please try again")
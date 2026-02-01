movies = input("Do you like movies?")
if movies == 'yes':
    car = input("Do you have a car?")
    if car == 'yes':
        print("Go to the theatre")
    else:
        print("Watch netflix")
else:
     walk = input("Are you tired?")
     if walk == 'yes':
         print("Sleep at home")
     else:
         print("Go for a walk")
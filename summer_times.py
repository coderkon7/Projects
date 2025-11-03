snow = input("Is there snow outside? y/n: ").lower()
if snow == "y":
    snow_melting = input("Is the snow melting? y/n: ").lower()
    if snow_melting == "y":
        season = "spring"
    if snow_melting == "n":
        season = "winter"
    else:
        print("Invalid input. Please only type either 'y' or 'n'")
elif snow == "n":
    colored_leaves = input("Are the trees' leaves different colors, such as red, orange, and brown? y/n: ").lower()
    if colored_leaves == "y":
        season = "fall"
    elif colored_leaves == "n":
        clothing = input("Are you still wearing a lot of hoodies, sweaters, jackets, or boots? y/n: ").lower()
        if clothing == "y":
            season = "spring"
        elif clothing == "n":
            season = "summer"
        else:
            print("Invalid input. Please only type either 'y' or 'n'")
    else:
        print("Invalid input. Please only type either 'y' or 'n'")
else:
    print("Invalid input. Please only type either 'y' or 'n'")


if season == "spring":
    print("The current season is: Spring")
    print("You should have a cookie")
    print("You should go outside to ride your bicycle")
elif season == "summer":
    print("The current season is: Summer")
    print("You should have an ice cream cone and a popsicle")
    print("You should go to the beach")
elif season == "fall":
    print("The current season is: Fall")
    print("You should have an ice cream cone (to enjoy the last bits of warm temperatures) and a cookie")
    print("You should go make a leaf pile")
elif season == "winter":
    print("The current season is: Winter")
    print("You should have a cup of hot chocolate")
    print("You should go sledding")
else:
    print("This is not a known season within the program.")
print("Welcome to My Fun Mom Password Game")
password = "hikergirl"
guess = ""
while guess != "hikergirl":
    guess = input("please try and guess the password: ")
    if guess != "hikergirl":
        print("Oh dear you didn't get it right. No supper for you")
print("You win! I'll make you supper tomorrow!")
words = float (input ("how many words did you type: "))
time = float (input ("how many minutes did it take you to type them: "))

def typing_speed (words, time):
    answer= words / time
    return answer

print ("Your typing speed is: ", typing_speed(words, time), "words per minute")
class reverse():

    def __init__(self, s):
         self.s = s
    
    def reverseMethod(self):
         print("Reversed word: ", self.s[::-1])

userinput = input("Enter a word you wish to reverse: ")
word = reverse(userinput)
word.reverseMethod()
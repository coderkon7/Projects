class RomanNumeral():
    def __init__(self, num):
        self.num = num
    
    def convert(self):
        # -------------------
        # I tried to manually code the number to roman numeral conversion, but I couldn't figure it out, so I copied this code from this website: https://www.geeksforgeeks.org/python/python-program-to-convert-integer-to-roman/
        num = [1, 4, 5, 9, 10, 40, 50, 90,
            100, 400, 500, 900, 1000]
        sym = ["I", "IV", "V", "IX", "X", "XL",
            "L", "XC", "C", "CD", "D", "CM", "M"]
        i = 12
        
        while self.num:
            div = self.num // num[i]
            self.num %= num[i]

            while div:
                print(sym[i], end = "")
                div -= 1
            i -= 1
        return self.num
        # -------------------           
        

num = int(input("Enter the number you want to convert to Roman numerals: "))
Object = RomanNumeral(num)
Object.convert()
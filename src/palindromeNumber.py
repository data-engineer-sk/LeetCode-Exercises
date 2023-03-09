# Palindrome Number 
# e.g. 123321 is Palindrome and 123431 is not

class PN():
    def checkPalindromeNumber(self, num:int) -> bool:
        from math import trunc
        
        convertNum = str(num)
        numLength = len(convertNum)
        halfLength = trunc(numLength/2)
        result = False

        if (num < 0):
            return result

        for i in range(0, numLength-1):
            if (i <= halfLength):
                if (convertNum[i] == convertNum[numLength - i - 1]):
                    print(convertNum[i])
                    if (i == halfLength):
                        result = True
                else:
                    break

        return result

myObject = PN()
# inNum = 123454321
inNum = int(input("Please enter an integer : "))
if (myObject.checkPalindromeNumber(inNum)):
    print(f"{inNum} is palindrome number ")
else:
    print(f"{inNum} is not a palindrome number ")
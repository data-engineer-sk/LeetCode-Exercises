class Solution:
    def isPalindrome(self, num:int) -> bool:
        from math import trunc

        convertNum = str(num)
        numLength = len(convertNum)
        halfLength = trunc(numLength/2)
        result = False
        
        if (num < 0):
            return result

        for i in range(0, numLength-1):
            if (i <= halfLength):
                if(convertNum[i] == convertNum[numLength - i - 1]):
                    if(i == halfLength):
                        result = True
                        break
                else:
                    break
        return result

myObject = Solution()
# inNum = 123454321
inNum = int(input("Please enter an integer : "))
if (myObject.isPalindrome(inNum)):
    print(f"{inNum} is palindrome number ")
else:
    print(f"{inNum} is not a palindrome number ")
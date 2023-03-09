# Must Study # 1
# Moving Window
class checkLongestSubString:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Initialize variable
        charSet = set()
        startPointer = 0
        res = 0

        # now s='astublisucdefvxiz'
        for endPointer in range(len(s)):
            # Check the character is in the set or not? If Yes, remove it.
            while s[endPointer] in charSet:
                charSet.remove(s[startPointer])
                print("Start Pointer Postion : ", startPointer)
                # Set the pointer to point to the next starting position
                startPointer += 1

            charSet.add(s[endPointer])
            print("This is charSet : ", charSet)
            res = max(res, endPointer - startPointer + 1)  # Check and return a larger number, here the largeer position
            print("Count String Length : ", res)
        return res

myObject = checkLongestSubString()
result = myObject.lengthOfLongestSubstring('astublisucdefvxiz')
print(result)
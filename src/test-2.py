# List Testing
class LT():
    def swapPair(self, a1: list) -> list:
        # result a2 = [2,1,4,3]
        numOfElement = len(a1)
        i = 0
        while i < numOfElement:
            temp = a1[i]
            a1[i] = a1[i+1] 
            a1[i+1] = temp
            i += 2

        return a1
        
myObject = LT()
curList=[1,2,3,4,5,6,7,8]
print(curList)
print(myObject.swapPair(curList))
        




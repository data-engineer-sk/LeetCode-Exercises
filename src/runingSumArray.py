# Running Sum of Array 
# https://dev.to/shubhamtiwari909/reduce-method-to-sum-values-of-array-of-objects-33bk

class RSA():
    def runningSumOfArray(self, inList:list) -> int:
        result = inList[0]
        for counter in range(len(inList)):  # for inList = [3,1,2,10,1], thus len(inList) = 5
            if counter < len(inList)-1:     # Keep this so that the len(inList) will not be exceeded
                result += inList[counter+1]
                inList[counter+1] = result  

        return result

sum = RSA()
myList = [3,1,2,10,1]
print(sum.runningSumOfArray(myList))

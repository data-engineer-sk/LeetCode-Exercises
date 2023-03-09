# Must Study
# Researse an Integer
class ReverseClass():
    def reverse(self,num:int) -> int:
        temp = str(num)
        myTemp1 = []
        # Read the integer into list
        for i in range(len(temp)):
            myTemp1.append(temp[i])

        # Reverse the element order in a list
        KeepOn = True
        myTemp2 = []
        myTemp3 = []
        i = 1
        while KeepOn:
            if (i < len(myTemp1)):
                tempVal = myTemp1[len(myTemp1)-i]
                myTemp2.append(myTemp1[i])
                myTemp3.append(tempVal)
                i += 1
            else:
                # Add the last one to the list
                myTemp3.append(myTemp1[0])
                break

        # Convert the list to string by .join function
        result = ''.join(myTemp3)
        return int(result)

myObject = ReverseClass()
inVal = input("Please enter a number : ")
print("The original number is : ", int(inVal))
print("The reverse number is : ", myObject.reverse(inVal))


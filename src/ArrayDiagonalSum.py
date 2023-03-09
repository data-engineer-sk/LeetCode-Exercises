class twoD():
    def twoD_DiagonalArraySum(self):
        self.a1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        total = 0
        for count in range(len(self.a1)):
            print(self.a1[count][count])
            total += self.a1[count][count]

        return total
    
myObject = twoD()
result = myObject.twoD_DiagonalArraySum()
print(result)
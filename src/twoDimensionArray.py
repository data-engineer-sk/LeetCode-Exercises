class twoDimensionA():
    def twoDimensionArray(self):
        self.myList = []
        self.myList = [['a','b','c'],['x','y','z']]

        for row in self.myList:
            print(row)

        for i in range(len(self.myList)):
            for j in range(len(self.myList[i])):
                print(self.myList[i][j])

myObject = twoDimensionA()
myObject.twoDimensionArray()


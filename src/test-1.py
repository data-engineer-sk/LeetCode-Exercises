# Max area
class Container():
    def maxArea(self, height: list[int]) -> int:
        maxarea = 0
        for left in range(len(height)):
            for right in range(left + 1, len(height)):
                width = right - left
                maxarea = max(maxarea, min(height[left], height[right]) * width)

        return maxarea

myObject = Container()
l = [1, 8, 6, 2, 5, 4, 8, 3, 7]

result = myObject.maxArea(l)
print (result)

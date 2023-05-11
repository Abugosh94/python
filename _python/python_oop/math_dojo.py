class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        self.result += num
        for x in nums:
            self.result += x
        return self
    def subtract(self, num, *nums):
        self.result -= num
        for x in nums:
            self.result -= x
        return self
# create an instance:
md = MathDojo()
# to test:
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)	# should print 5
# Write the add method and test it by calling it 3 times, with different numbers of arguments each time

x = md.add(4).add(5,8,9).add(13,8,5,3,2,1,1).result
print (x)

#Write the subtract method and test it by calling it 3 times, with different numbers of arguments each time
x = md.subtract(2).subtract(9,5,4).subtract(3,5,8).result
print (x)

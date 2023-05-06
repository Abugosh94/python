import random
def randInt(min=0, max=100):
    if(max<0 and min>max):
        return "Please enter a minimum number less than 0 and the max"
    if(min>max):
        return "Minimum number cannot be bigger than the maximum"
    if(max>0):
        num = random.random()*(max-min) + min
    else:
        num = random.random()*(min-max) + max
    return round(num)
#print(randInt()) 	# should print a random integer between 0 to 100
#print(randInt(max=50)) 	# should print a random integer between 0 to 50
#print(randInt(min=50)) 	# should print a random integer between 50 to 100
#print(randInt(min=50, max=500))    # should print a random integer between 50 and 500
#print(randInt(min=50, max=20)) #Should return an error message to fix inputs
#print(randInt(min=-30, max=-25)) #Should return a negative number between -30 and -25
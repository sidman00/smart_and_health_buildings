import random
def good_bye():
    num_iterations = random.randint(1,25)
    print("I will say goodbye "+str(num_iterations)+" times")
    for iteration in range(num_iterations):
        print("good bye cruel world")
good_bye()
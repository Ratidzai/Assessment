counter = 3

def tester():
    global counter # This is the line I added for the outpu to run which is 4
    counter += 1
    print(counter)

tester()

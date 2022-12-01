print(“it was just a normal day in\033[33]m”,Place,“\033[33]m, nothing much going on at the moment.”)

'''
fruit = input("""
which fruit do you like best
apple
banana
blueberry
watermelon
""")
if fruit.lower() == "apple":
	colorcode = "\033[31m"
	color = "red"
if fruit.lower() == "watermelon":
	colorcode = "\033[32m"
	color = "green"
if fruit.lower() == "banana":
	colorcode = "\033[33m"
	color = "yellow"
if fruit.lower() == "blueberry":
	colorcode = "\033[33m"
	color = "blue"
white = "\033[0m"
sentence = "so your favorite fruit is a " + colorcode + fruit + white + " Because they are the color " + colorcode + color + white + " Mine is \033[33mbananas"
print(sentence)
'''
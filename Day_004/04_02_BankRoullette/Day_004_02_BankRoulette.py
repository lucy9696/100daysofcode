import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
choice = random.sample(names, 1)
choice=str(choice)
choice=choice.replace("[","")
choice=choice.replace("]","")
choice=choice.strip("'")
print(f'{choice} is going to buy the meal today!')
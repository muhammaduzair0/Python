age = 6
pet = 'cat'

if (pet == 'dog' and age < 2):
    food = 'Puppy food'
elif (pet == 'cat' and age > 5):
    food = 'Senior cat food'
else:
    food = 'Not any recommendation'

print("Food recommendation for your pet: ", food)
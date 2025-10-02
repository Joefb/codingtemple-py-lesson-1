# IMPORTS
import os


### PRINT INTRO
print("")
print("")
print("")
print('"Welcome to Joes Pizza Shack!" Joe says to you as you enter the shack."')
print("")
print("")
print(
    'Joe walks up with a big smile, hands you a menu and says, "Hello there! What can I get for ya today?"'
)
print(
    "Amazed by the sheer beauty of Joe, totally in awe you take a look at the menu and say: "
)
print("")
print("#### Joes Menu ####")
print("1. Pizza - $150.99")
print("2. Burger - $12.50")
print("3. Salad - $9.99")
print("4. Pasta - $13.75")
print("")
print("")

### GET INPUT AND SET VARS
total_price = 0
food_price = 0
food = ""
order = int(input("Please enter the number for item you would like to order: "))

input("Press enter to continue...")
os.system("clear")


### CONDITIONALS
print("")
print("")

if order < 1 or order > 4:
    print(
        '"We dont have that here!" Joe yells! "What kind of place do you think this is? Now get out!"'
    )

if order == 1:
    print(
        '"150.99 for a pizza!" You say in shock as Joe smiles and nods his head. "Ill take it! But it better be good or else!"'
    )
    total_price += 150.99
    food = "Pizza"
    food_price = 150.99

if order == 2:
    print(
        '"That burger looks amazing! Not as good as your big guns but Ill take one!!" You say as Joe flexes the biggest muscles you have ever seen.'
    )
    total_price += 12.50
    food = "Burger"
    food_price = 12.50

if order == 3:
    print(
        '"Im on a diet and need to be healthy. Ill take a salad!" You say. Joe maintains his smile as he throws up in his mouth. "Another dirty vegan." He thinks.'
    )
    total_price += 9.99
    food = "Salad"
    food_price = 9.99

if order == 4:
    print(
        '"Is that pasta gluten free?" You ask. Joe smiles and says "Why yes it is!" But really he has no idea. "Ill take a it!" you yell!'
    )
    total_price += 13.75
    food = "Pasta"
    food_price = 13.75


print("")
print(
    'As Joe writes down your order he asks you, "Would you like a drink with that my friend? Only an extra $2.50!"'
)

### GET INPUT AND SET VARS
drink = input("Please enter yes or no: ").lower()
getting_drink = ""

### CLEAR SCREEN
input("Press enter to continue...")
os.system("clear")

### DRINK CONDITIONAL
print("")
if drink == "yes":
    print(
        '"Yes please, I will take a coke, light ice, not too cold, in a glass not a cup, gluten free, paper straw not plastic, and make sure to recycle the straw after Im done." With a puzzeled look Joe says "Coming right up!" and hurrys to the back.'
    )
    total_price += 2.50
    getting_drink = "Yes"

if drink == "no":
    print(
        '"No thanks, just the food is fine. Soda gives you anal cancer." You say as Joe nods and heads to the back. You think you hear him say "Peasant" as he walks away.'
    )
    getting_drink = "No"

print("")

### CLEAR SCREEN
input("Press enter to continue...")
os.system("clear")

print("")
print("")

print(
    "You smash down the food like its 1999 and quickly flee to the bathroom to unleash hell."
)

print("")
print(
    'As you exit the bathroom without washing your hands Joe says "You ok my friend? You were in there for almost an hour! Here is your check." '
)

input("Press enter to continue...")
os.system("clear")

### PRINT RECEIPT
print("")
print("")
print("You look down at your receipt and see: ")
print("")
print("#### Your Order ####")
print(f"Food: {food} - {food_price}")
print(f"Drink: {getting_drink} - $2.50")
print(f"Subtotal: ${total_price}")
print(f"Tax: ${total_price * 0.08:.2f}")
print(f"Total: ${total_price * 1.08:.2f}")
print("")
input("Press enter to continue...")
print(
    "You pay Joe, get one last peek at his firm pecs and exit the shack. And you live happily ever after."
)

# **Intro to Python \- Homework Assignment: Lessons 1-2**

## **Variables, Input/Output & Control Flow**

**Important Instructions:**

- **Create a Python file in VS Code** for each question (e.g., question1.py, question2.py, etc.)
- Test each program to make sure it works correctly
- Save all your Python files in a folder called "homework"
- Upload the work to github and submit the link to the repository

---

## **Question 1: Movie Ticket Pricing (Lesson 1 \- Variables & Output)**

**Points: 8**

Write a Python program that calculates movie ticket costs with different pricing.

**Requirements:**

- Ask the user for their name and age
- Set ticket prices:
  - Child (under 13): $8
  - _Adult_(13−64):$12
  - Senior (65+): $9
- Ask how many tickets they want (Ticket prices should be calculated based on the age of the person buying them)
- Calculate total cost and display a receipt-style output
- Use f-string formatting for the receipt

**Create file:** question1.py

**Example Output:**

```
Enter your name: Sarah
Enter your age: 28
How many tickets do you want? 2

=== MOVIE TICKET RECEIPT ===
Customer: Sarah
Ticket Type: Adult ($12.00 each)
Quantity: 2
Total Cost: $24.00
Thank you for your purchase!
```

---

## **Question 2: Restaurant Order System (Lesson 2 \- If/Elif/Else)**

**Points: 10**

Create a program that takes a restaurant order and calculates the bill based on menu choices.

**Requirements:**

- Display a menu with 4 food options and prices:

1. Pizza \- $15.99
2. Burger \- $12.50
3. Salad \- $9.99
4. Pasta \- $13.75

- Ask user to choose by number (1-4)
- Ask if they want a drink (+$2.50)
- Calculate total with 8% tax
- Display itemized bill

**Create file:** question2.py

**Example Output:**

```
=== RESTAURANT MENU ===
1. Pizza - $15.99
2. Burger - $12.50
3. Salad - $9.99
4. Pasta - $13.75

Enter your choice (1-4): 1
Would you like a drink? (+$2.50) (yes/no): yes

=== YOUR ORDER ===
Food: Pizza - $15.99
Drink: Yes - $2.50
Subtotal: $18.49
Tax (8%): $1.48
Total: $19.97
```

---

## **Question 3: Pet Age Calculator (Lessons 1-2 Combined)**

**Points: 12**

Create a program that converts human years to pet years for different animals.

**Requirements:**

- Ask for pet type (dog, cat, bird, hamster)
- Ask for pet's age in human years
- Convert using these formulas:
  - Dog: First 2 years \= 24 pet years, then 4 years for each additional year
  - Cat: First 2 years \= 24 pet years, then 4 years for each additional year
  - Bird: Multiply by 9
  - Hamster: Multiply by 25
- Display the converted age with a fun message

**Create file:** question3.py

**Example Output:**

```
Enter pet type (dog/cat/bird/hamster): dog
Enter your pet's age in human years: 5

=== PET AGE CONVERSION ===
Pet Type: Dog
Human Age: 5 years
Pet Age: 36 pet years

Fun Fact: Your dog is like a 36-year-old human!

Enter pet type (dog/cat/bird/hamster): hamster
Enter your pet's age in human years: 2
=== PET AGE CONVERSION ===
Pet Type: Hamster
Human Age: 2 years
Pet Age: 50 pet years

Fun Fact: Your hamster is like a 50-year-old human!
```

---

## **Getting Help**

If you get stuck:

1. Review the lesson materials from lessons 1-2
2. Try breaking down the problem into smaller steps
3. Test your code frequently as you write it
4. Ask questions during office hours or in class
5. Remember to save your work frequently in VS Code

**Remember:** The goal is to practice and learn. Focus on understanding the concepts.

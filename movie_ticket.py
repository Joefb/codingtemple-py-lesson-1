def display_welcome():
    print("###### Welcome to Joe Movies Unlimited! #########")
    print("")

    print("### Ticket Prices: ########")
    print("#                         #")
    print("# Child(13 and under): $8 #")
    print("# Adult(13-64): $12       #")
    print("# Senior(65+): $9          #")
    print("#                         #")
    print("###########################")
    print("")

    name = input("What is your name? ")
    print(f"Hello {name}, nice to meet you!")
    age = int(input("What is  your age? "))
    num_of_tickets = int(input("How many tickets would you like to buy? "))
    total_price, ticket_type = calc_price(age, num_of_tickets)

    print("### Receipt ##########################")
    print(f"# Name: {name}                      #")
    print(f"# Age: {age}                        #")
    print(f"# Ticket Type: {ticket_type}        #")
    print(f"# Tickets: {num_of_tickets}         #")
    print(f"# Total Price: ${total_price}       #")
    print("#                                    #")
    print("######################################")


def calc_price(age, tickets):
    child_price = 8
    adult_price = 12
    sedior_price = 9
    total_price = 0
    ticket_type = ""

    if age <= 13:
        total_price = child_price * tickets
        ticket_type = "Child($8.00)"

    if (age > 13) and (age < 65):
        total_price = adult_price * tickets
        ticket_type = "Adult($12.00 each)"

    if age >= 65:
        total_price = sedior_price * tickets
        ticket_type = "Senior($9.00 each)"

    return total_price, ticket_type


display_welcome()

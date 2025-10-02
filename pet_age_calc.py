# Convert human years to pet years
# Ask pet type store in vars
# Ask pet age store in vars
# If dog or cat human_years  = 24 + ((years_old - 2) * 4)
# If dog or cat = 1 years_old = 12
# If bird human_years = (years_old * 9)
# If Hamster human_years = (years_old * 25)
# Display pet type, human age, pet age

# CALC PET AGE
def calc_pet_age(pet_type, pet_age):
    new_pet_age = 0

    if pet_type == "dog" or pet_type == "cat":
        if pet_age == 1:
            new_pet_age = 12

    if pet_type == "dog" or pet_type == "cat":
        new_pet_age = 24 + ((pet_age - 2) * 4)

    if pet_type == "bird":
        new_pet_age = pet_age * 9

    if pet_type == "hamster":
        new_pet_age = pet_age * 25

    return new_pet_age


while True:
    try:
        print("=== Pet Age Conversion ===")
        pet_type = input(
            "Enter pet type (dog/cat/bird/hamster) or exit to quit: "
        ).lower()

        if pet_type == "exit":
            print("Goodbye!")
            exit()

        pet_years_old = int(input("Enter pet age in years: "))

        if (
            pet_type == "dog"
            or pet_type == "cat"
            or pet_type == "bird"
            or pet_type == "hamster"
        ):
            print(
                f"Calcutating age for a {pet_type} that is {pet_years_old} years old..."
            )
            print("")
            print(f"Pet Type: {pet_type}")
            print(f"Human Age: {pet_years_old} years")
            print(f"Pet Age: {calc_pet_age(pet_type, pet_years_old)} pet years")
            print("")
            print(
                f"Fun fact! Your {pet_type} is like a {calc_pet_age(pet_type, pet_years_old)} year old human!"
            )
            print("")

    except Exception:
        print("Error: Please enter a valid option!")
        continue

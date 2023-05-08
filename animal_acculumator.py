"""
CP1401 2023-1 Assignment 2
Animal Accumulator
Student Name: Joshua Bradley
Date started: April 17, 2023


Pseudocode:

function main()
    initialize day, total_income, animals
    display welcome message
    get animals_source (yes/no)
    set animals using determine_animals_source
    display animals
    set total_animals to length of animals

    display menu and get user choice
    while choice is not "q"
        if choice is "w"
            update day, total_income, total_animals using simulate_a_day
        else if choice is "d"
            display animals
        else if choice is "a"
            update animals and total_income using add_animal
            update total_animals to length of animals
        else
            display error message
        display day, total_animals, total_income, menu
        get user choice

    display final results
    ask user to save or not
    if user wants to save text
         save animals to file
    display closing message

function simulate_a_day(day, animals, total_income, total_animals)
    increment day
    generate random_luck
    if random_luck < 32
        update total_animals using choose_escaped_animal
    else
        update total_income using calculate_income
    return day, total_income, total_animals

function calculate_income(animals, random_luck, total_income)
    for each animal in animals
        calculate income based on name length and random_luck
        update total_income
    return total_income

function choose_escaped_animal(animals, total_animal)
    if total_animal > 0
        select random animal and remove from list
        update total_animal
        display escaped animal
    return total_animal

function determine_animals_source(animals_source, animals)
    if animals_source is not "n"
        read animals from "animals.txt"
    else
        set animals to snake, elephant, dingo
    return animals

function display_animal(total_animal, animals)
    display all animals separated by commas

function add_animal(animals, total_income)
    get new_animal with unique name
    calculate animal_price
    if enough total_income
        add animal to animals
        deduct animal_price from total_income
    return animals, total_income

function get_valid_name(prompt, animals)
    get name while it's unique and non-empty
    return name

function save_file(animals)
    save animals to "animals.txt"

"""
import random

WELCOME_MESSAGE = """
Welcome to the Animal Accumulator program!
Animals generate income based on name length and a random luck value (0-100).
Options:
- Wait (W): Simulate a day passing. Animal may escape if luck < 32.
- Display animals (D): Show current animals.
- Add new animal (A): Add a new animal to the list.
- Quit (Q): Quit the program.
Enjoy!"""

# Constants for menu options, luck values, and the luck threshold for animal escapes
STANDARD_ANIMALS = ["Snake", "Elephant", "Dingo"]
MIN_LUCK = 0
MAX_LUCK = 100
MIN_ANIMALS = 0
THRESHOLD_LUCK = 32
MENU = f"\n(W)ait" \
       f"\n(D)isplay animals" \
       f"\n(A)dd a new animal" \
       f"\n(Q)uit"


def main():
    """
    Main program for animal accumulator. It handles the user interaction, including displaying
    the menu, processing user inputs, and updating the game state.
    """

    # Initialize game state variables
    total_income = 0
    day = 0
    animals = []

    # Display the welcome message and load animals
    print(WELCOME_MESSAGE)
    animal_source = input(f"Would you like to load your animals from animals.txt (Y/n)? ")
    animals = determine_animals_source(animal_source, animals)

    # Display the initial animal list
    print("You start with these animals:")
    total_animals = len(animals)
    display_animal(total_animals, animals)

    # Display the initial game state and menu
    print(f"After {day} days, you have {total_animals} animals and your total income is {total_income}."
          f"{MENU}")
    choice = input("Choose:").upper()

    # Process user input until the user quits the game
    while choice != "Q":
        if choice == "W":
            day, total_income, total_animals = simulate_a_day(day, animals, total_income, total_animals)
        elif choice == "D":
            display_animal(total_animals, animals)
        elif choice == "A":
            animals, total_income = add_animal(animals, total_income)
            total_animals = len(animals)
        else:
            print("Invalid choice! Please choose again.")

            # Display the updated game state and menu
            print(f"After {day} days, you have {total_animals} animals and your total income is {total_income}."
                  f"{MENU}")
            choice = input("Choose:").upper()

    # Display the final results
    if total_animals == 0:
        print("You finished with no animals!")
    else:
        display_animal(total_animals, animals)

    # Prompt the user to save their progress and display a closing message
    save_or_not = input("Would you like to save your animals to animals.txt (Y/n)? ")
    if save_or_not != "n":
        save_file(animals)
    print("Thank you for simulating. Now enjoy some real animals!")


def simulate_a_day(day, animals, total_income, total_animals):
    """
    Simulate a day and update the total income and animal count.

    Parameters:
    - day: The current day
    - animals: A list of animals
    - total_income: The current total income
    - total_animals: The current total number of animals

    Returns:
    - A tuple containing the updated day, total_income, and total_animals
    """

    # Increment the day counter
    day += 1

    # Generate a random luck value for the day
    random_luck = random.randint(MIN_LUCK, MAX_LUCK)
    print(f"Today's luck value is {random_luck}.")

    # Check if the luck value is below the threshold, in which case an animal might escape
    if random_luck < THRESHOLD_LUCK:
        total_animals = choose_escaped_animal(animals, total_animals)
    else:
        # Calculate and update the income based on the current animals and luck value
        total_income = calculate_income(animals, random_luck, total_income)

    # Return the updated day, total_income, and total_animals
    return day, total_income, total_animals


def choose_escaped_animal(animals, total_animal):
    """
    Choose a random animal to escape from the animals list when the random luck value is below the threshold.

    Parameters:
    - animals: A list of animals
    - total_animal: The current total number of animals

    Returns:
    - The updated total number of animals after an animal escapes
    """
    # Check if the total number of animals is greater than the minimum allowed
    if total_animal > MIN_ANIMALS:
        # Select a random animal to escape
        escaped_animal = random.choice(animals)

        # Remove the escaped animal from the list
        animals.remove(escaped_animal)

        # Update the total number of animals
        total_animal = len(animals)

        # Notify the user about the escaped animal
        print(f"Sadly, your {escaped_animal} has escaped!.")

    # Return the updated total number of animals
    return total_animal


def calculate_income(animals, random_luck, total_income):
    """
    Calculate the income produced by each animal and update the total income.

    Parameters:
    - animals: A list of animals
    - random_luck: The random luck value generated for the day
    - total_income: The current total income

    Returns:
    - The updated total income
    """
    # Iterate through the list of animals
    for animal in animals:
        # Calculate the income produced by the current animal based on its name length
        name_length = len(animal)
        income = int((random_luck / 100) * name_length)

        # Update the total income by adding the income produced by the current animal
        total_income += income

        # Display the income produced by the current animal
        print(f"{animal} produced {income} !")

    # Return the updated total income
    return total_income


def determine_animals_source(animals_source, animals):
    """
        Determine the source of the initial animal list, either from a file or using a standard list.

        Parameters:
        - animals_source: User's input on whether to load animals from a file (y/n)
        - animals: A list of animals

        Returns:
        - The list of animals loaded from the chosen source
        """

    # Use the standard list of animals if the user chooses not to load from a file
    if animals_source == "n":
        animals = STANDARD_ANIMALS
    else:
        # Load animals from the "animals.txt" file
        in_file = open("animals.txt", 'r')

        # Iterate through the file and append each animal to the list
        for animal in in_file:
            animals.append(animal)

        # Close the file after reading all the animals
        in_file.close()

    # Return the list of animals from the chosen source
    return animals


def display_animal(total_animal, animals):
    """
    Displays the current animals in the given list, separated by commas.

    Parameters:
    - total_animal: The total number of animals in the list
    - animals: A list of animal names (strings)

    Returns:
    - None
    """

    # Only display the animals if the total number of animals is greater than MIN_LUCK
    if total_animal > MIN_LUCK:
        # Iterate through the animals list
        for animal in animals:
            # Check if the animal is the last element
            if animal == animals[-1]:
                # Display the last animal without a comma at the end
                print(animal.title())
            else:
                # Display the animal with a comma at the end
                print(animal.strip().title(), end=", ")
    else:
        # Print nothing if the total number of animals is not greater than MIN_LUCK
        print("")


def add_animal(animals, total_income):
    """
        Add a new animal to the list if the user has enough income to cover the cost of the animal.
        The cost of the animal is equal to the length of its name. If the user can't afford the animal,
        a message will be displayed.

        Parameters:
        - animals: A list of existing animals (strings)
        - total_income: The current total income (int)

        Returns:
        - A tuple containing the updated list of animals and the updated total income
        """
    # Get a valid animal name from the user
    new_animal = get_valid_name("Enter animal name: ", animals)
    # Calculate the cost of the new animal based on its name length
    animal_price = len(new_animal)

    # Check if the user has enough income to purchase the animal
    if animal_price > total_income:
        # Display a message indicating that the user can't afford the animal
        print(f"{new_animal} would cost {animal_price} food. With only {total_income}, you can't afford it.")
    else:
        # Add the new animal to the list and deduct its price from the total_income
        animals.append(new_animal)
        total_income -= animal_price

    # Return the updated animals list and total_income
    return animals, total_income


def get_valid_name(prompt, animals):
    """
    Get a unique, non-empty name for a new animal.

    Parameters:
    - prompt: A string prompt for the user input
    - animals: A list of existing animals

    Returns:
    - A unique, non-empty name for a new animal
    """
    # Get the user input for the new animal's name
    name = input(prompt).title()

    # Check if the name is empty or already exists in the list of animals
    while name == "" or name in animals:
        if name == "":
            # Display a message if the name is empty
            print("Invalid animal name.")
        else:
            # Display a message if the name already exists in the list of animals
            print(f"You already have a {name} animal.")

        # Ask the user for a new name
        name = input(prompt).title()

    # Return the unique, non-empty name
    return name


def save_file(animals):
    """
    Save the current list of animals to the "animals.txt" file.

    Parameters:
    - animals: A list of animals to be saved

    Returns:
    - None
    """
    # Open the "animals.txt" file in write mode
    in_file = open("animals.txt", 'w')

    # Write each animal to the file on a separate line
    for animal in animals:
        print(animal, file=in_file, sep="")

    # Close the file after writing
    in_file.close()

    # Print a confirmation message to the user
    print("Saved")


main()

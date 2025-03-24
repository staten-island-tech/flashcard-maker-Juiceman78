import json

info = input("Are you a Student or Teacher: ")

class Teacher:
    @staticmethod
    def make_cards():
        try:
            # Load existing flashcards from the file
            with open("flashcards.json", "r") as file:
                flashcards = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            # If the file doesn't exist or is empty, start with an empty dictionary
            flashcards = {}

        while True:
            a = input("Do you want to make a flashcard? (yes/no): ")
            if a.lower() == "yes":
                # Get the question and answer from the user
                question = input("What is your question? ")
                answer = input("What is your answer? ")
                # Add the flashcard to the dictionary
                flashcards[question] = answer
                # Save the updated flashcards to the file
                with open("flashcards.json", "w") as file:
                    json.dump(flashcards, file, indent=4)
                print("Flashcard saved!")
            elif a.lower() == "no":
                print("Have a nice day!")
                break
            else:
                print("Please enter a valid response (yes or no).")

class Student:
    @staticmethod
    def answer_cards():
        try:
            # Load existing flashcards from the file
            with open("flashcards.json", "r") as file:
                flashcards = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            # If the file doesn't exist or is empty, start with an empty dictionary
            flashcards = {}

        if not flashcards:
            print("There are no flashcards to study.")
        else:
            for question, answer in flashcards.items():
                input(f"Question: {question}\nPress Enter to see the Answer")
                print(f"Answer: {answer}")








if info.lower() == "teacher":
    Teacher.make_cards()
elif info.lower() == "student":
    Student.answer_cards()
else:
    print("Invalid role. Please restart the program.")
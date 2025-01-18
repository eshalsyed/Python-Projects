flashcards = []

point = 0

print("!!✨💥 FLASHCARDS 💥✨!!")


# Definings

def make():
    print("Let's make a flashcard!!")
    category = input("Enter subject: ").strip().lower()
    front = input("Front of the flashcard: ")
    back = input("Back of the flashcard: ")
    difficulty = input("Enter difficulty(easy/medium/hard): ").strip()
    if difficulty.lower() not in ["easy", "medium", "hard"]:
        print("Enter valid difficulty level")
        return 
    flashcards.append({"subject": category, 
                       "front": front, 
                       "back": back,
                        "difficulty": difficulty })
    print("Flashcards added succesfully!!")

def practice():
    global point
    if not flashcards:
        print("No flashcards were made to practice... ")
        return 
    
    sub = input("What subject would you like to practice?").strip().lower()
    subj = [flash for flash in flashcards if flash["subject"]== sub] 
    if not subj:
        print("No flashcards exist for this subject")
        return
    print(sub)
    for flash in subj:
        print(f"Question: {flash['front']}")
        ans = input("Answer: ").strip()

        if ans.lower() == flash['back'].lower() and flash['difficulty'].lower() == 'easy' :
            print("Correct!")
            point += 1
            print(f"Points: {point}")
        elif ans.lower() == flash['back'].lower() and flash['difficulty'].lower() == 'medium' :
            print("Correct!")
            point += 2
            print(f"Points: {point}")
        elif ans.lower() == flash['back'].lower() and flash['difficulty'].lower() == 'hard' :
            print("Correct!")
            point += 3
            print(f"Points: {point}")

        else: 
            print(f"Incorrect! Correct answer: {flash['back']}")
             

    print(f"Practice complete!! You achieved {point} points!")

def delete():
    if not flashcards:
        print("No flashcards are available to be deleted.")
        return
    
    print("Here are your flashcards:\n")
    for i, flash in enumerate(flashcards, start = 1):
        print(f"{i}) subject:{flash['subject']} | Question: {flash['front']} | difficulty: {flash['difficulty']} ")

    
    try: 
        dell = int(input("Enter the number of flashcard to delete: "))
        if 1 <= dell <= len(flashcards):
            remove = flashcards.pop(dell-1)
            print("Flashcard deleted succesfully!")
        else:
            print("Invalid number. Please try again.")
    except ValueError:
        print("Please enter a valid number.")


def progress():
    print("The progress system works by showing you how many points you have for correct answers:")
    print("Easy = 1 point per correct answear")
    print("Medium = 2 points per correct answear")
    print("Hard = 3 points per correct answear")
    print(f"Here are your points: {point}")
    
    



def main():
    while True:
        print("1. Make Flashcard")
        print("2. Practice flashcards by subject")
        print("3. Delete flashcard")
        print("4. Progress")
        print("5. Exit")
        choice = input("Enter option(1-5): ").strip()
        if choice == "1":
            make()
        elif choice == "2":
            practice()
        elif choice == "3":
            delete()
        elif choice == "4":
            progress()
        elif choice == "5":
            print("See you for your next set!")
            break
        else:
            print("Invalid option. Please try again")
main()

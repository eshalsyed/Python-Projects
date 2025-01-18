# Computer Science GCSE Revision quiz 

import difflib # Module that can compare sequences - Like strings

# Intro Level difficulty

print("\n           Welcome!!!\n")
print("You have now entered the")
print("COMPUTER SCIENCE GCSE REVISION PLACE!!!👾📚👩‍💻🎒\n")
print("""Here is how the point system works:\n
    1. Easy = 1 point per correct answear
    2. Medium = 2 points per correct answear
    3. Hard = 3 points per correct answear\n""")
print("Topic: 1.1 - Systems architecture\n")

# Points
point = 0 

# Defining 3 lvls - Subprograms

def easy():
    global point # Can use the point system with all defined functions 

    # Easy Q1 
    q_one_easy = input("""1.What is the role of the CPU in a computer system?\n
                       a) To store files
                       b) To process data and execute instructions
                       c) To provide power to the system
                       d) To connect to the internet
                        """)
    if q_one_easy == "b":
        print("Correct!✅")
        point +=1
    else:
        print("incorrect❌")

    # Easy Q2
    q_two_easy = input("""2.Which component is responsible for fetching, decoding, and executing instructions?\n
                       a) Cache
                       b) ALU
                       c) Control Unit
                       d) GPU""")
    if q_two_easy == "c":
        print("Correct!✅")
        point +=1
    else:
        print("Incorrect!❌")
    
    #Easy Q3
    q_three_easy = input("""3.What is the purpose of the ALU in the CPU?\n
                         a) To store data temporarily
                         b) To perform arithmetic and logical operations
                         c) To control the flow of data
                         d) To connect input and output devices """)
    if q_three_easy == "b" :
        print("Correct!✅")
        point +=1
    else:
        print("Incorrect!❌")
    
    print(f"You have {point} points!")


def medium():
    global point # Can use the point system with all defined functions

    # Medium Q1
    correct_one_m = """The Control Unit coordinates and controls all the operations of the CPU,
                     including fetching, decoding, and executing instructions."""
    q_one_m = input("What is the function of the Control Unit in the CPU?")
    similar_one_m = difflib.SequenceMatcher(None, q_one_m, correct_one_m).ratio()
    threshhold = 0.7 # Acceptance percent
    if similar_one_m >= threshhold:
        print("Correct!✅")
        point += 2
    else:
        print("Incorrect!❌")
    
    #Medium Q2
    correct_two_m = """Volatile memory, like RAM, loses its data when the power is turned 
                     off, while non-volatile memory, like ROM, retains data even when the power is off."""
    q_two_m = input("Name one difference between volatile and non-volatile memory.")
    similar_two_m = difflib.SequenceMatcher(None, q_two_m, correct_two_m).ratio()
    if similar_two_m >= threshhold:
        print("Correct!✅")
        point += 2
    else:
        print("Incorrect!❌")

    # Medium Q3
    correct_three_m = """Cache memory stores frequently accessed data and instructions,
                    allowing the CPU to access them more quickly than from main memory."""
    q_three_m = input("What is the purpose of cache memory in a computer?")
    similar_three_m = difflib.SequenceMatcher(None, q_three_m, correct_three_m).ratio()
    if similar_three_m >= threshhold:
        print("Correct!✅")
        point += 2
    else:
        print("Incorrect!❌")
    
    print(f"You have {point} points!")


def hard():
    global point # Can use the point system with all defined functions

    # Hard Q1
    correct_one_h = """The Fetch-Decode-Execute cycle is the process by which a CPU executes instructions.
    Fetch: The CPU retrieves an instruction from the memory, using the Program Counter to locate the instruction's memory address.
    Decode: The instruction is then sent to the Control Unit, which interprets it and determines the operation to be performed
    Execute: The CPU carries out the operation, such as performing a calculation in the ALU, storing data, or interacting with input/output devices.
    This cycle is essential as it allows the CPU to process and execute instructions systematically, enabling the computer to perform tasks efficiently."""
    q_one_h = input("Explain the Fetch-Decode-Execute cycle and why it is important for a CPU.")
    similar_one_h = difflib.SequenceMatcher(None, q_one_h, correct_one_h).ratio()
    threshhold_h = 0.8
    if similar_one_h >= threshhold_h:
        print("Correct!✅")
        point += 3
    else:
        print("Incorrect!❌")

    # Hard Q2
    correct_two_h = """Von Neumann architecture: This uses a single memory for both instructions and data, with the CPU accessing them via a single bus. It is commonly used in general-purpose computers.
    Harvard architecture: This has separate memory and buses for instructions and data, allowing faster processing since data and instructions can be accessed simultaneously. 
    It is typically used in embedded systems like microcontrollers."""
    q_two_h = input("Describe the difference between Harvard and Von Neumann architectures and give one example of where each is used.")
    similar_two_h = difflib.SequenceMatcher(None, q_two_h, correct_two_h).ratio()
    if similar_two_h >= threshhold_h:
        print("Correct!✅")
        point += 3
    else:
        print("Incorrect!❌")

    # Hard Q3
    correct_three_h = """"More cores allow a CPU to execute multiple instructions simultaneously, which improves performance for tasks that can be parallelized (e.g., video editing, gaming).
    However, adding more cores does not always result in a proportional increase in performance due to limitations such as 
    software not being optimized for multi-threading, increased power consumption, and challenges in heat dissipation. Some tasks are also inherently sequential and cannot take advantage of multiple cores."""
    q_three_h = input("How do the number of cores in a CPU affect performance, and what are the limitations of having more cores?")
    similar_three_h = difflib.SequenceMatcher(None, q_three_h, correct_three_h).ratio()
    if similar_three_h >= threshhold_h:
        print("Correct!✅")
        point += 3
    else:
        print("Incorrect!❌")

    print(f"You have {point} points!")



def main():
    while True:
        
        print("Here are 3 difficulty levels:\n")
        print("1.Easy🧠👌")
        print("2.Meduim🤩⭐️")
        print("3.Hard🤯")
        print("4.Exit🚪")

        ask_difficulty = input("Enter difficulty lvl: ")
        
        if ask_difficulty == "1" or ask_difficulty.lower() == "easy":
            easy()
        elif ask_difficulty == "2" or ask_difficulty.lower() == "medium":
            medium()
        elif ask_difficulty == "3" or ask_difficulty.lower() == "hard":
            hard()
        elif ask_difficulty == "4" or ask_difficulty.lower() == "exit":
            print("Bye!")
            break
        else:
            print("\nInvalid option!\n")
main()

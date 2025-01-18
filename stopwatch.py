import time

def main():
    print("STOPWATCH!\n")
    print("Instructions:")
    print("1. Press the 'Enter' key to start the stopwatch.")
    print("2. Press 'Enter' key again to stop it.")
    print("3. Type 'reset' to reset the stopwatch")
    print("4. Type 'quit' to exit.")

    while True:
        input("Press 'Enter' to start: ")
        print("Stopwatch started... ⏳")
        start_time = time.time()  

        input("Press 'Enter' to stop: ")
        end_time = time.time()  
        elapsed_time = end_time - start_time  

        print(f"Elapsed time: {elapsed_time:.2f} seconds⏱️")
        

        action = input("Type 'reset' to restart, or 'quit' to exit: ").strip().lower()
        
        if action == "quit":
            break

        elif action == "reset":
            print("Resetting the stopwatch...\n")


        else:
            print("Invalid input. Exiting stopwatch.")
            break


main()

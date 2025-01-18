import requests
import json


print("Hello!")

def joke():
    jokes = requests.get("https://official-joke-api.appspot.com/random_joke")
    j = jokes.json()

    if jokes.status_code== 200:
        j = jokes.json()
        print(j["setup"])
        return j
    else:
        print("There was an error recieving the punchline .\nPlease try again later")
        return None 
def punch(j):
    if j:
        print(j["punchline"])
    else:
        print("Appologies, there was an error recieving the joke.\nPlease try again later")


def main():
    while True:
        ask = input("Would you like to hear a joke?")
        if ask.lower() == "yes":
            print("No you cant hear the joke... you are going to see the joke. \n(because you're reading)😅\n")
            print("Here's the joke: ")
            j = joke()
            if j:
                ask_p = input("Would you like to hear the punchline?")
                if ask_p.lower() == "yes":
                    punch(j)
                elif ask_p.lower() == "no":
                    break
                else:
                    print("Please enter valid option - Yes or No?")
            else:
                break 

        elif ask.lower() == "no":
            print("Well... that's too bad. Bye bye!")
            break
        else:
            print("Please enter valid option - Yes or No?")
main()

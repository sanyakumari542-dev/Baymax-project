import random


def greetings():
    print("Hello! I am Baymax, your personal healthcare companion.")


err_msg = (
    "I do not understand. Please enter a number from 1 to 10.",
    "I cannot help you if you do not rate your pain.",
    "Please enter a number between 1 and 10.",
    "Rate your pain please, out of 10.",
)
scan_msg = ("I will scan you now.", "I will begin the scan now.")
scan_comp = "Scan complete!"
diagnosis = (
    "You have some snack deficiency!",
    "You are perfectly fine.",
    "Have a lollipop!",
    "happy-happy-happy~",
)
deactivate = (
    "I cannot deactivate until you say you are satisfied with your care.",
    "Are you satisfied with your care?",
    "You have to say you are satisfied for me to deactivate.",
)
action_err = (
    "Please choose one action.",
    "What would you like me to do?",
    "Scan, Medicine schedule or Exit?",
)


def goodbye():
    while True:
        print(random.choice(deactivate))
        bye = input().lower().strip()
        if bye == "i am satisfied with my care" or bye == "i am satisfied" or bye == "i'm satisfied with my care.":
            print("Patient satisfied.")
            print("Baymax deactivated.")
            return


def pain_inp():
    while True:
        try:
            print("On a scale of 1 to 10, how would you rate your pain?")
            pain = int(input())
            if 1 <= pain <= 10:
                return pain
            else:
                print(random.choice(err_msg))
        except ValueError:
            print(random.choice(err_msg))


def pain_eval(pain):
    if pain <= 4:
        pain_4 = (
            "You have been a good kid. Have a lollipop!",
            "You have a snack deficiency!",
            "Have some chocolates!",
            "Try going for a walk!",
        )
        print(random.choice(pain_4))
    elif pain <= 7:
        pain_7 = (
            "Your pain level is mild. I recommend a snack.",
            "That is mild. A short rest should help.",
            "Did you take a break from work yet?",
            "When was your last nap?",
            "Is it the high screen time?",
        )
        print(random.choice(pain_7))
    else:
        print("You should visit a Doctor!")


def menu():
    print("What would you like me to do?\na) Scan\nb) Medicine schedule record\nc) Exit")
    return input().strip().lower()


def scan():
    print(random.choice(scan_msg))
    print(scan_comp)
    print(random.choice(diagnosis))
    # placeholder, replace with real data


def medicine_schedule():
    med = (
        "Your medicine is scheduled after 1 hour.",
        "Take your medicine with warm water or milk in 10 mins.",
        "You have to take your medicine before bed.",
    )
    # placeholder, replace with real data in lvl3
    print(random.choice(med))


def task():
    while True:
        action = menu()
        if action == "scan" or action == "a":
            scan()
        elif action == "medicine schedule record" or action == "b":
            medicine_schedule()
        elif action == "exit" or action == "c":
            goodbye()
            return
        else:
            print(random.choice(action_err))


def main():
    greetings()

    pain_score = pain_inp()
    pain_eval(pain_score)
    task()


if __name__ == "__main__":
    main()

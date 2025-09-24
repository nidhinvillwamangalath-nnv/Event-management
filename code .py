print(" Welcome to Output Wedding Planner ")


hindu_wedding = {

    "Pre-Wedding Photoshoot": 25000,

    "Engagement": 10000,

    "Ganesh Puja": 12000,

    "Mehendi": 10000,

    "Haldi": 20000,

    "Sangeet": 22000,

    "Wedding Day": 150000,

    "Reception": 200000
}

christian_wedding = {
    "Pre-Wedding Photoshoot": 25000,

    "Betrothal Ceremony": 8000,

    "Bridal Shower": 6000,

    "Bachelor/Spinster Party": 15000,

    "Wedding Ceremony": 100000,

    "Reception": 180000
}

muslim_wedding = {
    "Pre-Wedding Photoshoot": 25000,

    "Mehendi": 10000,

    "Haldi/Mayun": 12000,

    "Dholki Night": 15000,

    "Nikah Ceremony": 50000,

    "Rukhsati": 10000,

    "Walima (Reception)": 120000
}

print("\nSelect Your Wedding Type:")

print("1. Hindu Wedding")

print("2. Christian Wedding")

print("3. Muslim Wedding")

choice = input("Enter your choice (1/2/3): ")

if choice == "1":

    selected = hindu_wedding.copy()

    name = "Hindu Wedding"

elif choice == "2":

    selected = christian_wedding.copy()

    name = "Christian Wedding"

elif choice == "3":

    selected = muslim_wedding.copy()

    name = "Muslim Wedding"

else:

    print(" Invalid choice.")

    exit()


print(f"\n {name} Package Includes:")

for event, cost in selected.items():

    print(f" - {event}: {cost}")

total = sum(selected.values())

print(f"\n Total Estimated Cost: {total}")



try:
    budget = int(input(" Please enter your total budget : "))

except ValueError:
    print(" Invalid input. Please enter a number.")
    exit()


while budget < total and len(selected) > 0:

    print("\n Your budget is lower than the current package.")

    print(" Please remove one or more events to reduce the cost.")

    print("Your Current Plan:")

    for i, (event, cost) in enumerate(selected.items(), 1):

        print(f"{i}. {event} - {cost}")

    try:

        remove_index = int(input("Enter the number of the event to remove: "))

        if 1 <= remove_index <= len(selected):

            event_to_remove = list(selected.keys())[remove_index - 1]

            removed_cost = selected.pop(event_to_remove)

            total = sum(selected.values())

            print(f" Removed '{event_to_remove}' ({removed_cost})")

            print(f" New Total Cost: {total}")

        else:
            print(" Invalid choice.")

    except ValueError:
        print(" Please enter a valid number.")


if len(selected) == 0:
    print("\n All events were removed. Please contact us directly for custom planning.")
    exit()


if budget >= total:
    print(f"\n Your current plan fits within your budget!")
    print(f"Remaining balance: {budget - total}")
    
    
    contact = input(" Please enter your contact number for our staff to contact our lovely client for arrangeing a meeting: ")

    if not contact.isdigit() or len(contact)< 10:
        print(" Invalid contact number. Please restart and try again.")
        exit()

    
    print("\n Final Event Plan:")

    for event, cost in selected.items():

        print(f" - {event}: {cost}")
    print(f"\n Final Total Cost: {total}")
    
    print("\n Thank you! Your details have been saved.")
    print(f" We will contact you soon at {contact}.")
    print("\n We always aim for *premium weddings*.")
    print(" A personalized meeting will be arranged to help you experience a *premium-class wedding within your budget*.")
    print("Honey Moon packages are available with up for a premium class budget frienly trip we can discus in meeting")

else:
    print("\n Sorry, your budget will not reach upto our quality.")

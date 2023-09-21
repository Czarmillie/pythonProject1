from enum import Enum
class GeopoliticalZone(Enum):
    SOUTHSOUTH = "Akwa-ibom", "Bayelsa", "Cross-rivers", "Delta", "Edo", "Rivers",
    NORTHEAST = "Adamawa", "Bauchi", "Borno", "Gombe", "Taraba", "Yobe",
    NORTHCENTRAL = "Benue", "FCT", "Kogi", "Kwara", "Nasarawa", "Niger", "Plateau",
    SOUTHEAST = "Abia", "Anambra", "Ebonyi", "Enugu", "Imo",
    SOUTHWEST = "Ekiti", "Lagos", "Osun", "Ondo", "Ogun", "Oyo",
    NORTHWEST = "Kaduna", "Katsina", "KKano", "Kebbi", "Sokoto", "Jigawa", "Zamfara",


def new_entry():
    try:
        entry = input("Enter your state:  ")
        if entry.capitalize() in GeopoliticalZone.SOUTHSOUTH.value:
            print('Your Geopolitical zone is South South')
        elif entry.capitalize() in GeopoliticalZone.NORTHEAST.value:
            print('Your Geopolitical zone is North East')
        elif entry.capitalize() in GeopoliticalZone.NORTHCENTRAL.value:
            print('Your Geopolitical zone is North Central')
        elif entry.capitalize() in GeopoliticalZone.SOUTHEAST.value:
            print('Your Geopolitical zone is South East')
        elif entry.capitalize() in GeopoliticalZone.SOUTHWEST.value:
            print('Your Geopolitical zone is South West')
        elif entry.capitalize() in GeopoliticalZone.NORTHWEST.value:
            print('Your Geopolitical zone is North West')
        else:
            print('Invalid input')
            new_entry()
    except (ValueError, SyntaxError, TypeError, KeyboardInterrupt, NameError, ZeroDivisionError):
        print()

new_entry()
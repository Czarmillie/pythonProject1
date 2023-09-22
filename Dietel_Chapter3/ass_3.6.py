print("What is your problem? ")
input()

print("Have you had this problem before (yes or no)? ")
response = input()

if response == 'yes':
    print("Well, you have it again.")
elif response == 'no':
    print("Well, you have it now.")
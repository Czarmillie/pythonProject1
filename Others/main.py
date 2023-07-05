while True:
    print("""
    List of menu functions
    1.  Phone Book
    2.  Messages
    3.  Chat
    4.  Call Register
    5.  Tones
    6.  Settings
    7.  Call Divert
    8.  Games
    9.  Calculator
    10. Reminder
    11. Clock
    12. Profiles
    13. Sim Services
    0.  Exit
    """)
    user_input = int(input("Press a Number: "))
    if user_input == 0:
        print("Exiting the menu app...")
        break

    elif user_input == 1:
        while True:
            print("""
            1.  Search
            2.  Service Nos
            3.  Add Name
            4.  Erase
            5.  Edit
            6.  Assign Tune
            7.  Send B'crd
            8.  Options
            9.  Speed Dials
            10. Voice Tags
            0.  Back
            """)
            user_input_a = int(input("Press a Number: "))

            if user_input_a == 0:
                break

            elif user_input_a == 8:
                while True:
                    print("""
                    1.  Type of View
                    2.  Memory Status
                    0.  Back
                    """)
                    user_input_b = int(input("Press a Number: "))
                    if user_input_b == 0:
                        break

    elif user_input == 2:
        while True:
            print("""
            1.  Write Message
            2.  Inbox
            3.  Outbox
            4.  Picture Messages
            5.  Templates
            6.  Smileys
            7.  Message Settings
            8.  Info Service
            9.  Voice Mailbox Number
            10. Service Command Editor
            0.  Back
            """)

            user_input_c = int(input("Press a Number: "))

            if user_input_c == 0:
                break

            elif user_input_c == 7:
                while True:
                    print("""
                    1.  Set 1
                    2.  Common
                    0.  Back
                    """)
                    user_input_d = int(input("Press a number: "))

                    if user_input_d == 0:
                        break

                    elif user_input_d == 1:
                        while True:
                            print("""
                            1.  Message Centre Number
                            2.  Messages Sent as
                            3.  Messages Validity
                            0.  Back
                            """)
                            user_input_e = int(input("Press a Number: "))

                            if user_input_e == 0:
                                break

                    elif user_input_d == 2:
                        while True:
                            print("""
                            1.  Delivery Reports
                            2.  Reply Via Same Centre
                            3.  Character Support
                            0.  Back
                            """)

                            user_input_e = int(input("Press a number: "))
                            if user_input_e == 0:
                                break

    elif user_input == 3:
        while True:
            print("""1. Chat
                     0. Back
            """)

            user_input = int(input("Press a number: "))
            if user_input == 0:
                break

    elif user_input == 4:
        while True:
            print("""
            1.  Missed Calls
            2.  Received Calls
            3.  Dialed Numbers
            4.  Erase Recent Call Lists
            5.  Show Call Duration
            6.  Show Call Costs
            7.  Call Cost Settings
            8.  Prepaid Credit
            0.  Back
            """)
            user_input = int(input("Press a Number: "))
            if user_input == 0:
                break
            elif user_input == 5:
                while True:
                    print("""
                    1.  Last Call Duration
                    2.  All Calls' Duration
                    3.  Received Calls' Duration
                    4.  Dialed Calls' Duration
                    5.  Clear Timers
                    0.  Back
                    """)
                    user_input_one = int(input("Press a Number: "))
                    if user_input_one == 0:
                        break
            elif user_input == 6:
                while True:
                    print("""
                    1.  Last Call Cost
                    2.  All Calls' Cost
                    3.  Clear Counters
                    0.  Back
                    """)
                    user_input_one = int(input("Press a Number: "))
                    if user_input_one == 0:
                        break
            elif user_input == 7:
                while True:
                    print("""
                    1.  Call Cost Limit
                    2.  Show Costs in
                    0.  Back
                    """)
                    user_input_one = int(input("Press a Number: "))
                    if user_input_one == 0:
                        break
            elif user_input == 8:
                while True:
                    print("""1. Prepaid Credit
                             0. Back""")

    elif user_input == 5:
        while True:
            print("""
            1.  Ringing Tone
            2.  Ringing Volume
            3. Incoming call alert
            4. Composer
            5. Message alert tone
            6. Keypad tones
            7. Warning and game tones
            8. Vibrating alert
            9. Screen saver
            0.  Back
            """)
            user_input = int(input("Press a Number: "))

    elif user_input == 6:
        while True:
            print("""
            1.  Call Settings
            2.  Phone Settings
            3.  Security Settings
            4.  Restore Factory Settings
            0.  Back
            """)
            user_input = int(input("Press a Number: "))
            if user_input == 1:
                while True:
                    print("""
                    1.  Automatic Redial
                    2.  Speed Dialing
                    3.  Call Waiting Options
                    4.  Own Number Sending
                    5.  Phone line in use
                    6.  Automatic Answer
                    0.  Back
                    """)
                    user_input_one = int(input("Press a Number: "))
                    if user_input_one == 0:
                        break
            elif user_input == 2:
                while True:
                    print("""
                    1.  Language
                    2.  Cell Info Display
                    3.  Welcome Note
                    4.  Network Selection
                    5.  Lights
                    6.  Confirm SIM Service Actions
                    0.  Back
                    """)
                    user_input_one = int(input("Press a Number: "))
                    if user_input_one == 0:
                        break
            elif user_input == 3:
                while True:
                    print("""
                    1.  PIN Code Request
                    2.  Call Barring Service
                    3.  Fixed Dialing
                    4.  Closed User Group
                    5.  Phone Security
                    6.  Change Access Codes
                    0.  Back
                    """)
                    user_input_one = int(input("Press a Number: "))
                    if user_input_one == 0:
                        break
            elif user_input == 4:
                while True:
                    print("Restore Factory Settings")
            elif user_input == 0:
                break

    elif user_input == 7:
        while True:
            print("""1. Call Divert
                     0. Back
            """)
    elif user_input == 8:
        while True:
            print("""1. Games
                     0. Back
            """)
    elif user_input == 9:
        while True:
            print("""1. Calculator
                     0. Back
            """)
    elif user_input == 10:
        while True:
            print("""1. Reminders
                     0. Back
            """)
    elif user_input == 11:
        while True:
            print("""
            1.  Alarm Clock
            2.  Clock Settings
            3.  Date Setting
            4.  Stopwatch
            5.  Counter Timer
            6.  Auto Update of Date and Time
            0.  Back
            """)
            user_input = int(input("Press a Number: "))
            if user_input == 0:
                break
    elif user_input == 12:
        while True:
            print("""1. Profiles
                     0. Back
            """)
    elif user_input == 13:
        while True:
            print("""1. Sim Services
                     0.
            """)
    elif user_input == 0:
        break
    else:
        print("Invalid Input")

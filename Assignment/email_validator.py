import re

def email_validator(emails):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    for email in emails:
        if email.startswith('@') or email.count('@') > 1 or not re.match(pattern, email):
            print(f"{email} is not a valid email.")
        else:
            print(f"{email} is a valid email.")

emails_to_validate = ("example@email.com", "invalid.email", "no@dot", "short@do.t", "@invalid_start",
                      "invalid@@email.com", "valid@domain.c", "valid@domain.com")
email_validator(emails_to_validate)
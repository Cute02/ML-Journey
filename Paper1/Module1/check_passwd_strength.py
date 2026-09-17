#  Utility program: Password Strength Checker
def check_passwd_strength(passwd):
    if len(passwd) < 8:
        return "Weak"

    has_Upper = False
    has_Lower = False
    has_Digit = False
    has_chars = False
    Characters = "@!#$%^&*"
    for ch in passwd:
        if ch.isupper():
            has_Upper = True
        if ch.islower():
            has_Lower = True
        if ch.isdigit():
            has_Digit = True
        if ch in Characters:
            has_chars = True

    if has_Upper and has_Lower and has_Digit and has_chars:
        return "Strong"
    else:
        return "Moderate"


print(check_passwd_strength("abc23489&"))

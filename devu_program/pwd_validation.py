# WAP to validate a given password with below criteria:
#i) Password length must be 6 or more
 #   ii) It must contain at least one digit
  #  iii) It must contain at least one special character
   # iv) It must contain at least one UPPERCASE character.
    # v) It must begin with an alphabet.
def is_valid_password(p):
    dcount = splcount = ucount = 0
    for i in p:
        if i.isdigit():
            dcount = dcount+1
        if not i.isalnum():
            splcount = splcount+1
        if i.isupper():
            ucount = ucount+1

    if dcount>=1 and splcount >=1 and ucount >= 1 and len(p)>=6 and p[0].isalpha():
        return "Valid Password"
    return "invalid Password"
print(is_valid_password('Abc@12'))
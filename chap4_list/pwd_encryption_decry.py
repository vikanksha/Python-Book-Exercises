# Password encryption/Decryption Program.
pwd_out = ''
encryption_key = (('a','m'),('b','a'),('c','n'),('d','i'),('e','s'),('f','h'))
pwd = input('Enter (e) to encrypt and (d) to decrypt')
while pwd!='e' and pwd!='d':
    pwd = input("Invalid - Enter 'e' to encrypt and 'd' to decrypt")
encrypting = (pwd == 'e')
pwd_in = input("Enter a password :")
if encrypting:
    from_index = 0
    to_index = 1
else:
    from_index = 1
    to_index = 0
for ch in pwd_in:
    letter_found = False
    for k in encryption_key:
        if('a' <= ch and ch <= 'z') and ch == k[from_index]:
            pwd_out = pwd_out+k[to_index]
            letter_found  = True
    if not letter_found:
        pwd_out = pwd_out + ch
        
if encrypting:
    print('encrypted password' , pwd_out)
else:
    print('decrypted password' , pwd_out)
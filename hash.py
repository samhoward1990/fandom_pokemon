import hashlib
import os, binascii

def setPass(password, salt):
    hashedPW = hashlib.md5("{}{}".format(password, salt).encode()).hexdigest()
    return hashedPW

def setPassAgain(password, salt):
    hashedPW = hashlib.md5(f"{password}{salt}".encode()).hexdigest()
    return hashedPW

def setPassAgainButDifferent(password, salt):
    hashedPW = hashlib.md5("{}{}".format(password, salt).encode()).hexdigest()
    return hashedPW

def setSalt():
    return binascii.b2a_hex(os.urandom(15))

salt = setSalt()
passwordInfo = setPass("password", salt)
passwordFailer = setPassAgain("password", salt)
passwordMatcher = setPassAgainButDifferent("password", salt)

print(passwordInfo)
print(passwordMatcher)
print(passwordFailer)

print(passwordInfo == passwordMatcher)
print(passwordInfo == passwordFailer)



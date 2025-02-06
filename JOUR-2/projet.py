# codage Jule César
def c2n(string):
    string = string.upper()
    return [ord(letter) - 65 for letter in string]

def n2c(iterable_int):
    return ''.join([chr(index + 65) for index in iterable_int])

def decal(n, l):
    return [e+n if(e+n)<26 else e+n-26 for e in l]

def cesar(n, message):
    return n2c(decal(n, c2n(message)))

print(cesar(13,"BONJOUR"))

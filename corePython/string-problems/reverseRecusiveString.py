def recursiveString(string):
    if len(string)<1:
        return string
    return recursiveString(string[1:]) + string[0]

string = "hellovivek"
print(recursiveString(string))
    
def reverseStr(string):
    s = ''
    for i in string:
        s = i + s 
    return s 

res = reverseStr("vivek")
print(res)

string = "vina"
res = [string[i] for i in range(len(string)-1,-1,-1)]
print("list-comprheson", "".join(res))
        
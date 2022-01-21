def del_char(s,c):
    if len(c)==1:
        return s.replace(c, '')
    else:
        return s
s = input()
c = input()
print(del_char(s,c))
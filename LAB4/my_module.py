def UP (string):
    return (string.upper())
def DOWN(string):
    return (string.lower())
def dud (mn, mx):
    lst = []
    lst.append(mn)
    lst.append(mx)
    if mn == mx:
        return ('они равны')
    else:
        return max(lst)
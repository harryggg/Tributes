#a/b
#arbitary precision division
def division(a,b):
    """a will be divided by b"""
    """repeating cycle will be marked in ()"""

    remainder = int(a[0])
    b = int(b)
    result = ""
    nonzero = False
    for element in list(a)[1:]:
        
        if remainder//b!= 0:
            nonzero = True
        if nonzero:
            result += str(remainder//b)
        remainder = (remainder%b)*10 + int(element)
        
    result += str(remainder // b)
    remainder = remainder % b

    result += "."

    rlist = [remainder]
    while True:
        remainder = (remainder * 10) % b
        if remainder in rlist:break
        rlist.append(remainder)

    cursor = rlist.index(remainder)
    for i in range(len(rlist)):
        if cursor == i:
            result += "("
        result += str(rlist[i]*10//b)

    result += ")"
    return result
if __name__ == "__main__":
    a = input("a: ")
    b = input("b: ")
    print(division(a,b))

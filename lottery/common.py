__author__ = 'MyKings'

def filterTel(tel):
    result = ""
    if tel and len(tel)==11:
        for num in range(0, 11):
            if num > 2 and num <7:
                result += "*"
            else:
                result += tel[num]
    return result
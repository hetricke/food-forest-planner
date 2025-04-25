
def cleanInput(width, length):
    try:
        w = float(width)
        l = float(length)
        area = w * l
        return w, l
    except:
        raise Exception("Width and length must be numbers")

    return w, l

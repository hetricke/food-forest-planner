import plotly

def cleanInput(width, length):
    try:
        w = float(width)
        l = float(length)
        area = w * l

        if area <= 0 or w <=0 or l <= 0:
            raise Exception("Width and length must be postitive, non-zero numbers")
        
        return w, l
    except:
        raise Exception("Width and length must be postitive, non-zero numbers")

    return w, l

def plotGarden()
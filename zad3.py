
if __name__ == '__main__':
    with open("sygnaly.txt","r") as f:
        for line in f:
            maks = 0
            minimum = 255
            for i in list(line[:-1]):
                if ord(i) > maks:
                    maks = ord(i)
                if ord(i) < minimum:
                    minimum = ord(i)
                roz = maks-minimum
            if roz <= 10:
                print(line[:-1])


                

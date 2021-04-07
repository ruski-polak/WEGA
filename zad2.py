           
if __name__ == '__main__':
    maxs = 0
    slowo = ""
    with open("sygnaly.txt" , "r") as f:
        for line in f:
            slowa = [0]*255 # kod ascii
            for j in list(line[:-1]):
                slowa[ord(j)]+=1  # char -> kod ASCI
            ile = 0
            
            for j in slowa: 
                if j!=0:
                    ile+=1
            if maxs < ile:
                maxs = ile
                slowo = line

    print(maxs)
    print(slowo)
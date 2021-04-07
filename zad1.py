
            
if __name__ == '__main__':
    count = 0
    tmp = []
    with open("sygnaly.txt" , "r") as f:
        for line in f:
            a = line[:-1].split(" ")
            #### zad1
            for i in a:
                count+=1 
                if count % 40 == 0:
                    print(i[9], end=" ")
        
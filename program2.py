


#create a program that asks 3 numbers
def getNumber ():
    _first = int(input("First Number:"))
    _second = int(input("Second Number:"))
    _third = int(input("Third Number:"))
    return _first, _second, _third

first, second, third = getNumber()

#find the lowest number using only if-else statement
if first == second == third:    #equal lahat
    print ("All numbers are equal")
else: 
    if first == second and first < third:   #equal yung first at second
        print(f"{first} is the smallest number.")
    else:
        if first == second and first > third:
            print (f"{third} is the smallest number.")
        else:
            if second == third and second < first:     #equal yung second at third
                  print(f"{second} is the smallest number.")
            else:
                if second == third and second > first:
                    print (f"{first} is the smallest number.")
                else:
                    if first == third and first < second:   #equal yung first at third
                        print (f"{first} is the smallest number.")
                    else:
                        if first == third and first > second:
                            print(f"{second} is the smallest number.")
                        else:
                            if first < second and first < third:    #first ang smallest
                                print(f"{first} is the smallest number.")
                            else:
                                if second < first and second < third:   #second ang smallest
                                    print (f"{second} is the smallest number.")
                                else:
                                    if third < first and third < second:    #third and smallest
                                        print(f"{third} is the smallest number.")   #display the lowest number
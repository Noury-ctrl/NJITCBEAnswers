def cities(cityList):
    lst=[]   ### empty list
    i=0
    while True:
        city=cityList[i]   ### citylist[i] will be the corresponding city ex Citylist[0]="New York"
        i+=1               ### add 1 to i. i=1 but city does not change yet
        if city =="Newark":  ### if the city is Newark end the loop
            break
        lst.append(city)     ### add the city to the empty list
    return lst
lst=["New York", "Philadelphia","Newark","Baltimore"]
print(cities(lst))
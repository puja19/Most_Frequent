def most_frequent():
    str1 = input('Please enter a string ')
    #Counting frequecy of characters
    mydict={}
    for i in range(len(str1)):
        mydict[str1[i]]=str1.count(str1[i])
    #Printig the letters of str1 in decreasing order of requency
    def select_value(val):
        return val[1]
    print(sorted(mydict.items(),key=select_value, reverse=True))

most_frequent()


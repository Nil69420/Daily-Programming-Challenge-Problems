def decoding(digit, length) :

    count = [0] * (length+1) #storing counts in a list

    count[0] = 1
    count[1] = 1 

    for i in range(2, length+1) :
        
        count[i] = 0

        if digit[i-1] > '0' :
            count[i] = count[i-1]
         
        if (digit[i-2] == '1' or (digit [i-2] == '2' and digit[i-1] < '7')) :
            count[i] += count[i-2]
            
    return count[length]


digit = "1234"
n = len(digit)
print(decoding(digit, n)) 
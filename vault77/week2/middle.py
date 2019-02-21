number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def middle(number):
    if len(number) % 2 == 0:
        i = (int(len(number) / 2))
        a = (number[i] + number[i - 1]) / 2
        return a
    else:
        a = int(len(number) / 2)
        return(number[a])
        
    
print(middle(number))
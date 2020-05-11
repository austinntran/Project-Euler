def main():
    #variable to total result
    sum = 0

    #loop iterates from 0-999 inclusive
    for i in range(1000):

        #add to total only if a multiple of 3 or 5
        if i % 3 == 0 or i % 5 == 0:
            sum += i

    print(sum)

main()

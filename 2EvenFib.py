def main():
    a = 1
    b = 2
    sum = 0
    while a < 4000000:
        # print(a)
        tmp = b
        b = a + b
        a = tmp
        if a % 2 == 0:
            sum += a

    print(sum)


if __name__ == "__main__":
    main()
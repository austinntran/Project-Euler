def main():
    num = 20
    while True:
        flag = 0
        for i in range(20):
            if num % (i + 1) != 0:
                num += 2
                flag = 1
                break
        if flag == 1:
            continue
        break
    print(num)


if __name__ == "__main__":
    main()
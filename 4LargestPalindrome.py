def main():
    l = []
    for i in range(999, 1, -1):
        for j in range(999, 1, -1):
            s = str(i * j)
            p = ""
            for k in s:
                p = k + p
            if s == p:
                l.append(int(s))
    print(max(l))
if __name__ == "__main__":
    main()
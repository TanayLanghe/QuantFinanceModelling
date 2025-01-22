def main():
    with open('acc_data.txt', 'r') as file:
        lines = file.readlines()
    HC = []
    BP = []
    lineNum = 0
    for line in lines:
        lineNum = lineNum + 1
        values = line.split()
        if lineNum % 7 == 0:
            HC.append(values[7])
            BP.append(values[8])
    print(HC)
    print(BP)

if __name__ == '__main__':
    main()

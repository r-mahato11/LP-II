print("Enter n: ")
n = int(input())

b = [[0] * n for i in range(n)]

print(b)

# b = []
# for i in range(n):
# 	l = []
# 	for j in range(n):
# 		l.append(0)
# 	b.append(l)

# print(b)


def printBoard(b):
    print("$"*10)
    for i in b:
        print(i)
    print("$"*10)


def attack(i, j):
    for k in range(n):
        if b[i][k] == 1 or b[k][j] == 1:
            return True

    for p in range(n):
        for q in range(n):
            if p+q == i+j or p-q == i-j:
                if b[p][q] == 1:
                    return True

    return False


def nqueen(n):
    if n == 0:
        return True

    for i in range(N):
        for j in range(N):
            print(i, j, attack(i, j), n)
            if not attack(i, j) and b[i][j] != 1:
                b[i][j] = 1
                printBoard(b)

                if nqueen(n-1) == True:
                    return True

                b[i][j] = 0

    return False


nqueen(4)

printBoard(b)

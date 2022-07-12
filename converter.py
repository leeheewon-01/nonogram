X = int(input("넣어야 할 x의 개수 : "))
Y = int(input("넣어야 할 y의 개수 : "))
X_list = []
Y_list = []
print("X를 입력하시오.(enter로 묶음 구분)")
for i in range(X):
    X_list.append(list(map(int, input().split())))
print("Y를 입력하시오.(enter로 묶음 구분)\n Y는 위에서 부터 읽는 숫자를 입력해야 합니다!")
for j in range(Y):
    Y_list.append(list(map(int, input().split())))
X_alpha = ""
Y_alpha = ""

def num_to_alpha(num):
    list1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
             'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    return list1[num-1]
for k in X_list:
    for l in k:
        X_alpha += num_to_alpha(l)
    X_alpha += " "
for m in Y_list:
    for n in m:
        Y_alpha += num_to_alpha(n)
    Y_alpha += " "
print("X converter result :", X_alpha)
print("Y converter result :", Y_alpha)

f = open("D://VSC//nonogram//nonogram_problems.txt", 'w')
f.write(X_alpha)
f.write("\n")
f.write(Y_alpha)
f.close()
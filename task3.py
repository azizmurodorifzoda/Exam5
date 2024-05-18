a=input().split()
for i in a:
    if len(i)>5:
        for j in range(len(i)):
            print("#", end=" ")
    else:
        print("*", end=" ")
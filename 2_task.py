n=int(input("Введите количество кустов: "))
n_list=[]
for i in range(n):
    n_list.append(int(input()))
print(*n_list)

max_sum=0



for i in range(len(n_list)-1):
    if (n_list[i-1]+n_list[i]+n_list[i+1])>max_sum:
        max_sum=(n_list[i-1]+n_list[i]+n_list[i+1])
print(max_sum)
n = int(input("Введи кол-во элементов первого множества: "))
m = int(input("Введи кол-во элементов второго множества: "))
n_list = []
m_list = []
result_list=[]



for i in range(n):
    n_list.append(int(input()))
print(*n_list)
for i in range(m):
    m_list.append(int(input()))
print(*m_list)


    
for i in n_list:
    if m_list.count(i)>0 and not(i in result_list):
        result_list.append(i)
result_list.sort()
print(result_list)

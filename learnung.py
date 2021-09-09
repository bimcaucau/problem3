n = int(input())
list = map(int,input().split())
list_sorted = sorted(list,key=lambda x:abs(x))
list2 = []
list3 = []
list4 = []
list2_1 = []
list3_1 = []
list4_1 = []
for i in list_sorted:
    if i > 0 :
        list2.append(i)
    else: list2_1.append(i)
for k in list2:
    if k % 2 == 0:
        list4.append(k)
    else: list3.append(k)
for i in list2_1:
    if i%2 ==0:
        list4_1.append(i)
    else: list3_1.append(i)


list5_1 = list3+list3_1
list5_2 = list3+list4_1
list5_3 = list4+list3_1
list5_4 = list4+list4_1

a = len(list5_1)
b = len(list5_2)
c = len(list5_3)
d = len(list5_4)
final = [a,b,c,d]
print(max(final))




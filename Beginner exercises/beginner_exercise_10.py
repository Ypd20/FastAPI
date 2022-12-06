result_list=[]
list1=[10,20,25,30,35]
list2=[40,45,60,90]

for i in list1:
    if i%2!=0: 
        result_list.append(i)

for i in list2:
    if i%2==0:
        result_list.append(i)

print("result list:",result_list)
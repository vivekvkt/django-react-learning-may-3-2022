test_list = [(4, 5), (6, 7), (3, 6), (1, 2), (1, 8)]

# new_tuple=[]
# k=9
# for elm in  test_list:
#     if sum(elm)==k:
#         new_tuple.append(elm)

# tup=[]
# [tup.append(elm) for elm in test_list if sum(elm)==k]

# lst = [1,3,5,7,9]
# print("hello")
# l = len(lst)
# res_tup = []
# for i in range(len(lst)):
#    for j in range(i+1,len(lst)):
#         if lst[i] + lst[j]==8:
#             res_tup.append((lst[i],lst[j]))
# res1 = []    
# [res1.append((lst[i],lst[j])) for i in range(len(lst)) for j in range(i+1 , len(lst)) if lst[i] + lst[j]==8]
# print(res1)
   
     
#find the  sum of pair in list [] with given number 8   
lst = [1,3,5,7,9]  
hasmap = {}
s=8
for i in range(0,len(lst)):
    temp = s - lst[i] 
    if temp in hasmap:
        print(f"sum {s} is ({temp},{lst[i]})")
    hasmap[lst[i]]=i
    
  
      
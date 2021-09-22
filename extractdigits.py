my_list = [(67, 2), (34, 65), (212, 23), (17, 67), (18, )]

print("The list is : ")
print(my_list)

N = 2
print("The value of N is ")
print(N)
my_result = [sub for sub in my_list if all(len(str(ele)) == N for ele in sub)]

print("The extracted tuples are : " )
print(my_result)

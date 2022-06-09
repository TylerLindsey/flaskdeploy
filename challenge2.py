# given an array and int called target, find 2 indices that add up to the number of the target
# have an array 1,2,3,4
# tagret value is 6
# indices of where 2 and 4 is located, so the answer is 0 and 2 because it is 0 index
# exactly 1 combination of number and add up to the target
# cannot use the same element twice, like if the target was 6 you cannot use the 3 twice to make a value of 6, it has to be 2 and 4
# if  

# import numpy as sc
# # Numpy arrray with elements frrm 3 to 25
# num_arr = sc.arange(3, 25, 1)
# # To select those numbers which are divisible by 5
# new_arr = num_arr[num_arr%5==0]
# print(new_arr)


# x = indices[2]
# print(x)

# maybe a loop where it takes the first number and adds it to the second to see if it = the trget, and if not then to compare the 1st num to the 3d and if they do not equal the target then add 1 to 4, and once you reach the end, the 2nd num is compared to the 3d and then the 4th until it reaches the end and so on. The first time it gets the result it prints/returns it
# nested loop and it is a valid solution
# indices = [1,2,3,4]

# target = 6

# def add_num():
#   if indices[0]+indices[1]==target:
#     print(target)
#   elif indices[0]+indices[2]==target:
#     print(target)
#   elif indices[0]+indices[3]==target:
#     print(target)
#   elif indices[1]+indices[2]==target:
#     print(target)
#   elif indices[1]+indices[3]==target:
#     print(target)
#   elif indices[2]+indices[3]==target:
#     print(target)
#   else:
#     print('error')
    
    # this is the in squared class, worst case scenario run squared operation
my_list = [2, 5, 10, 20, 44, 32, 12, -45]

def two_sum(my_list, target):
  for i in range(len(my_list)):
    for j in range(i+1,len(my_list)):
      if my_list[i] + my_list[j] == target:
        return(i,j)

# this is the better solution because the altgorythm only goes through once, and doesnt have to loop through multiple times like the nestded loop does above
def one_pass(my_list, target):
  complement = {}
  for i in range(len(my_list)):
    num = my_list[i]
    comp = target - num
    complement[comp] = i
    if (complement.get(num) != None):
      return (complement.get(num), i)     
      
      # return (i, complement[comp])     
     
print(two_sum(my_list, 52))
print(two_sum(my_list, -33))

print(one_pass(my_list, 52))
print(one_pass(my_list, -33))

# create dictionary








# start with a solution and then optomize
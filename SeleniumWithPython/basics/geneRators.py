'''
Created on May 9, 2018

@author: kishlay.mishra
'''
# def square_numbers(num):
#     result=[]
#     for i in num:
#         result.append(i**2)
#     return result
#  
# my_nums=square_numbers([1,2,3,4,5])
# print(my_nums)

#===============================================

# def square_numbers(num):
#     for i in num:
#         yield(i**2)
# my_nums=square_numbers([1,2,3,4,5])
# print(my_nums)

#===============================================

# def square_numbers(num):
#     for i in num:
#         yield(i**2)
# my_nums=square_numbers([1,2,3,4,5])
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# #print(next(my_nums))

#===============================================

# my_nums=[x**2 for x in [1,2,3,4,5]]
# for num in my_nums:
#     print(num)
    
#===============================================

my_nums=(x**2 for x in [1,2,3,4,5])
print(my_nums)
for num in my_nums:
    print(num)
#  
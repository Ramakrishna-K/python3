# Map and Filter explaination 

# nums = [ 1,2,3,4]

# squared = list(map(lambda x: x**2, nums))
# even = list(filter(lambda x : x%2==0,nums))

# print(squared)
# print(even)


# name = ["hello",'ramakrisha','python']

# value =list(map(lambda x:x.upper(),name))
# print(value)

name = ["ho",'ramakrisha','python','ema','se']


long_word = list(filter(lambda x: len(x)>3 , name))
print(long_word)

nums = [2, 7, 4, 10, 1]
greater_than_5 = list(filter(lambda x: x > 5, nums))
print(greater_than_5)  # [7, 10]



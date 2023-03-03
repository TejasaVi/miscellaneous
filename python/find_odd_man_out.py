import pprint 

input_array = [1,2,3,4,3,4,2,1,5,8,8]

'''output= []'''
map_dict = {}
cnt = 0
for i in set(input_array):
    map_dict[i] = 0

for i in range(len(input_array)):
    map_dict[input_array[i]] = map_dict[input_array[i]] + 1

output = [ key for (key,val) in map_dict.items() if val == 1]
print(output)

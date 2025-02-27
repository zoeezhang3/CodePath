# def transpose(matrix):
#   result = []
#   for i in range(len(matrix)):
#     min_res = []
#     for j in range(len(matrix[0])):
#       min_res.append(matrix[j][i])
#     result.append(min_res)
#   return result

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# transpose(matrix)

# def reverse_list(lst):
#   left = 0
#   right = len(lst) - 1
#   result = []
  
#   while(left < right):
#     result.append(lst[right])
#     right -= 1
#   return result

# lst = ["pooh", "christopher robin", "piglet", "roo", "eeyore"]
# print(reverse_list(lst))

def remove_dupes(items):
    left = 0

    for right in range(1, len(items)):  # Move right pointer forward
      if items[right] != items[left]:  # If a new unique element is found
        left += 1  
        items[left] = items[right] 
    return items[:left+1]
  
items = ["extract of malt", "haycorns", "honey", "thistle", "thistle"]
print(remove_dupes(items))



# def is_balanced(code):
#     new_dict = {}
    
#     for char in code:
#       if char in new_dict:
#         new_dict[char] += 1
#       else:
#         new_dict[char] = 1
    
#     unique_val = set(new_dict.values())
    
#     if len(unique_val) == 1 or len(unique_val) > 2:
#       return False
#     else:
#       num1, num2 = unique_val
#       return abs(num1-num2) == 1
      
# code1 = "arghh"
# code2 = "haha"

# print(is_balanced(code1)) 
# print(is_balanced(code2)) 

# def find_treasure_indices(gold_amounts, target):
#   if len(gold_amounts) == 1:
#     if gold_amounts[0] == target:
#       return [0]
#     else:
#       return []
#   if len(gold_amounts) == 2:
#     if gold_amounts[0] + gold_amounts[1] == target:
#       return [0,1]
#     else:
#       return []
  
#   map = {}
#   res = []
#   for index, value in enumerate(gold_amounts):
#     rest_num = target - value
#     if rest_num in map:
#       res.append(map[rest_num])
#       res.append(index)
#     else:
#       map[value] = index
#   return res
       
  
# gold_amounts1 = [2, 7, 11, 15]
# target1 = 9

# gold_amounts2 = [3, 2, 4]
# target2 = 6

# gold_amounts3 = [3, 3]
# target3 = 6

# print(find_treasure_indices(gold_amounts1, target1))  
# print(find_treasure_indices(gold_amounts2, target2))  
# print(find_treasure_indices(gold_amounts3, target3)) 

from collections import Counter

def min_steps_to_match_maps(map1, map2):
    map1_dict = Counter(map1)
    map2_dict = Counter(map2)
    total_steps = 0
    
    for char in map1_dict:
      if char not in map2_dict:
        map2_dict[char] = 0
      if map1_dict[char] > map2_dict[char]:
        total_steps += map1_dict[char] - map2_dict[char]
    return total_steps

map1_1 = "bab"
map2_1 = "aba"
map1_2 = "treasure"
map2_2 = "huntgold"
map1_3 = "anagram"
map2_3 = "mangaar"

print(min_steps_to_match_maps(map1_1, map2_1))
print(min_steps_to_match_maps(map1_2, map2_2))
print(min_steps_to_match_maps(map1_3, map2_3))
# def filter_sustainable_brands(brands, criterion):
#   res = []
#   for brand in brands:
#     if criterion in brand['criteria']:
#       # if name == criterion:
#       res.append(brand['name'])
#   return res
          
# brands = [
#     {"name": "EcoWear", "criteria": ["eco-friendly", "ethical labor"]},
#     {"name": "FastFashion", "criteria": ["cheap materials", "fast production"]},
#     {"name": "GreenThreads", "criteria": ["eco-friendly", "carbon-neutral"]},
#     {"name": "TrendyStyle", "criteria": ["trendy designs"]}
# ]

# brands_2 = [
#     {"name": "Earthly", "criteria": ["ethical labor", "fair wages"]},
#     {"name": "FastStyle", "criteria": ["mass production"]},
#     {"name": "NatureWear", "criteria": ["eco-friendly"]},
#     {"name": "GreenFit", "criteria": ["recycled materials", "eco-friendly"]}
# ]

# brands_3 = [
#     {"name": "OrganicThreads", "criteria": ["organic cotton", "fair trade"]},
#     {"name": "GreenLife", "criteria": ["recycled materials", "carbon-neutral"]},
#     {"name": "FastCloth", "criteria": ["cheap production"]}
# ]

# print(filter_sustainable_brands(brands, "eco-friendly"))
# print(filter_sustainable_brands(brands_2, "ethical labor"))
# print(filter_sustainable_brands(brands_3, "carbon-neutral"))

# # time complexity O(n^2)
# # space complexity O(n)

from collections import Counter

# def count_material_usage(brands):
#   dict_material = {}
  
#   for brand in brands:
#     for material in brand['materials']:
#       if material in dict_material:
#         dict_material[material] += 1
#       else:
#         dict_material[material] = 1
#   return dict_material

# brands = [
#     {"name": "EcoWear", "materials": ["organic cotton", "recycled polyester"]},
#     {"name": "GreenThreads", "materials": ["organic cotton", "bamboo"]},
#     {"name": "SustainableStyle", "materials": ["bamboo", "recycled polyester"]}
# ]

# brands_2 = [
#     {"name": "NatureWear", "materials": ["hemp", "linen"]},
#     {"name": "Earthly", "materials": ["organic cotton", "hemp"]},
#     {"name": "GreenFit", "materials": ["linen", "recycled wool"]}
# ]

# brands_3 = [
#     {"name": "OrganicThreads", "materials": ["organic cotton"]},
#     {"name": "EcoFashion", "materials": ["recycled polyester", "hemp"]},
#     {"name": "GreenLife", "materials": ["recycled polyester", "bamboo"]}
# ]

# print(count_material_usage(brands))
# print(count_material_usage(brands_2))
# print(count_material_usage(brands_3))

# # time complexity O(n^2)
# # space complexity O(n)

# def find_trending_materials(brands):
#   res = set()
#   seen = set()
#   #  return list(seen)
#   for brand in brands:
#     for material in brand['materials']:
#       if material in seen:
#         res.add(material)
#       else:
#         seen.add(material)
#   return list(res)
  

# brands = [
#     {"name": "EcoWear", "materials": ["organic cotton", "recycled polyester"]},
#     {"name": "GreenThreads", "materials": ["organic cotton", "bamboo"]},
#     {"name": "SustainableStyle", "materials": ["bamboo", "recycled polyester"]}
# ]

# brands_2 = [
#     {"name": "NatureWear", "materials": ["hemp", "linen"]},
#     {"name": "Earthly", "materials": ["organic cotton", "hemp"]},
#     {"name": "GreenFit", "materials": ["linen", "recycled wool"]}
# ]

# brands_3 = [
#     {"name": "OrganicThreads", "materials": ["organic cotton"]},
#     {"name": "EcoFashion", "materials": ["recycled polyester", "hemp"]},
#     {"name": "GreenLife", "materials": ["recycled polyester", "bamboo"]}
# ]

# print(find_trending_materials(brands))
# print(find_trending_materials(brands_2))
# print(find_trending_materials(brands_3))

#  time complexity O(n^2)
#  space complexity O(n)  (check this answer later)

# problem 4
# def find_best_fabric_pair(fabrics, budget):
#   cost_list = []
#   closest_sum = 0
#   best_pair = ()
  
#   for fabric, cost in fabrics:
#     cost_list.append(cost)
  
#   left = 0
#   right = len(cost_list) - 1
#   cost_list = sorted(cost_list)
  
#   while left < right:
#     cost_sum = cost_list[left] + cost_list[right]
#     if cost_sum > closest_sum and cost_sum <= budget:
#       closest_sum = cost_sum
#       best_pair = (fabrics[left][0], fabrics[right][0])
#     if cost_sum > budget:
#       right -= 1
#     else:
#       left += 1
#   return best_pair
  
  
# fabrics = [("Organic Cotton", 30), ("Recycled Polyester", 20), ("Bamboo", 25), ("Hemp", 15)]
# fabrics_2 = [("Linen", 50), ("Recycled Wool", 40), ("Tencel", 30), ("Organic Cotton", 60)]
# fabrics_3 = [("Linen", 40), ("Hemp", 35), ("Recycled Polyester", 25), ("Bamboo", 20)]

# print(find_best_fabric_pair(fabrics, 45))
# print(find_best_fabric_pair(fabrics_2, 70))
# print(find_best_fabric_pair(fabrics_3, 60))

# problem 5
def organize_fabrics(fabrics):
  fabrics.sort(key=lambda x: x[1])
  stack = []
  
  for fabric in fabrics:
    stack.append(fabric[0])
  
  res = []
  while stack:
    res.append(stack.pop())
    
  return res
  

fabrics = [("Organic Cotton", 8), ("Recycled Polyester", 6), ("Bamboo", 7), ("Hemp", 9)]
fabrics_2 = [("Linen", 5), ("Recycled Wool", 9), ("Tencel", 7), ("Organic Cotton", 6)]
fabrics_3 = [("Linen", 4), ("Hemp", 8), ("Recycled Polyester", 5), ("Bamboo", 7)]

print(organize_fabrics(fabrics))
print(organize_fabrics(fabrics_2))
print(organize_fabrics(fabrics_3))

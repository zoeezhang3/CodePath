from collections import Counter, defaultdict
from itertools import combinations


def find_balanced_subsequence(art_pieces):
  if not art_pieces:
    return 0
  
  count = Counter(art_pieces)
  print(count)
  max_length = 0
  for key in count:
    if key+1 in count:
      max_length = max(max_length, count[key]+count[key+1])

  return max_length

art_pieces1 = [1,3,2,2,5,2,3,7]
art_pieces2 = [1,2,3,4]
art_pieces3 = [1,1,1,1]

# print(find_balanced_subsequence(art_pieces1))
# print(find_balanced_subsequence(art_pieces2))
# print(find_balanced_subsequence(art_pieces3))

def is_authentic_collection(art_pieces):
  if not art_pieces:
    return False
  
  max_num = max(art_pieces)
  
  if len(art_pieces) != max_num+1:
    return False
  
  count = Counter(art_pieces)
  
  for i in range(1, max_num):
    if count[i] != 1:
      return False
  
  return count[max_num] == 2

collection1 = [2, 1, 3]
collection2 = [1, 3, 3, 2]
collection3 = [1, 1]

# print(is_authentic_collection(collection1))
# print(is_authentic_collection(collection2))
# print(is_authentic_collection(collection3))

def organize_exhibition(collection):
  count_dict = Counter(collection)
  two_d_arr = []
  
  while any(count_dict.values()):       # the loop will stop when all the values are 0
    two_d_arr_row = []
    for key in count_dict:
      if count_dict[key] > 0:
        two_d_arr_row.append(key)
        count_dict[key] -= 1
    two_d_arr.append(two_d_arr_row)
      
  return two_d_arr
    
collection1 = ["O'Keefe", "Kahlo", "Picasso", "O'Keefe", "Warhol", "Kahlo", "O'Keefe"]
collection2 = ["Kusama", "Monet", "Ofili", "Banksy"]

# print(organize_exhibition(collection1))
# print(organize_exhibition(collection2))


# Problem 4: Gallery Subdomain Traffic
def subdomain_visits(cpdomains):
  visit_counts = defaultdict(int)
  
  for item in cpdomains:
    arr = item.split(' ')
    count = int(arr[0])
    domains = arr[1].split(".")
    
    for i in range(len(domains)):
      subdomain = ".".join(domains[i:])
      visit_counts[subdomain] += count
      
  result = []
  for key, val in visit_counts.items():
    item = [val, key]
    result.append(item)
  return result  

cpdomains1 = ["9001 modern.artmuseum.com"]
cpdomains2 = ["900 abstract.gallery.com", "50 impressionism.com", 
              "1 contemporary.gallery.com", "5 medieval.org"]

# print(subdomain_visits(cpdomains1))
# print(subdomain_visits(cpdomains2))

def beauty_sum(collection):
  total_beauty = 0
  # collection = "aabcb"
  
  for i in range(len(collection)):
    # i = 0
    # i = 1
    b_dict = Counter()
    for r in range(i, len(collection)):
      # r = 0, 1, 2, 3, 4
      # r = 1, 2, 3, 4
      char = collection[r]
      b_dict[char] += 1
      sub_sum = max(b_dict.values()) - min(b_dict.values())
      total_beauty += sub_sum
      
    return total_beauty 

# print(beauty_sum("aabcb")) 
# print(beauty_sum("aabcbaa"))

# Problem 6: Counting Divisible Collections in the Gallery
def count_divisible_collections(collection_sizes, k):
    count = 0
    
    for i in range(len(collection_sizes)):
      total = 0
      for j in range(i, len(collection_sizes)):
        total += collection_sizes[j]
        if total%k == 0:
          count+=1
          
    return count

nums1 = [4, 5, 0, -2, -3, 1]
k1 = 5
nums2 = [5]
k2 = 9

print(count_divisible_collections(nums1, k1))  
print(count_divisible_collections(nums2, k2)) 

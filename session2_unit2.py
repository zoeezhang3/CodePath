from collections import Counter


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

print(find_balanced_subsequence(art_pieces1))
print(find_balanced_subsequence(art_pieces2))
print(find_balanced_subsequence(art_pieces3))

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

print(is_authentic_collection(collection1))
print(is_authentic_collection(collection2))
print(is_authentic_collection(collection3))

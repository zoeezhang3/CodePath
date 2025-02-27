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

# print(find_balanced_subsequence(art_pieces1))
# print(find_balanced_subsequence(art_pieces2))
# print(find_balanced_subsequence(art_pieces3))



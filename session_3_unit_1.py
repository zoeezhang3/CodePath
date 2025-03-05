#  problem 1
#  problem 3
def arrange_attendees_by_priority(attendees, priority):
  # less_than = [x for x in attendees if x < priority]
  # equal_to = [x for x in attendees if x == priority]
  # greater_than = [x for x in attendees if x > priority]
  # return less_than + equal_to + greater_than
  
  low, mid, high = 0, 0, len(attendees)-1
  #  low for mark the element as the lowest, keep it in the left
  
  while mid <= high:
    if attendees[mid] < priority:
      attendees[low], attendees[mid] = attendees[mid], attendees[low]
      low += 1
      mid += 1
    elif attendees[mid] > attendees[high]:
      attendees[mid], attendees[high] = attendees[high], attendees[mid]
      high -= 1
    else: 
      mid += 1  
  return attendees
      

print(arrange_attendees_by_priority([9,12,5,10,14,3,10], 10)) 
print(arrange_attendees_by_priority([-3,4,3,2], 2)) 
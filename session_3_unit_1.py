# problem 1
def arrange_guest_arrival_order(arrival_pattern):
  guest_order = []
  stack = []
  
  for i in range(len(arrival_pattern)+1):
    stack.append(str(i+1))
    if i == len(arrival_pattern) or arrival_pattern[i] == 'I':
      while stack:
        guest_order.append(stack.pop())
  
  return ''.join(guest_order)

print(arrange_guest_arrival_order("IIIDIDDD"))  
print(arrange_guest_arrival_order("DDD")) 

from collections import deque 

# problem 2
def reveal_attendee_list_in_order(attendees):
  attendees.sort(reverse=True)  # Sort in descending order (process largest first)
  queue = deque()

  for num in attendees:
      if queue:
          queue.appendleft(queue.pop())  # Simulate moving last element to front
      queue.appendleft(num)  # Insert current number at the front

  return list(queue)  # Convert deque to list

print(reveal_attendee_list_in_order([17,13,11,2,3,5,7])) 
print(reveal_attendee_list_in_order([1,1000])) 


# problem 3
def arrange_attendees_by_priority(attendees, priority):
  # less_than = [x for x in attendees if x < priority]
  # equal_to = [x for x in attendees if x == priority]
  # greater_than = [x for x in attendees if x > priority]
  # return less_than + equal_to + greater_than
  
  low, mid, high = 0, 0, len(attendees)-1
  #  low for mark the element as the lowest, keep it in the left
  
  while mid <= high:
    if attendees[mid] < priority:
      attendees.insert(low, attendees.pop(mid))
      low += 1
      mid += 1
    elif attendees[mid] > priority:
      attendees.append(attendees.pop(mid))
      high -= 1
    else: 
      mid += 1  
  return attendees
      

# print(arrange_attendees_by_priority([9,12,5,10,14,3,10], 10)) 
# print(arrange_attendees_by_priority([-3,4,3,2], 2)) 

# problem 4
def rearrange_guests(guests):
  positive = [x for x in guests if x > 0]
  negative = [x for x in guests if x < 0]
  
  res = []
  i = 0
  
  while i < len(positive):
    res.append(positive[i])
    res.append(negative[i])
    i+=1
  return res
  
# print(rearrange_guests([3,1,-2,-5,2,-4]))  
# print(rearrange_guests([-1,1])) 

# problem 5
def min_changes_to_make_balanced(schedule):
  stack = []
  close_needed = 0
  
  for item in schedule:
    if item == "(":
      stack.append(item)
    else:
      if stack:
        stack.pop()
      else:
        close_needed += 1
  return len(stack) + close_needed
    
# print(min_changes_to_make_balanced("()))))))"))
# print(min_changes_to_make_balanced("((((((()))))))))")) 

# problem 6

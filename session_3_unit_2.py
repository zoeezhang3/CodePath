from collections import deque

def blueprint_approval(blueprints):
  blueprints.sort()
  queue = deque(blueprints)
    
  approval_order = []
  while queue:
    approval_order.append(queue.popleft())
  
  return approval_order      

print(blueprint_approval([3, 5, 2, 1, 4])) 
print(blueprint_approval([7, 4, 6, 2, 5])) 


# problem 4 - The minimum swaps required is half of the maximum extra ] encountered.
def min_swaps(s):
  max_imbalance = 0
  extra_close = 0
    
  for item in s:
    if item == "[":
      extra_close -= 1
    else: 
      extra_close += 1
      max_imbalance = max(max_imbalance, extra_close)
  return (max_imbalance + 1)//2

print(min_swaps("][][")) 
print(min_swaps("]]][[[")) 
print(min_swaps("[]")) 

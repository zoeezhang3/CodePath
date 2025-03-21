# Advance 2
# Problem 4

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def middle_match(head, val):
    slow = head
    fast = head
    
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
    return slow.value == val
  
kart_choices = Node("Bullet Bike", Node("Wild Wing", Node("Pirahna Prowler")))
tournament_tracks = Node("Rainbow Road", Node("Bowser Castle", Node("Sherbet Land", Node("Yoshi Valley"))))

# print(middle_match(kart_choices, "Wild Wing"))
# print(middle_match(tournament_tracks, "Bowser Castle"))

# problem 5

# For testing
def reverse(head):
  curr = head
  prev = None
  
  while curr:
    temp = curr.next
    curr.next = prev
    prev = curr
    curr = temp
  return prev

kart_choices = Node("Bullet Bike", Node("Wild Wing", Node("Pirahna Prowler")))
print(reverse(kart_choices))

#  problem 6
def is_symmetric(head):
  if head is None or head.next is None:
    return True
  
  # find the middle node of the list, slow is the middle node
  slow = fast = head
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

  #  reverse the second half of the list, after reserve, prev will become the middle node
  prev = None
  while slow:
    temp = slow.next
    slow.next = prev
    prev = slow
    slow = temp
    
  # lastly compare the first half and the reversed second half
  left, right = head, prev
  while right:
    if left.value != right.value:
      return False
    left = left.next
    right = right.next
  return True
    
head1 = Node("Bitterling", Node("Crawfish", Node("Bitterling")))
head2 = Node("Bitterling", Node("Carp", Node("Koi")))

print(is_symmetric(head1))
print(is_symmetric(head2))

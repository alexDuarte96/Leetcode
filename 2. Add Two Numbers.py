#Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
      self.val = val
      self.next = next

  def listPrint(self):
    current = self
    while current is not None:
      print(current.val,end=",")
      current = current.next

def add(nList, newVal):
  q = None
  p = nList

  while p is not None:
    q = p
    p = p.next

  q.next = ListNode(val = newVal)

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
  listN = ListNode()
  num1 = 0
  num2 = 0
  n = 0
  
  power = 1
  node1 = l1
  while node1 is not None:
      num1 += node1.val * power
      power *= 10
      node1 = node1.next
      
  power = 1
  node2 = l2
  while node2 is not None:
      num2 += node2.val * power
      power *= 10
      node2 = node2.next

  print(f"[1]:{num1} - [2]:{num2}")    
  
  n = num1 + num2
  while n>0:
      listN.next = ListNode(val = n%10)
      listN = listN.next
      n/=10
  
  return listN

# Test
list1 = ListNode(val=2)
add(list1,4)
add(list1,3)
list1.listPrint()

print()

list2 = ListNode(val=5)
add(list2,6)
add(list2,4)
list2.listPrint()

print()

addTwoNumbers(list1,list2)

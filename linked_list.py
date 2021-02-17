# person_vs_comet.py
from pydantic import BaseModel
from typing import Optional,Any

class ListNode(BaseModel):
    val:int 
    next:Any

def get_list_from_linked_list(p):
    list_from_linked_list = []
    while True:
        list_from_linked_list.append(p.val)
        p=p.next
        if p is None:
            break   
    return list_from_linked_list

def get_linked_list_from_list(A):
    prev = ListNode(val=A[-1],next=None)
    if len(A)<2:
      return prev
    for i,v in enumerate(A[-2::-1]):
        cur = ListNode(val=v,next=prev)
        prev = cur
    return cur

class Solution():
    def swapPairs(self, A):
        index = 2 
        n_3 = None
        if A is not None and A.next is not None:
          n_2 = A
          n_1 = A.next

        else:
          return A
        cur = A.next.next 
        head = n_1 
        while True:            
            print(f"Index {index} cur_val {cur.val if cur is not None else 'End'}")
            if index%2==0:
                print(f"Its time for a switch,current")
                n_2.next=cur
                n_1.next=n_2
                if n_3 is not None:
                  # IF YOU DON,T DO THIS SWITCH, YOU WILL SKIP n_1 AS NOBODY WILL POINT TO IT :(
                  n_3.next = n_1 
            if cur is None:
              break
            print(get_list_from_linked_list(head))
            if index%2==0:
              n_3=n_1
              n_2=n_2
            else:
              n_3=n_2
              n_2=n_1
            n_1=cur
            cur=cur.next
            index+=1
        return head 


A=[1,2,3,4,5,6]

A=[1,2]
A=[1]
p=get_linked_list_from_list(A)
print(p)
sol = Solution()  
res=sol.swapPairs(p)
swapped_list_from_linked_list = get_list_from_linked_list(res)

print(swapped_list_from_linked_list)
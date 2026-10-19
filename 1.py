class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev

#на каждом шаге менем направление одной ссылки, в итоге получаем указатель на голову нового списка
#Проходим по списку 1 раз, т.е. O(n)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def delete_node(head, val):
    if head is None:
        return None

    if head.val == val:
        return head.next

    curr = head

    while curr.next:
        if curr.next.val == val:
            curr.next = curr.next.next
            return head

        curr = curr.next

    return head

#Если удаляется голова - возвращаем следующий узел
#если удаляется внтуренний узел - сдвигаем указатель
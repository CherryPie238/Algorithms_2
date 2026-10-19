class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def merge_two_lists(list1, list2):
    if not list1:
        return list2

    if not list2:
        return list1

    if list1.val <= list2.val:
        head = list1
        list1 = list1.next
    else:
        head = list2
        list2 = list2.next

    curr = head

    while list1 and list2:
        if list1.val <= list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next

        curr = curr.next

    if list1:
        curr.next = list1
    else:
        curr.next = list2

    return head

#Каждый узел первого списка обрабатывается не более одного раза O(n).
#у второго списка O(m).
#когда один из списков заканчивается, оставшаяся часть другого присоединяется одной операцией изменения ссылки, т.е. O(n+m)
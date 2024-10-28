class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    values = set()
    current = llist_1.head
    while current:
        values.add(current.value)
        current = current.next

    current = llist_2.head
    while current:
        values.add(current.value)
        current = current.next

    union_list = LinkedList()
    for value in values:
        union_list.append(value)

    return union_list


def intersection(llist_1, llist_2):
    values_1 = set()
    values_2 = set()
    current = llist_1.head
    while current:
        values_1.add(current.value)
        current = current.next

    current = llist_2.head
    while current:
        if current.value in values_1:
            values_2.add(current.value)
        current = current.next

    intersection_list = LinkedList()
    for value in values_2:
        intersection_list.append(value)

    return intersection_list

# Test Case 1: Basic Union and Intersection
llist_1 = LinkedList()
llist_1.append(1)
llist_1.append(2)
llist_1.append(3)

llist_2 = LinkedList()
llist_2.append(3)
llist_2.append(4)
llist_2.append(5)

union_result_1 = union(llist_1, llist_2)
intersection_result_1 = intersection(llist_1, llist_2)
print("Test Case 1:")
print("Union:", union_result_1)
print("Intersection:", intersection_result_1)
print()

# Test Case 2: Duplicate Values
llist_3 = LinkedList()
llist_3.append(1)
llist_3.append(2)
llist_3.append(2)
llist_3.append(3)

llist_4 = LinkedList()
llist_4.append(2)
llist_4.append(3)
llist_4.append(3)
llist_4.append(4)

union_result_2 = union(llist_3, llist_4)
intersection_result_2 = intersection(llist_3, llist_4)
print("Test Case 2:")
print("Union:", union_result_2)
print("Intersection:", intersection_result_2)
print()

# Test Case 3: Edge Case - Empty Lists
llist_5 = LinkedList()  # empty list
llist_6 = LinkedList()  # empty list

union_result_3 = union(llist_5, llist_6)
intersection_result_3 = intersection(llist_5, llist_6)
print("Test Case 3:")
print("Union:", union_result_3)
print("Intersection:", intersection_result_3)
print()


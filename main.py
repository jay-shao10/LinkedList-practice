from Linkedlist import LinkedList

list1 = LinkedList()
list1.add_list_item(2)
list1.add_list_item(7)
list1.add_list_item(11)
list1.add_list_item(7)
list1.print_list()
print(list1.search(7))
list1.remove_list_item_by_id(1)
list1.print_list()
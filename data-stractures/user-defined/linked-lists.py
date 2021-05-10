class Node(object):
    def __init__(self, data=None, next_node=Node):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        current = self.head
        count = 0

        while current:
            count += 1

            print(current.get_data())

            current = current.get_next()

        print('The size of linked list is ', count)


    def search(self, data):
        current =  self.head
        found = False

        while current and found is False:
            if current.get_data() == data:
                found = True

            else:
                current = current.get_next()

        if current is None:
            raise ValueError("Data not in list")

        return found

    def delete(self, data):
        current = self.head
        previous = None
        found = False

        while current and found is False:
            if current.get_data() == data:
                found = True

            else:
                previous = current
                current = current.get_next()

        if current is None:
            raise ValueError("Data not in list")

        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())


11 = LinkedList()
11.insert(1)
11.insert(2)
11.insert(3)
11.size()

val = 11.search(1)
if val:
    print('Value is Found.')

11.delete(1)
11.size()

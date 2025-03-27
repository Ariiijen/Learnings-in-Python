class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, iterable=None):
        self.head = None
        if iterable:
            self.from_iterable(iterable)
    
    def from_iterable(self, iterable):
        if isinstance(iterable, (list, tuple, set, str, dict)):
            for item in iterable:
                self.append(item)
        else:
            raise TypeError("Unsupported data structure")
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        return elements
    
    def to_list(self):
        return self.display()
    
    def to_tuple(self):
        return tuple(self.display())
    
    def to_set(self):
        return set(self.display())
    
    def to_string(self):
        return ''.join(str(item) for item in self.display())
    
    def to_dict(self):
        elements = self.display()
        if len(elements) % 2 != 0:
            raise ValueError("Cannot convert to dictionary, odd number of elements")
        return dict(zip(elements[::2], elements[1::2]))

if __name__ == "__main__":
    ll = LinkedList([5, 4, 7, 6])
    print("LinkedList contents:", ll.display())
    print("Converted to tuple:", ll.to_tuple())
    print("Converted to set:", ll.to_set())
    print("Converted to string:", ll.to_string())

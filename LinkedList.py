class LinkedList:
    class Node:
        def __init__(self, value, link_next, link_prev):
            self.value = value
            self.link_next = link_next
            self.link_prev = link_prev

        def __repr__(self):
            return str(self.value)

    def __init__(self):
        self.head = None

    def get_last(self):
        element = self.head

        if not element:
            return None

        while element.link_next:
            element = element.link_next

        return element

    def __iadd__(self, other):
        last_element = self.get_last()
        new_node = self.Node(other, None, last_element)

        if last_element:
            last_element.link_next = new_node
        else:
            self.head = new_node

        return self

    def __iter__(self):
        element = self.head

        if not element:
            return None

        while element.link_next:
            yield element
            element = element.link_next
        yield element

    def __repr__(self):
        objects = ""

        for el in self:
            objects += str(el.value) + " -> "

        return objects

    def insert(self, other, position):
        if position < 0:
            raise IndexError

        new_node = self.Node(other, None, None)

        if position == 0:
            new_node.link_next = self.head.link_next
            new_node.link_prev = self.head

            self.head.next_link = new_node
            return

        new_node.link_next = self[position - 1].link_next
        new_node.link_prev = self[position + 1].link_prev

        self[position - 1].link_next = new_node
        self[position + 1].link_prev = new_node

    def __getitem__(self, item):
        element = self.head
        i = 0

        if item < 0:
            raise IndexError()

        if not element:
            return IndexError()

        while element.link_next:
            if i == item:
                return element

            element = element.link_next
            i += 1

        if i == item:
            return element

        raise IndexError()


if __name__ == '__main__':
    ls = LinkedList()

    for i in range(100):
        ls += i

    ls.insert("hello!", 10)
    print(ls[10])

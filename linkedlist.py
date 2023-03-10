# create the circular linked list
class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
class CircularLinkedList:
    def __init__ (self,size):
        self.size = size
        self.head = None
        self.tail = None
        self.current = None
        self.create()
    # Create the list
    def create(self):
        for i in range(1,self.size + 1):
            node = Node(i)
            if self.head == None:
                self.head = node
                self.tail = node
                self.current = node
            else:
                self.tail.next = node
                self.tail = node
                self.tail.next = self.head

    #Traverse the list
    def traverse(self,k):
        for i in range (1,self.size):
            for j in range(1,k):
                self.current = self.current.next

            print("Person ", self.current)
        #Get the person to be killed
        self.current = self.current.next
        print("Person ", self.current.next , "is killed")
        # Remove the killed person
        self.current.prev.next = self.current.next
        self.current.next.prev = self.current.prev

        # Move the current pointer
        self.current = self.current.next

        # Repeat the process
        self.traverse(k)
def josephus(people, skip):
    people_list = list(range(1, people + 1))
    index = skip - 1
    while len(people_list) > 1:
        print("Person %d is killed" % people_list.pop(index))
        index = (index + skip - 1) % len(people_list)
    print("The last survivor is Person %d" % people_list[0])
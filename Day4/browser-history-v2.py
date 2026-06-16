# Simulate a browser's navigation using two stacks and a queue:
 
# Every visit() pushes URL onto back stack 
# back() pops from back stack → pushes to forward stack 
# forward() pops from forward stack → pushes to back stack 
# A deque queue keeps the full chronological history log 

from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.top = None

    def push(self, url):
        new_node = Node(url)

        new_node.next = self.top

        self.top = new_node

    def pop(self):

        if self.is_empty():
            return None
        
        removed = self.top.data
        self.top = self.top.next

        return removed
    
    def is_empty(self):
        return self.top is None
    
    def display(self):

        temp = self.top
        result = []

        while temp:
            result.append(temp.data)
            temp = temp.next
        return result

class Browser():

    def __init__(self):

        self.back_stack = Stack()
        self.forward_stack = Stack()
        self.history_log = deque()
        self.current = None

    def visit(self, url):

        if self.current:
            self.back_stack.push(self.current)

        self.current = url

        self.forward_stack = Stack()
        self.history_log.append(url)

        print(f"Visited: {url}")

    def back(self):

        if self.back_stack.is_empty():
            print("Nothing to go back to")
            return
        
        self.forward_stack.push(self.current)     
        self.current = self.back_stack.pop()

        print()
        print(f"Back -> {self.current}")

    def forward(self):

        if self.forward_stack.is_empty():
            print("Nothing to go forward to")
            return
        
        self.back_stack.push(self.current)

        self.current = self.forward_stack.pop()

        print()
        print(f"Forward -> {self.current}")

    def show_history(self):

        print("History:")

        for site in self.history_log:
            print(site, end = "->")

        print()
        print(f"Current: {self.current}")

    def search_history(self, keyword):

        search_result = []

        for site in self.history_log:
            if keyword in site:
                search_result.append(site)
        
        return search_result

def main():
    b = Browser()

    b.visit("google.com")
    b.visit("youtube.com")
    b.visit("github.com")

    b.back()
    b.back()

    b.forward()

    b.visit("stackoverflow.com")

    b.show_history()

    print()
    print("Search:", b.search_history("ub"))


if __name__ == "__main__":
    main()


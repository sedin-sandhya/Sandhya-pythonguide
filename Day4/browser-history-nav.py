# Simulate a browser's navigation using two stacks and a queue:
 
# Every visit() pushes URL onto back stack 
# back() pops from back stack → pushes to forward stack 
# forward() pops from forward stack → pushes to back stack 
# A deque queue keeps the full chronological history log 

from collections import deque
class Browser():

    def __init__(self):

        self.back_stack = []
        self.forward_stack = []
        self.history_log = deque()
        self.current = None

    def visit(self, url):

        if self.current:
            self.back_stack.append(self.current)

        self.current = url

        self.forward_stack.clear()
        self.history_log.append(url)

        print(self.back_stack)
        print(f"Visited: {url}")

    def back(self):

        if not self.back_stack:
            print("Nothing to go back to")
            return
        
        self.forward_stack.append(self.current)     
        self.current = self.back_stack.pop()

        print()
        print(f"Back -> {self.current}")

    def forward(self):

        if not self.forward_stack:
            print("Nothing to go forward to")
            return
        
        self.back_stack.append(self.current)

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

    # google.com->youtube.com->github.com->youtube.com->google.comstackoverflow.com->
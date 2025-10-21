class DNode:
    def __init__(self, url):
        self.url = url
        self.next = None
        self.prev = None

class BrowserHistory:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None

    def visit(self, url):               # Visit new page (Add to end, set as current)
        new_page = DNode(url)

        if self.head is None:               # For an Empty list
            self.head = new_page            # Make it head
            self.tail = new_page            # And tail
            self.current = new_page
            return

        self.tail.next = new_page           # add pointer on tail to point to new node
        new_page.prev = self.tail           # add pointer to front of new node to point at tail
        self.tail = new_page                # now the new node is officially the tail
        self.current = new_page
    
    def back(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
            return self.current.url
        return "Can't go back"
    
    def forward(self):
        if self.current and self.current.next:
            self.current = self.current.next
            return self.current.url
        return "Can't go forward"

    def current_page(self):                 # Show current url
        return self.current.url

# Test
browser = BrowserHistory()
browser.visit("google.com")
browser.visit("youtube.com")
browser.visit("github.com")
print(browser.current_page())  # github.com

browser.back()
print(browser.current_page())  # youtube.com

browser.back()
print(browser.current_page())  # google.com

browser.forward()
print(browser.current_page())  # youtube.com
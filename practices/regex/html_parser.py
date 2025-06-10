from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs): 
        print("Start :", tag)
        for a in attrs:
            print("->", a[0], ">", a[1]) 

    def handle_endtag(self, tag): 
        print("End   :", tag) 

    def handle_startendtag(self, tag, attrs):
        print ('Empty :',tag)
        for ele in attrs:
            print ('->',ele[0],'>',ele[1])

parser = MyHTMLParser()

# parser.feed('<html><head><title>HTML Parser - I</title></head>' 
#             '<body data-modal-target class="1"><h1>HackerRank</h1><br /></body></html>'
#             '<!-- Comments -->'
#             '<img src="https://www.hackerrank.com/favicon.ico" />'
#             '<input type="text" />'
#             '<a href="https://www.hackerrank.com">HackerRank</a>')

int = int(input())
for _ in range(int):
    parser.feed(input())
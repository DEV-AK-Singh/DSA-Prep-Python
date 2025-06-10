from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):  
    def handle_starttag(self, tag, attrs): 
        print(tag)
        for a in attrs:
            print("->", a[0], ">", a[1]) 
    
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()
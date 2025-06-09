# import re

# html = """
# <head>
# <title>HTML</title>
# </head>
# <object type="application/x-flash" 
#   data="your-file.swf" 
#   width="0" height="0">
#   <!-- <param name="movie"  value="your-file.swf" /> -->
#   <!-- <param name="movie"  value="your-file.swf" /> -->
#   <!-- <param name="movie"  value="your-file.swf" /> -->
#   <param name="quality" value="high"/>
# </object>
# """
# def test(match): 
#     return re.findall(r"<!--(.*)-->", match.group())[0] 

# print(re.sub("(<!--.*-->)", test, html))

import re

n = int(input())
for _ in range(n):
    line = str(input())
    commented_line = re.findall(r"^#{1}(.*)", line)
    filtered_line = re.findall(r"^(?!#).*", line) 
    if len(filtered_line) > 0:  
        substituted_or = re.sub(r"\s+(\|\|){1}\s+", " or ", filtered_line[0])
        substituted_and = re.sub(r"\s+(&&){1}\s+", " and ", substituted_or)
        print(substituted_and)
    if len(commented_line) > 0:
        print(line)
        continue 
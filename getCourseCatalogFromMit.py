from bs4 import BeautifulSoup
import requests
import sys

json_data = {}
url = "http://catalog.mit.edu/subjects/"

arg = sys.argv[1]
url+=arg+"/"
#url = "http://catalog.mit.edu/subjects/18/"
page = requests.get(url)

soup = BeautifulSoup(page.content,"html.parser")

page_title = soup.find(class_="page-title")
json_data['page-title'] = page_title.text

#print(soup.prettify())
body = soup.body
#print(body.prettify())
page_content = body.find("div", id="page-content")
right_col = page_content.find("div",id="right-col")
content = right_col.find("div",id="content")
page_title = content.find("h1",class_="page-title")
print("Title : ",page_title.text)

coursestextcontainer = content.find("div",id="coursestextcontainer")
#print(coursestextcontainer.prettify())
sc_sccoursedescs = body.find("div",id="sc_sccoursedescs")

#section_head = sc_sccoursedescs.find("div",class_="sectionhead")
#print("   Section Head : ",section_head.text)
#print(sc_sccoursedescs.prettify())
courseblocks = sc_sccoursedescs.find_all("div", class_="courseblock")

print(len(courseblocks))

for courseblock in courseblocks:
    course_title = courseblock.find("h4", class_="courseblocktitle")
    strong = course_title.span.strong
    print("Title : ",strong.text,"\n")

    courseblockextra = courseblock.find("p",class_="courseblockextra")
    courseblockprereq = courseblockextra.span
    print("  ",courseblockprereq.text,"\n")
    
    courseblockdesc = courseblock.find("p",class_="courseblockdesc")
    print("    ",courseblockdesc.text,"\n       -----------------------\n")
print("page title : ",page_title.text)


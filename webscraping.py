# # we need beautifulsoup4 and requests

import requests
from bs4 import BeautifulSoup

response = requests.get("https://stackoverflow.com/questions")

# # dont do this it ll take out all data from that web
# print(response.text)


# # we are gonna parser html file that why html.parser
soup = BeautifulSoup(response.text, "html.parser")

# # now this soup object mirror the structure of our html document
# # easily navigate the doc and find various elemnt

questions = soup.select(".question-summary")
# # about question ll throw a list
# # each item in the list is an instance of tag class

# """instead of tag its shows resultset class """
x = type(questions)
# # <class 'bs4.element.ResultSet'>

x = questions[0].attrs
# # {'class': ['question-summary'], 'id': 'question-summary-66040365'}

x = questions[0].get("id", 0)
# # from above we get id key

y = questions[0].select(".question-hyperlink")
# """[<a class="question-hyperlink" href="/questions/66040505/laravel-page-expire-419-error-on-namecheap-hosting">
# Laravel page expire 419 error on namecheap hosting</a>]"""


# # so here for each question we have one title better do it with method name .select_one we dont need a list
# # if you put .select("unknow-mention class") its shows you empty list here


# # this select_one return one object instead of a list
z = questions[0].select_one(".question-hyperlink")
# # same result as y but no list

z1 = questions[0].select_one(".question-hyperlink").get_text()
# # provide actual questions


for question in questions:
    print(question.select_one(".question-hyperlink").getText())

# # getting vote for each question

for question in questions:
    print(question.select_one(".vote-count-post").getText())

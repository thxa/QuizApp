import json
import re
import functools
import pandas as pd
#|%%--%%| <XfrGGZBrTA|7c1LxMrXlk>

!ls pages

#|%%--%%| <7c1LxMrXlk|yFvWWN9PyI>

# json.load()
# ! ls -l

data_x = []
for i in range(1, 646):
    data_x.append(json.loads(open(f"pages/{i}.json").read()))

#|%%--%%| <yFvWWN9PyI|V3MQTK7qLS>
print(data_x)

#|%%--%%| <V3MQTK7qLS|1bXyd8tmeF>
def extract_text(x):
    l = []
    def dfs(x):
        if(type(x) == int): return
        if(type(x) == str and x != "https://www.youtube.com/channel/UC1w7rLIVgDgMdI_ktBwAqww" and x != "https://www.google.com/url?q=https://www.youtube.com/channel/UC1w7rLIVgDgMdI_ktBwAqww&sa=D&source=apps-viewer-frontend&ust=1720248651247659&usg=AOvVaw2MN0QVG6txDfdv3a4kChCB"):
            l.append(x)
            return
        if(type(x) == list):
            for i in x:
                dfs(i)
    dfs(x)
    return l

#|%%--%%| <1bXyd8tmeF|9BuY0XhRLU>

# https://stackoverflow.com/questions/7160737/how-to-validate-a-url-in-python-malformed-or-not
def is_url(text):
    regex = re.compile(
            r'^(?:http|ftp)s?://' # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
               r'localhost|' #localhost...
               r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
            r'(?::\d+)?' # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return True if re.match(regex, text) is not None  else False

# print(is_url("google.com")) # False
# print(is_url("https://google.com")) # True

#|%%--%%| <9BuY0XhRLU|WtYYKUzonj>

# data = extract_text(x)
data = map(lambda a: extract_text(a), data_x)
data = list(functools.reduce(lambda a,b: a+b, data))

#|%%--%%| <WtYYKUzonj|048L0admSI>

data

#|%%--%%| <048L0admSI|vXqVP2rzhN>
"""
Question
[number][char_cap] last thing [?] or [A.]

Options:
[A.] text until [B.] until [C.] until [D.] maybe until [E.]

urls for each quetion.

"""
"A. { } ."
    



#|%%--%%| <vXqVP2rzhN|GfGEw1n3Kv>
questions = []
options = []
urls = []

start_q = 0 
start_a = 0
is_a = 0

for i, text in enumerate(data):
    if i+1 == len(data):
        break

    # if(text == "812"): breakpoint()    
    if( (text.isdigit() or text.split("#")[0].isdigit()) and data[i+1]  in ("A", "The", "#")):
        start_q = i 
        if(is_a):
            options.append([start_a, i]) 
            start_a = i 
            is_a = 0

    if(text == "A."):
        questions.append([start_q, i])
        start_a = i
        is_a = 1

    elif(text in ("B.", "C.", "D.", "E.", "F.")):
        options.append([start_a, i]) 
        start_a = i 
    
    elif(is_url(text) and is_a):
        options.append([start_a, i]) 
        start_a = i 
        is_a = 0

    if is_url(text):
        urls.append(i)









#|%%--%%| <GfGEw1n3Kv|58kuOhL06Y>
# questions
 
for question in questions:
    print(" ".join(data[question[0]:question[1]]))



#|%%--%%| <58kuOhL06Y|Wn9mNBR3dh>

# options
for option in options:
    print(" ".join(data[option[0]:option[1]]))

#|%%--%%| <Wn9mNBR3dh|IUIEsRxIFa>

# url
for url in urls:
    print(data[url])
#|%%--%%| <IUIEsRxIFa|OYhXlPp8z8>

# class Question(object):
# class Answers(object):
# class Resource(object):

class Quiz(object):
    def __init__(self, _id, question, options, explain=None, resources=None, answers=None):
        self._id = _id
        self.question = question
        self.options = options
        self.explain = explain
        self.resources = resources
        self.answers = answers
    
    def __str__(self):
        return self.question

    def __repr__(self):
        return self.question
    def __dict__(self):
        return {
            "_id":self._id,
            "question": self.question,
            "options": self.options,
            "explain": self.explain,
            "answers": self.answers,
            "resources": self.resources,
        }


#|%%--%%| <OYhXlPp8z8|LtmdMKzZU1>

quizes = []
i_o = 0
i_r = 0

for i, q in enumerate(questions):
    
    options_x = []
    explain_x = ""
    resources_x = []
    options_x = []
    if(i == len(questions)-1):
       options_x = list(map(lambda a: " ".join(data[a[0]:a[1]]), options[i_o:]))
       resources_x = list(map(lambda a: data[a], urls[i_r:]))

    else:

        while(i_o < len(options) and options[i_o][0] < questions[i+1][0]):
            option = " ".join(data[options[i_o][0]:options[i_o][1]])
            options_x.append(option)
            i_o += 1

        while(i_r < len(urls) and urls[i_r] < questions[i+1][0]):

            resource = data[urls[i_r]]
            resources_x.append(resource)
            i_r += 1

    
    

    # pre-processes
    q = " ".join(data[q[0]: q[1]])

    quizes.append(Quiz(
        _id=int(q.split()[0].split("#")[0]),
        question=q,
        options=options_x,
        explain=explain_x,
        answers=[],
        resources=resources_x
    ))




#|%%--%%| <LtmdMKzZU1|PQdqNVycKR>

for q in quizes:
    print(q.options)


#|%%--%%| <PQdqNVycKR|i0KRDwm4pX>

print(len(quizes))

#|%%--%%| <i0KRDwm4pX|zedkqOm8BB>

# quizes[0].question
# quizes[0].options
# quizes[0].explain
# quizes[0].answersx
# quizes[0].resources

# print(quizes[0])


for q in quizes:
    print()
    print(q.question)
    print(q.options)
    # print(q.answersx)
    print(q.resources)
    print()
#|%%--%%| <zedkqOm8BB|iNnR1s1xUc>
from collections import defaultdict

d = defaultdict(lambda:0)
print(len(quizes))
for i, q in enumerate(quizes):
    if d[q.question]:
        quizes[i], quizes[-1] = quizes[-1], quizes[i]
        quizes.pop()
    else:
        d[q.question]=1

    
print(len(quizes))





#|%%--%%| <iNnR1s1xUc|ltDvILny53>
quizes = sorted(quizes, key=lambda a: a._id)



#|%%--%%| <ltDvILny53|LoBH3dOGbi>
r"""°°°
This is the Recommanded option:
°°°"""
#|%%--%%| <LoBH3dOGbi|aXx81kUKJf>

#|%%--%%| <aXx81kUKJf|ActsDjeCPp>
x = list(map(lambda x: x.__dict__(), quizes))
with open("output/all_questions.json", "w") as f:
    json.dump(x, f)

#|%%--%%| <ActsDjeCPp|UDKJhsP7U6>

# x = list(map(lambda x: x.__dict__(), quizes))
# data = 
with open("output/a_10.json", "r") as f:
    data = json.loads(f.read())

#|%%--%%| <UDKJhsP7U6|rMIfhBfb0Y>

with open("output/x.json", "r") as f:
    data = json.loads(f.read())

#|%%--%%| <rMIfhBfb0Y|rGqkZLcW81>


with open("output/all_questions.json", "r") as f:
    quizes = json.loads(f.read())

#|%%--%%| <rGqkZLcW81|g4ZnOjY5D1>


with open("output/a_10.json", "r") as f:
    hmm = json.loads(f.read())
print(len(hmm))

#|%%--%%| <g4ZnOjY5D1|gTDcDTOUBa>
# quizes

# print(quizes)
n = 1
l,r = (0, 65)
while r < len(quizes):
    with open(f"output/quiz_{n}.json", "w") as f:
        json.dump(quizes[l:r], f)
    l = r
    if(r == len(quizes)-1):
        break
    if(r + 65 < len(quizes)):
        r+=65
    else:
        r+=(len(quizes)-r) - 1
    print(r)
    n+=1

#|%%--%%| <gTDcDTOUBa|JZUJDtj5ho>

x = list(map(lambda x: x.__dict__(), data[:10]))
with open("output/a_10.json", "w") as f:
    json.dump(x, f)

#|%%--%%| <JZUJDtj5ho|sfD39w98pi>



#|%%--%%| <sfD39w98pi|2H8VtkOEz5>

# Quiz(   _id=int(data[0].get("id", None)),
#         question=data[0].get("question", None),
#         options=data[0].get("options", None),
#         explain=data[0].get("explain", None),
#         answersx=data[0].get("answers", None),
#         resources=data[0].get("resources", None),
#     )


#|%%--%%| <2H8VtkOEz5|tD6Ih3ARAS>

data = list(map(lambda x: Quiz(**x), data))

#|%%--%%| <tD6Ih3ARAS|ySzidnnESj>
for q in data:
    print(q.options)


#|%%--%%| <ySzidnnESj|VrhYYVt6xX>

type(data[0])


#|%%--%%| <VrhYYVt6xX|lESOWCiRRp>
r"""°°°
This is not Recommanded option
°°°"""
#|%%--%%| <lESOWCiRRp|n22ctopXAQ>

import pandas as pd

#|%%--%%| <n22ctopXAQ|zU1vnLK4Vq>

df = pd.DataFrame(map(lambda x: x.__dict__(), quizes))


#|%%--%%| <zU1vnLK4Vq|lUt0JFlzXc>

df.info()
#|%%--%%| <lUt0JFlzXc|3HxWZyTjgT>
# df.drop_duplicates(df["question"])
df = df.drop_duplicates(subset="question")


#|%%--%%| <3HxWZyTjgT|I1LbXpAKWa>

df.to_json("output/quizes.json")

#|%%--%%| <I1LbXpAKWa|TfrUGyu460>
r"""°°°
This Code for read quizes json file
°°°"""
#|%%--%%| <TfrUGyu460|l1IkTb2ykG>

df = pd.read_json("output/quizes.json")


#|%%--%%| <l1IkTb2ykG|22GngVP4s4>

df.loc[0]

#|%%--%%| <22GngVP4s4|VkPMFNj91x>




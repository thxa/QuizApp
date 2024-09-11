import json
import re

#|%%--%%| <ar9vKMOiPe|xloZ274bM3>

with open("output/Edited_quiz_1.json", "r") as f:
    data = json.loads(f.read())
print(len(data))

#|%%--%%| <xloZ274bM3|FyjS1WqAUt>
# remove missing data
new_data = list(filter(lambda x: x["question"] != "", data))

#|%%--%%| <FyjS1WqAUt|glOgY5YGUU>
# To convert any options sperate by \n and at the same time in one option
for i, quiz in enumerate(new_data):

    # handle cleaning questions
    new_data[i]["question"] = re.sub(r'https?:\/\/\S+', '', quiz["question"])
    new_data[i]["answers"] = list(map(lambda a: int(a), quiz["answers"]))

    # handle cleaning options
    if len(quiz["options"]) == 1: 
        new_data[i]["options"] = quiz["options"][0].split("\n")

#|%%--%%| <glOgY5YGUU|hzwijIj3TY>


with open("output/Edited_quiz_1_cleaned_1.json", "w") as f:
    json.dump(new_data, f)

#|%%--%%| <hzwijIj3TY|mUww3KzEvT>




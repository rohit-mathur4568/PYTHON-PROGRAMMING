import json

document = {
    "text": "Section 80C provides tax deductions",
    "page" : 55,
    "source": "aflkh",
    "category": "lknlnln"

}

with open("document.json" ,"w") as file:
    json.dumps(document , file , indent = 4)

with open("document.json", "r") as file:
    data = json.load(file)

    print(data["text"])
    print(data["page"])
    print(data["source"])


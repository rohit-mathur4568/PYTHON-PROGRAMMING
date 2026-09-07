document = {
    "text": "Section 80C provides tax deductions.",
    "page": 25,
    "source": "income tax act",
    "category":"income tax"
}
print(document["text"])
print(document["page"])
print(document["source"])
print(document["category"])


document["author"] = "TAXMANN"
print (document)

for key, value in document.items():
    print(key,":",value)

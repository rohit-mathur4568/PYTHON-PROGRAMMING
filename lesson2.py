name =  "Rohit Mathur"
skills = ["Python","Rag" , "Langchain" , "FAISS"]

print(f"my name is {name}")
print(f"my skills is {skills}")
print("top skills : " + skills[2] + " , " + skills[1])

# print(skills[0])
# print(skills[2])
print("add fast api")
skills.append("FastAPI")
print (skills)

for skill in skills: 
    print(skill)
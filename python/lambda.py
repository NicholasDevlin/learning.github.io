people =[
  {"name" : "lia", "house" : "my heart"},
  {"name" : "nicholas", "house" : "lia"}
]

people.sort(key = lambda person : person["name"])

print(people)
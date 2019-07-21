import json

diary = {
    "id": 3,
    "title": "I'm starving..",
    "body": "On nana On na On nanana deal car",
}

print(diary)
print(type(diary))


# dumps : dict --> json
diary_s = json.dumps(diary)

print(diary_s)
print(type(diary_s))


# loads : json --> dict
diary_back = json.loads(diary_s)
print(diary_back)
print(type(diary_back))

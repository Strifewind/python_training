import wolframalpha

input = raw_input("Question: ")
app_id = "VPATHT-42H3TYV8V8"
client = wolframalpha.Client(app_id)

res = client.query(input)
answer = next(res.results).text

print(answer)
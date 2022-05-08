import wikipedia

while True:
        input = raw_input("Question: ")
        wikipedia.set_lang("eng")
        print wikipedia.summery(input, sentences=2)
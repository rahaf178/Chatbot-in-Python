
import cohere

# API key
co = cohere.Client("")

while True:
    question = input("مرحباً ماذا تريد ان تسأل")
    if question.lower() == "خروج":
        break

    response = co.chat(message=question)
    print(response.text)

from search import search_prompt

def main():
    question = input("Digite sua pergunta: ")
    while question.strip():
        chain = search_prompt(question)
        print(chain.content)
        question = input("Digite sua pergunta: ")
    pass

if __name__ == "__main__":
    main()
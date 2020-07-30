

respond = {"crashed":"Are the drivers up to date",
            "blue":"Ah, the blue screen of death. And then what happened?",
            "hacked":"You should consider installing anti-virus software?",
            "windows":"Ah, I think I see your problem. What version?",
            "bluetooth":"Have you tried mouthwash.",
            "apple":"You do mean the computer kind?.",
            "spam":"You should see if your mail client can filter messages.",
            "connection":"Contact Telkom."}


def welcome():
    print('Welcome to the automated technical support system.')
    print('Please describe your problem.')

def get_input(input):
    sentence = input.lower().split(" ")
    for i in sentence:
        if i in respond.keys():
            # response = respond.get(i)
            return respond.get(i)

    return 'Curious, tell me more.'

# def response(q):
#     if response in respond:
#         print(respond.get(response))
#     else:
#         print('Curious, tell me more.')

def main():
    welcome()
    # query = get_input(input())
    query = ""
    stop = True
    while stop:
        # response(query)
        query = input()
        if query == 'quit':
            break
        else:
            print(get_input(query))
        # query = get_input(input())
        # print("Curious, tell me more")
        # print(query)

main()
if __name__ == '__main__': main()
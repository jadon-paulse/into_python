

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


def get_input():
    return input().lower()

def response(q):
    if q in respond:
        print(respond.get(q))
    else:
        print('Curious, tell me more.')

def main():
    welcome()
    query = get_input()

    while (not query == 'quit'):
        response(query)
        query = get_input()

main()
if __name__ == '__main__': main()
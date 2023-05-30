import openai
import textwrap

with open('api_key.dat','r') as f:
    key=f.read()
openai.api_key=key

def answer(query): 
    response = openai.Completion.create(
        model="text-davinci-003", 
        prompt=query,
        temperature=0,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0.2,
        presence_penalty=0
) 
    return response.choices[0].text

def ask():
    flag=True
    greeting='Hi there, what do you want to know?'
    print(greeting)
    while(flag==True):
        query=input()
        if 'bye' not in query:
            chat=answer(query)
            print('chatGPT:',textwrap.fill(chat, 100))
            print()
        else:
            flag=False
            print('chatGPT: Bye!')
ask()
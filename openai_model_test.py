import openai

key='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'
openai.api_key=key 

def answer(query): 
    response = openai.Completion.create(
        model="davinci", 
        prompt=query,
        temperature=0,
        max_tokens=100,
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
            print('chatGPT:',chat)
            print()
        else:
            flag=False
            print('chatGPT: Bye!')
ask()
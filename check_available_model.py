import openai

key='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'
openai.api_key=key

data = openai.Engine.list() 
models=[]
for eng in data['data']:
    models.append(eng['id'])
with open('avail_openai_model.txt','w') as f:
    for m in models:
        f.write(m+'\n')

exit()
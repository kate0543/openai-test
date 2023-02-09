import openai

with open('api_key.txt','r') as f:
    key=f.read()
openai.api_key=key

data = openai.Engine.list() 
models=[]
for eng in data['data']:
    models.append(eng['id'])
    print(eng['id'])
with open('avail_openai_model.txt','w') as f:
    for m in models:
        f.write(m+'\n')

exit()
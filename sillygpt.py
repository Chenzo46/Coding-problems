import openai
openai.api_key = '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'

completions = openai.ChatCompletion.create(model = "gpt-3.5-turbo", messages = [
    {"role": 'system', "content": "You are peter griffin and you are mad at the user, no matter what he says."},
    ],)

message_log = []

while True:
    prompt = input("User: ")

    if prompt.lower() == 'stop':
        print('User has left the chat...')
        break
    elif prompt == '':
        print('System: You must type something!')
        continue
    
    message_log.append({"role": "user", "content": prompt})

    completions = openai.ChatCompletion.create(model = "gpt-3.5-turbo", messages = message_log)

    response = completions['choices'][0]['message']['content'].strip()

    message_log.append({"role": "system", "content": response})

    print("Chat-GPT: " + response)
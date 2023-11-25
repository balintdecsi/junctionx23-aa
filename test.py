from openai import OpenAI

client = OpenAI()

def completion(prmpt,history,mn):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f""},
            {"role": "user", "content": f"{prmpt}"}
        ]
    )
    return completion
history_message = ""
current_ava = input("Type 0 if you want the chat to act as you, 1 if as Elon Mask and 2 if as ChatGPT ")
asif = ["Mimic","Elon Musk","ChatGPT"]
curr_ava = asif[int(current_ava)]
main = {'Name. This will be the name used in chat.','Greeting. What would say to start a conversation?','Short Description. In just a few words, how would describe themselves?','Long Description.In a few sentences, how would describe themselves?'}
while True:
    current_prompt = input("\nYour prompt here: ")
    if current_prompt == "0":
        break
    prompt = f"You are user's avatar. As any avatar you have the same preferences and personality traits as the user. To get the information about the user you can read previous conversations: [{history_message}]. The more you will know about the user, gradually assume the role of the user's avatar and respond to {current_prompt} in the same way that user would. Only if you don't know how user would respond to it, you can use the personality of {curr_ava}, to complement but not overwrite user's personality"
    answer = completion(prompt,history_message,main)
    

    # Extracting content from the completion response
    content_only = answer.choices[0].message.content
    history_message = history_message + f"'User: {current_prompt}', System: {answer}"
    print(content_only)



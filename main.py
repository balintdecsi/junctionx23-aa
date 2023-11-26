from flask import Flask, render_template, request, jsonify 
from vertexai.language_models import ChatModel, InputOutputTextPair

app = Flask(__name__)
app.static_folder = 'static'

T = 0.2

# global message_history
# global examples
# global current_input_text
# global current_output_text

message_history = [
    "You: Hi, I'm your digital self! TellYou made me from your data. Let us get to know better! Can you please introduce yourself, including your age, sex and hometown? Thanks!",
]
examples = []
current_input_text = ["Can you please introduce yourself, including your age, sex and hometown?", "debugging"]

# TODO developer - override these parameters as needed:
parameters = {
    "temperature": T,  # Temperature controls the degree of randomness in token selection.
    "max_output_tokens": 256,  # Token limit determines the maximum amount of text output.
    "top_p": 0.95,  # Tokens are selected from most probable to least until the sum of their probabilities equals the top_p value.
    "top_k": 40,  # A top_k of 1 means the selected token is the most probable among all tokens.
}

def bison_chat_start(examples, message_history):
    chat_model = ChatModel.from_pretrained("chat-bison@001")

    chat = chat_model.start_chat(
        context="You are a chatbot with the following chat history:\n" + "\n".join(message_history) + "\n",
		examples=examples,
    )
    return chat

def get_completion(chat, prompt):
    
    message_prompt = "My answer to your question is as follows: '" + prompt + "'. React to that and also ask me about a new random topic."
    response = chat.send_message(
        message_prompt,
        **parameters,
    )

    return response.text

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    message_history.append("User: " + userText)
    current_example = InputOutputTextPair(
        input_text=current_input_text[0],
        output_text=userText,
    )
    examples.append(current_example)
    chat = bison_chat_start(examples, message_history)
    bot_response = get_completion(chat, userText)
    message_history.append("Bot: " + bot_response)
    current_input_text[0] = bot_response.split(".")[-1]
    return bot_response


if __name__ == "__main__": 
	app.run()
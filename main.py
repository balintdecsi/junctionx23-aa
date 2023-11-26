from flask import Flask, render_template, request, jsonify 
from vertexai.language_models import ChatModel, InputOutputTextPair

app = Flask(__name__)
app.static_folder = 'static'

T = 0.2

# TODO developer - override these parameters as needed:
parameters = {
    "temperature": T,  # Temperature controls the degree of randomness in token selection.
    "max_output_tokens": 256,  # Token limit determines the maximum amount of text output.
    "top_p": 0.95,  # Tokens are selected from most probable to least until the sum of their probabilities equals the top_p value.
    "top_k": 40,  # A top_k of 1 means the selected token is the most probable among all tokens.
}

def bison_chat_start() -> None:
    chat_model = ChatModel.from_pretrained("chat-bison@001")


    chat = chat_model.start_chat(
        context="",
        examples=[
        ],
    )
    return chat

chat = bison_chat_start()

def get_completion(prompt):
        
    response = chat.send_message(
        prompt, **parameters
    )

    return response.text

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return get_completion(userText)


if __name__ == "__main__": 
	app.run() 

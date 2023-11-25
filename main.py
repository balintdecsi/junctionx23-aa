from flask import Flask, render_template, request, jsonify 
from vertexai.language_models import ChatModel, InputOutputTextPair

app = Flask(__name__) 

T = 0.2

# TODO developer - override these parameters as needed:
parameters = {
    "temperature": T,  # Temperature controls the degree of randomness in token selection.
    "max_output_tokens": 256,  # Token limit determines the maximum amount of text output.
    "top_p": 0.95,  # Tokens are selected from most probable to least until the sum of their probabilities equals the top_p value.
    "top_k": 40,  # A top_k of 1 means the selected token is the most probable among all tokens.
}

def bison_chat_start(history_message) -> None:
    chat_model = ChatModel.from_pretrained("chat-bison@001")

    chat = chat_model.start_chat(
        context=f"You are user's avatar. Being an avatar means you have the same preferences and personality traits as the user, it also means, whenever you are asked a question about you, the question is actually about the user. For example 'you' becomes 'user' and 'your' becomes 'users'. Memorize the information about user from [{history_message}]. You don't have to do a review of this information.",# If you don't know about some user's preferences or personality traits, you can assume that they are similar to {curr_ava}'. Try to respond in a style that user would usually use in his conversations. ",
		examples=[],
    )
    return chat

with open('chat_history.txt', 'r') as f:
    history_message = f.read()
    chat = bison_chat_start(history_message)

def get_completion(prompt):
        
    response = chat.send_message(
        prompt, **parameters
    )

    return response.text

@app.route("/", methods=['POST', 'GET']) 
def query_view(): 
	if request.method == 'POST': 
		print('step1')
		prompt = request.form['prompt'] 
		response = get_completion(prompt) 
		print(response) 

		return jsonify({'response': response}) 
	return render_template('index.html')


if __name__ == "__main__": 
	app.run(debug=True)

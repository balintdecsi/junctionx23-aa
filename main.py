from flask import Flask, render_template, request, jsonify 
from openai import OpenAI
from dotenv import load_dotenv
import os

app = Flask(__name__) 

# Load the environment variables from .env file
load_dotenv()

# Get the value of the OPENAI_KEY variable
openai_key = os.getenv("OPENAI_KEY")

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=openai_key,
)

def get_completion(prompt): 
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo",
    )
	
    return chat_completion.choices[0].message.content

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

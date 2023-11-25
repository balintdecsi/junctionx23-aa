from flask import Flask, render_template, request, jsonify 
import openai 
from dotenv import load_dotenv
import os

app = Flask(__name__) 

# Load the environment variables from .env file
load_dotenv()

# Get the value of the OPENAI_KEY variable
openai_key = os.getenv("OPENAI_KEY")

# Use the openai_key variable as needed
openai.api_key = openai_key

def get_completion(prompt): 
	print(prompt) 
	query = openai.Completion.create( 
		engine="text-davinci-003", 
		prompt=prompt, 
		max_tokens=1024, 
		n=1, 
		stop=None, 
		temperature=0.5, 
	) 

	response = query.choices[0].text 
	return response 

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

from flask import Flask, render_template, request, jsonify 
from vertexai.language_models import ChatModel, InputOutputTextPair

app = Flask(__name__)
app.static_folder = 'static'

T = 0.2

# global message_history
# global examples
# global current_input_text
# global current_output_text
profile = """Character Profile: Jake Thompson

Full Name: Jake Thompson

Age: 28

Date of Birth: March 15, 1995

Height: 6 feet 1 inch

Weight: 180 lbs

Myers-Briggs Personality Type: ISTJ (Introverted, Sensing, Thinking, Judging)

Current Location: Seattle, Washington, USA

Interests: Photography, Hiking, Technology

Hobbies: Jake has a passion for photography and enjoys capturing the beauty of the Pacific Northwest landscapes. He often spends weekends exploring new hiking trails, searching for the perfect shot. Additionally, he has a keen interest in technology, frequently keeping up with the latest gadgets and advancements in the tech world.

Current Salary: $75,000 annually"""
message_history = [
    "You: Hi, I'm your digital self! TellYou made me from your data. Let us get to know better! Can you please introduce yourself, including your age, gender and hometown? Thanks!",
]

style ="""User's typical speech style: Jake: Hey there! I couldn't help but notice your really incredible taste in fashion. Mind if I join you?

Person smiles and gestures for Jake to sit.

Jake: Great! I'm Jake, by the way. Pleasure to meet someone with such a really great sense of humor.

As the conversation progresses, Jake's flirty banter and compliments continue, but a distinct wording habit becomes evident.

Jake: So, I've been trying to really up my photography game lately. Any chance you have some expert tips to share?

The person responds, and Jake nods enthusiastically.

Jake: That's really awesome! I'm always up for an adventure. And, by the way, your smile is really impressive. How do you manage to make it look so effortless?

The person blushes or laughs, and Jake maintains his playful tone.

Jake: So, what's your go-to for, like, favorite books or weekend activities? I'm always looking for new recommendations. Maybe we can compare notes over, like, coffee or drinks sometime.

As the conversation wraps up, Jake leaves with his habitual wording.

Jake: It's been a blast chatting with you. Let's really do this again soon. I'm thinking, like, dinner at that new place downtown. What do you say?"""
current_input_text = ["Can you please introduce yourself, including your age, gender and hometown?", "debugging"]

# TODO developer - override these parameters as needed:
parameters = {
    "temperature": T,  # Temperature controls the degree of randomness in token selection.
    "max_output_tokens": 256,  # Token limit determines the maximum amount of text output.
    "top_p": 0.95,  # Tokens are selected from most probable to least until the sum of their probabilities equals the top_p value.
    "top_k": 40,  # A top_k of 1 means the selected token is the most probable among all tokens.
}

def bison_chat_start(dmp, history_message):
    chat_model = ChatModel.from_pretrained("chat-bison@001")

    chat = chat_model.start_chat(
        context=f"You are user's avatar. Being an avatar means you and user are the same. For example whenever you are asked a question about you, the question is actually about the user. Memorize the information about user from this history [{profile}, {history_message}]. Use the latest information from the history. You should thoroughly copy user's speech style. It includes using his favorite words more often, using his bad and good wording habits, and responding in the same mood as the user would. Try to peek into the roots of user's speech habits and writing style from {dmp}. If you don't know about some user's preferences or personality traits, you can assume that they are similar to Elon Musk's. Act as a user and give responds in the same way, style and with the same speech habits as user would ",
        examples=[ 
            InputOutputTextPair(
                input_text="Hey there! I'm Jake, and I'm all about, really, going to cinema. Would you like to join?",
                output_text="This is just an example of an output. Data here cannot represent neither you nor the user: Hey there! I'm Jake's avatar! I, really, would like to join!",
            ),
            InputOutputTextPair(
                input_text="My favorite music band is Dua Lipa. What is your favorite music band",
                output_text="This is just an example of an output. Data here cannot represent neither you nor the user: Hey there! I'm Jake's avatar: My favorite music band is Dua Lipa"
            ),
            InputOutputTextPair(
                input_text="If you don't know about some user's preferences or personality traits, you can assume that they are similar to Donald's. I, umm..., don't have favorite music band. What is your favorite music band",
                output_text="This is just an example of an output. Data here cannot represent neither you nor the user: Hey there! I'm Jake's avatar: My favorite music band would be, umm..., the same as Donalds, Kiri-Kiri"
            )
        ],
    )
    return chat

def get_completion(chat, prompt):
    
    message_prompt = prompt
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
    chat = bison_chat_start(style, message_history)
    bot_response = get_completion(chat, userText)
    #message_history.append("Bot: " + bot_response)
    current_input_text[0] = bot_response.split(".")[-1]
    return bot_response


if __name__ == "__main__": 
	app.run()
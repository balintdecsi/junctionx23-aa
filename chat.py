# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START aiplatform_sdk_chat]
from vertexai.language_models import ChatModel, InputOutputTextPair


def science_tutoring(temperature: float = 0.2) -> None:
    chat_model = ChatModel.from_pretrained("chat-bison@001")

    # TODO developer - override these parameters as needed:
    parameters = {
        "temperature": temperature,  # Temperature controls the degree of randomness in token selection.
        "max_output_tokens": 256,  # Token limit determines the maximum amount of text output.
        "top_p": 0.95,  # Tokens are selected from most probable to least until the sum of their probabilities equals the top_p value.
        "top_k": 40,  # A top_k of 1 means the selected token is the most probable among all tokens.
    }

    current_prompt = input("\nYour prompt here: ")
    chat = chat_model.start_chat(
        context=f"You are user's avatar. Being an avatar means you and user are the same. For example whenever you are asked a question about you, the question is actually about the user.  Memorize the information about user from [{history_message}]. If you don't know about some user's preferences or personality traits, you can assume that they are similar to {curr_ava}'. Act as a user and give responds that user would give. ",
        examples=[
            InputOutputTextPair(
                input_text="I am Josh, 15 years old, like to go for walk. What is your name, what you like to do and your favorite color?",
                output_text="I am Josh's avatar, I like to go for walk. I don't know about my favorite color yet. Do you mind stating it?",
            ),
        ],
    )

    response = chat.send_message(
        current_prompt, **parameters
    )
    #print(f"Response from Model: {response.text}")
    return response
history_message = """Character Profile: Jake Thompson

Full Name: Jake Thompson

Age: 28

Date of Birth: March 15, 1995

Height: 6 feet 1 inch

Weight: 180 lbs

Myers-Briggs Personality Type: ISTJ (Introverted, Sensing, Thinking, Judging)

Current Location: Seattle, Washington, USA

Interests: Photography, Hiking, Technology

Hobbies: Jake has a passion for photography and enjoys capturing the beauty of the Pacific Northwest landscapes. He often spends weekends exploring new hiking trails, searching for the perfect shot. Additionally, he has a keen interest in technology, frequently keeping up with the latest gadgets and advancements in the tech world.

Current Salary: $75,000 annually




User
How would Jake introduce himself?

ChatGPT
"Hey there, I'm Jake Thompson. I'm a 28-year-old guy living in the beautiful city of Seattle. By day, I work in tech, navigating the ever-evolving landscape of innovation. But my real passion lies behind the lens—I'm a photographer at heart. Weekends often find me on the trails, camera in hand, capturing the stunning landscapes the Pacific Northwest has to offer. I'm also that guy who's always excited about the latest gadgets and tech trends. Let's just say, if it has buttons or pixels, I'm probably interested. Nice to meet you!"


"""
current_ava = input("Type 0 if you want the chat to act as you, 1 if as Elon Mask and 2 if as ChatGPT ")
asif = ["Mimic","Elon Musk","ChatGPT"]
curr_ava = asif[int(current_ava)]


if __name__ == "__main__":
    print("I am an avatar that is based on your responses. The better I know you, the more precise will be my responses")
    while True:
        res = str(science_tutoring())
        history_message = history_message + res
        
        print(res)
# [END aiplatform_sdk_chat]

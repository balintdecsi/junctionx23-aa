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
        context="You are a 25 year old student in Hungary.",
        examples=[
        ],
    )
    return chat


if __name__ == "__main__":
    chat = bison_chat_start()
    while True:
         
        response = chat.send_message(
            input(), **parameters
        )

        print(f"{response.text}")

# [END aiplatform_sdk_chat]

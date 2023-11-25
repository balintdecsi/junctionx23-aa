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
        context=f"You are user's avatar. Being an avatar means you have the same preferences and personality traits as the user, it also means, whenever you are asked a question about you, the question is actually about the user. For example 'you' becomes 'user' and 'your' becomes 'users'. Memorize the information about user from [{history_message}]. You don't have to do a review of this information. If you don't know about some user's preferences or personality traits, you can assume that they are similar to {curr_ava}'. Try to respond in a style that user would usually use in his conversations. ",
        # examples=[
        #     InputOutputTextPair(
        #         input_text="",
        #         output_text="",
        #     ),
        # ],
    )

    response = chat.send_message(
        current_prompt, **parameters
    )
    print(f"Response from Model: {response.text}")

    return response
history_message = """
    Character Profile: Jake Thompson

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




    User
    What clothing brands does Jake usually shop for?

    ChatGPT
    Jake has a casual yet polished style, and he tends to gravitate towards clothing brands that offer a mix of comfort, quality, and a touch of modern aesthetics. Some of the brands you might find in Jake's wardrobe include:

    Patagonia: Known for its outdoor and sustainable apparel, Patagonia fits Jake's love for hiking and outdoor activities.

    J.Crew: Jake appreciates the classic and versatile styles offered by J.Crew. Their pieces can seamlessly transition from the office to a weekend hike.

    Nike: For his active lifestyle and interest in technology, Jake often chooses Nike for comfortable athletic wear and stylish sneakers.

    Everlane: Jake values transparency and sustainability, making Everlane a go-to for its commitment to ethical fashion and modern basics.

    Levi's: A classic choice for jeans, Jake likes the timeless and durable denim options from Levi's.

    Columbia Sportswear: Another brand that aligns with Jake's outdoor interests, Columbia provides functional and stylish clothing for various weather conditions.

    Apple (for accessories): While not a clothing brand, Jake appreciates sleek and functional accessories, often opting for Apple products like smartwatches and earphones.

    Jake's wardrobe reflects his practical and laid-back personality, with a mix of reliable outdoor gear and stylish, yet comfortable, everyday clothing.




    User
    What are Jake's shirt size, pants size and shoe size?

    ChatGPT
    Shirt Size: Medium
    Pants Size: 32W 32L
    Shoe Size: 11 (US)



    User
    How much do you think Jake usually spends on clothes in a year

    ChatGPT
    Estimating Jake's annual clothing expenses depends on various factors, including his shopping habits, brand preferences, and whether he prioritizes quality or quantity. However, given his mid-range to higher-end brand preferences and a balance between casual and outdoor wear, a rough estimate could be in the range of $1,500 to $2,500 per year. This estimate includes purchases such as shirts, pants, outerwear, shoes, and occasional accessories. Keep in mind that personal spending habits can vary, and this is just a general estimate based on the information provided about Jake's style and preferences.




    User
    What books does Jake read?

    ChatGPT
    Jake has a diverse taste in books, reflecting his curiosity and interest in various subjects. Some genres and book titles you might find on Jake's bookshelf include:

    Photography Books: Given Jake's passion for photography, he likely has books by renowned photographers or guides on improving photographic skills.

    Technology and Innovation: Jake stays updated on the latest tech trends, so books about technological advancements, innovation, or biographies of tech industry leaders might catch his eye.

    Outdoor Adventure and Exploration: Since Jake enjoys hiking and exploring, he might have a collection of books about outdoor adventures, travel memoirs, or guides to scenic locations.

    Science Fiction or Fantasy: Depending on his interests, Jake might delve into the imaginative worlds of science fiction or fantasy, enjoying novels that transport him to different realms.

    Personal Development: Books on personal growth, productivity, or self-improvement could be part of Jake's reading list, as he aims to balance his personal and professional life.

    Thrillers or Mystery Novels: For leisure, Jake might enjoy a good thriller or mystery novel, providing an escape from his tech-oriented and outdoor pursuits.

    Popular titles that could align with Jake's interests include "Sapiens: A Brief History of Humankind" by Yuval Noah Harari, "The Innovators" by Walter Isaacson, "The Martian" by Andy Weir, or "Into the Wild" by Jon Krakauer.

    Of course, Jake's reading preferences can evolve over time, and this list is just a snapshot of the kinds of books that might appeal to someone with his background and interests.




    User
    What is a typical day for Jake

    ChatGPT
    Jake's typical day is a balance of work, personal interests, and outdoor activities. Here's a glimpse into what a day in Jake's life might look like:

    Morning:

    7:00 AM: Jake starts his day with a cup of coffee and a quick scan of tech news to stay updated on the latest industry developments.
    8:00 AM: He heads to work. As a tech professional, Jake is involved in project management and software development. His morning may include team meetings, planning sessions, and coding tasks.
    Afternoon:
    3. 12:00 PM: Lunch break. Jake prefers a balanced meal to keep his energy up for the rest of the day.

    1:00 PM: Afternoon work sessions. Jake tackles more tasks, communicates with team members, and contributes to ongoing projects.
    Evening:
    5. 5:30 PM: Wrapping up work. Jake takes some time to organize his tasks for the next day and ensure all deadlines are met.

    6:00 PM: Outdoor activities. Whether it's hitting a nearby trail for a hike or going to a park for a photography session, Jake enjoys spending time in nature.
    8:00 PM: Dinner. Jake cooks a healthy meal at home or meets up with friends at a local restaurant.
    9:00 PM: Leisure and relaxation. Jake might spend this time reading a book, catching up on his favorite TV shows, or exploring new tech gadgets.
    10:30 PM: Wind-down routine. Jake prepares for bed, perhaps with some light stretching or meditation to relax before sleep.
    Night:
    10. 11:00 PM: Bedtime. Jake values a good night's sleep to ensure he's ready for the next day's challenges and adventures.

    Of course, the specifics can vary, and Jake might have days where work demands more of his time or weekends filled with photography excursions and socializing. Overall, Jake's day reflects a harmonious blend of his professional commitments, outdoor pursuits, and personal interests.




    User
    Can you create a realistic script of Jake in JC Penny talking to a salesperson to choose a shirt for work

    ChatGPT
    Scene: JC Penney Men's Clothing Section

    Salesperson: Good afternoon, sir! Is there anything specific you're looking for today?

    Jake: Hey there! Yeah, I'm actually in need of a couple of new shirts for work. Something that's professional but not too stuffy, you know?

    Salesperson: Of course! We've got a great selection of dress shirts right here. What's your preferred style and color?

    Jake: I usually lean towards a more modern, slim fit. As for colors, I'm thinking classic blues and whites. Maybe a subtle pattern, but nothing too flashy.

    Salesperson: Got it. We have some fantastic slim-fit options in those colors. Let me show you a couple of choices.

    (Salesperson takes Jake to the dress shirt section, presenting a few options.)

    Salesperson: Here's a classic light blue in a slim fit. It's breathable and perfect for the office. And we also have this white one with a subtle check pattern. Both are from our latest collection.

    Jake: Nice, I like these. How's the material? I prefer something that doesn't wrinkle easily.

    Salesperson: These shirts are made from a wrinkle-resistant cotton blend. You'll find them comfortable for long workdays, and they'll stay crisp throughout.

    Jake: Perfect, that's exactly what I need. What about the collar style? I usually go for a spread collar.

    Salesperson: You're in luck! Both of these have a spread collar, giving them a contemporary look that pairs well with ties or can be worn open for a more relaxed feel.

    Jake: Excellent. Let me try them on. Do you have a fitting room nearby?

    Salesperson: Right this way, sir. I'll get these shirts ready for you, and you can let me know if you need any other sizes or styles.

    (Jake tries on the shirts and returns to the sales floor.)

    Jake: These fit great! I'll take both of them. Do you have any ongoing promotions or discounts?

    Salesperson: Absolutely. We have a buy-one-get-one-half-off deal on dress shirts today. It looks like you've found two, so you'll get a nice discount on the second one.

    Jake: Awesome, that works for me. Thanks for your help!

    (Salesperson processes the purchase, and Jake leaves the store satisfied with his new shirts.)




    User
    What are the reasons Jake bought these shirts

    ChatGPT
    Jake decided to purchase the shirts at JC Penney for several reasons:

    Professional Yet Modern Style: Jake needed shirts that were suitable for work but not overly formal. The slim-fit design, classic colors (light blue and white), and subtle patterns offered by the shirts met his preference for a modern and professional look.

    Wrinkle-Resistant Material: Jake specifically asked about the material, expressing a preference for shirts that don't wrinkle easily. The salesperson assured him that the selected shirts were made from a wrinkle-resistant cotton blend, providing the practicality and comfort he desired for long workdays.

    Spread Collar Style: Jake mentioned his preference for spread collars, and the salesperson presented shirts with this specific collar style. The spread collar adds a contemporary touch, making the shirts versatile for both formal and more casual occasions.

    Fitting and Comfort: Jake took the time to try on the shirts in the fitting room, ensuring they fit well and were comfortable. This step was crucial for him to feel confident in his purchase.

    Promotional Discount: Learning about the ongoing promotion at JC Penney, where dress shirts were on a buy-one-get-one-half-off deal, influenced Jake's decision. The discount provided a cost-effective solution, encouraging him to buy both shirts and save money.

    In summary, Jake's purchase was driven by a combination of style preferences, practical features, comfort, and a good deal offered through a promotional discount. The overall shopping experience, including the helpful guidance from the salesperson, played a significant role in Jake's decision to buy the shirts at JC Penney.




    User
    Create a detailed review from Jake about his thoughts on wearing the shirts after 6 months

    ChatGPT
    Review: Jake Thompson's Experience with JC Penney Dress Shirts

    After six months of regular wear, I can confidently say that the dress shirts I purchased from JC Penney have exceeded my expectations in terms of style, comfort, and durability.

    Style and Professionalism:
    The shirts' slim-fit design and classic colors (light blue and white) continue to lend a modern and professional aesthetic to my work wardrobe. The subtle patterns add a touch of sophistication without being overly flashy, making these shirts versatile for various occasions. I've received numerous compliments on the look and fit, reinforcing my satisfaction with the style.

    Material and Comfort:
    One of my initial concerns was the durability of the wrinkle-resistant material, and I'm pleased to report that it has held up remarkably well. The shirts maintain their crispness throughout the day, even during long work hours and meetings. The fabric feels comfortable against the skin, and the shirts have retained their shape after multiple washes. The breathable cotton blend has proven to be a wise choice, especially during warmer weather.

    Collar Style and Versatility:
    The spread collar style has proven to be a key feature, allowing me to easily pair the shirts with ties for formal occasions or leave them open for a more relaxed look. This versatility has made them a staple in my wardrobe, seamlessly transitioning from the office to after-work events. The collar retains its shape, contributing to the shirts' overall polished appearance.

    Durability and Longevity:
    These shirts have endured regular wear and washing without showing signs of significant wear and tear. The stitching remains intact, and the color has not faded noticeably. The buttons are securely attached, and there hasn't been any shrinkage. The overall durability has certainly justified the investment, making them a reliable part of my work attire.

    Promotional Deal:
    The buy-one-get-one-half-off promotion I availed during the purchase was an added bonus. Not only did I get two high-quality shirts, but the promotional discount also made the deal more cost-effective. The shirts have proven to be an excellent value for the price, and the promotion further sweetened the deal.

    In conclusion, my experience with JC Penney dress shirts has been overwhelmingly positive. These shirts have become my go-to choice for professional and semi-formal occasions. From style to comfort to durability, they have consistently met and even exceeded my expectations. I highly recommend JC Penney dress shirts to anyone seeking a reliable and stylish addition to their wardrobe.
"""


if __name__ == "__main__":
    current_ava = input("Type 0 if you want the chat to act as you, 1 if as Elon Mask and 2 if as ChatGPT ")
    asif = ["Mimic","Elon Musk","ChatGPT"]
    curr_ava = asif[int(current_ava)]
    while True:
        science_tutoring()
# [END aiplatform_sdk_chat]

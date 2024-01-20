
import tweepy
import openai
import time

# Add your Twitter API credentials
consumer_key = 'consumer key here'
consumer_secret = 'consumer secret here'
access_token = 'access token here'
access_token_secret = 'access token secret here'

# Set your OpenAI API key
openai.api_key = 'open api key here'

# Authenticate with your credentials
client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)


# Function to generate tweet content using GPT-3.5
def generate_tweet_content(prompt):
    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=100,
        n=1,
        temperature=0.9
    )
    return response.choices[0].text.strip()


# Function to post a tweet
def post_tweet():
    # Generate propmpt
    tweet_content = generate_tweet_content("put your chatgpt prompt here")
# Assuming tweet_content is the generated text

    MAX_TWEET_LENGTH = 250  # Twitter's character limit
# Truncate the tweet content if it exceeds the character limit
# this part needs work it cuts off text
    tweet_content = tweet_content[:MAX_TWEET_LENGTH]

    # Post the generated content as a tweet
    response = client.create_tweet(text=tweet_content)
    tweet_url = f"https://twitter.com/user/status/{response.data['id']}"
    print(f"Tweet posted successfully: {tweet_content}\nTweet URL: {tweet_url}")

# Main loop to tweet every hour
while True:
    post_tweet()
    time.sleep(3600)  # Sleep for 30mins (1800 seconds)

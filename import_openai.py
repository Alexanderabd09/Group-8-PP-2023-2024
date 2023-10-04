import openai

# Replace 'your-api-key' with your actual API key
api_key = 'your-api-key'

# The text you want to rephrase
original_text = "The quick brown fox jumps over the lazy dog."

# Make an API call
response = openai.Completion.create(
    engine="davinci",
    prompt=original_text,
    max_tokens=50,  # Adjust the number of tokens as needed
    api_key=api_key
)

# Get the rephrased text from the API response
rephrased_text = response.choices[0].text

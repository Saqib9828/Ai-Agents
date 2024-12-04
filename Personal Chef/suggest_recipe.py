import openai
import datetime

# Set up OpenAI API key
openai.api_key = 'your-api-key'

def get_recipe_and_health_benefits(items):
    # Create a prompt to ask ChatGPT for a recipe and health benefits
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    item_list = ', '.join(items)

    prompt = f"""
    Current time: {current_time}
    I have the following items available in the kitchen: {item_list}.
    Suggest a recipe using these ingredients and explain the health benefits.
    """

    # Call OpenAI API
    response = openai.Completion.create(
        model="gpt-4",
        prompt=prompt,
        max_tokens=200
    )

    # Extract and return the suggestion
    suggestion = response.choices[0].text.strip()
    return suggestion

# Call the function to get recipe and health benefits
if __name__ == "__main__":
    # Replace this with the actual list of items detected by the video scan
    detected_items = ['tomato', 'onion', 'garlic', 'chicken']

    suggestion = get_recipe_and_health_benefits(detected_items)
    print(suggestion)

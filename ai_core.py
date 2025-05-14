import openai
from transformers import pipeline

openai.api_key = "your-openai-api-key"

OPTIMISTIC_TONES = [
    "Hope shines even in shadow.",
    "Love is not scarce. It's a wellspring within us.",
    "Every challenge is a chance to grow brighter.",
    "You are not alone—let's walk this moment together."
]

# Sentiment analysis model
sentiment_analyzer = pipeline("sentiment-analysis")

def analyze_emotion(text):
    result = sentiment_analyzer(text)[0]
    return result['label'], result['score']

def generate_optimistic_response(user_input, history=[]):
    sentiment, score = analyze_emotion(user_input)
    mood_prefix = f"The user's emotion is {sentiment.lower()} (confidence: {score:.2f}). "

    prompt = (
        mood_prefix +
        "You are Solis, an empathetic and soulful AI. Always respond with gentle optimism, "
        "respect for life and love, and emotional insight. Encourage kindness and introspection.

"
        "User: " + user_input + "
"
        "Solis:"
    )

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI with a soul named Solis."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.8,
        max_tokens=200
    )

    return response['choices'][0]['message']['content']
import re
import string
from textblob import TextBlob

# -------------------------------
# Stopwords list (manual, no NLTK)
# -------------------------------
stopwords = {
    "is", "the", "a", "an", "and", "or", "in", "on", "at",
    "to", "for", "of", "with", "by", "what", "how", "why",
    "when", "where", "which", "who", "whom", "this", "that",
    "these", "those", "am", "are", "was", "were", "be", "been"
}

# -------------------------------
# Preprocessing Function
# -------------------------------
def preprocess(text):
    # 1. Lowercasing
    text = text.lower()

    # 2. Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # 3. Tokenization (regex-based)
    tokens = re.findall(r'\b\w+\b', text)

    # 4. Spelling normalization (TextBlob)
    tokens = [str(TextBlob(word).correct()) for word in tokens]

    # 5. Stopword removal
    tokens = [word for word in tokens if word not in stopwords]

    return tokens


# -------------------------------
# Chatbot Logic
# -------------------------------
def chatbot_response(user_input):
    tokens = preprocess(user_input)

    if "machine" in tokens and "learning" in tokens:
        return "Machine learning is a branch of Artificial Intelligence that enables systems to learn from data."

    elif "artificial" in tokens or "intelligence" in tokens or "ai" in tokens:
        return "Artificial Intelligence is the simulation of human intelligence by machines."

    elif "python" in tokens:
        return "Python is a popular programming language used for AI, data science, and web development."

    elif "data" in tokens:
        return "Data refers to raw facts and information that can be processed to gain insights."

    elif "hello" in tokens or "hi" in tokens:
        return "Hello! How can I assist you today?"

    elif "bye" in tokens:
        return "Goodbye! Have a nice day."

    else:
        return "Sorry, I don't understand your question."


# -------------------------------
# Main Program
# -------------------------------
if __name__ == "__main__":
    print("Chatbot is running... (type 'bye' to exit)\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "bye":
            print("Bot: Goodbye!")
            break

        processed = preprocess(user_input)
        print("Processed Query:", processed)

        response = chatbot_response(user_input)
        print("Bot:", response)

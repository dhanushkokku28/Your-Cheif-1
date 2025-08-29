# Zero-shot prompting example using OpenAI's API

import openai

openai.api_key = "AIzaSyAGd5qIMc-JGrRAjx3Q8iswDi2TxNeqbqQ"  # Replace with your actual API key

def get_answer(context, question):
    # Dynamic prompt construction
    prompt = f"Based on the following context, answer the question:\n\nContext: {context}\n\nQuestion: {question}\nAnswer:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=60,
        temperature=0.5
    )
    # Log the number of tokens used
    if hasattr(response, 'usage'):
        print(f"Tokens used: {response.usage['total_tokens']}")
    else:
        print("Token usage information not available.")
    return response.choices[0].text.strip()

# Example usage
context = "Artificial intelligence is a field of computer science that focuses on creating systems capable of performing tasks that typically require human intelligence."
question = "What does artificial intelligence focus on?"

answer = get_answer(context, question)
print("Answer:", answer)

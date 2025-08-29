# Zero-shot prompting example using OpenAI's API

import openai

openai.api_key = "AIzaSyAGd5qIMc-JGrRAjx3Q8iswDi2TxNeqbqQ"  # Replace with your actual API key

def get_answer(context, question):
    # Dynamic prompt construction with structured output instruction
    prompt = (
        f"Based on the following context, answer the question in JSON format with keys 'answer' and 'confidence' (confidence is a number between 0 and 1):\n\n"
        f"Context: {context}\n\nQuestion: {question}\nJSON:"
    )
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=80,
        temperature=0.7,
        top_p=0.9,
        top_k=50,
        stop=["\n\n", "\nJSON:"]  # Added stop sequences to control output
    )
    # Log the number of tokens used
    if hasattr(response, 'usage'):
        print(f"Tokens used: {response.usage['total_tokens']}")
    else:
        print("Token usage information not available.")
    # Parse the JSON output
    import json
    try:
        structured = json.loads(response.choices[0].text.strip())
    except Exception as e:
        print("Failed to parse JSON:", e)
        structured = {"answer": response.choices[0].text.strip(), "confidence": None}
    return structured

# Example usage
context = "Artificial intelligence is a field of computer science that focuses on creating systems capable of performing tasks that typically require human intelligence."
question = "What does artificial intelligence focus on?"

result = get_answer(context, question)
print("Structured Answer:", result)

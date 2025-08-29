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

def get_embedding(text, model="text-embedding-ada-002"):
    """
    Generate an embedding vector for the given text using OpenAI's embedding API.
    """
    response = openai.Embedding.create(
        input=text,
        model=model
    )
    embedding = response['data'][0]['embedding']
    print(f"Embedding for '{text}':", embedding)
    return embedding

# System prompt (for use with chat-based models or as documentation/context)
SYSTEM_PROMPT = (
    "You are an intelligent assistant. Your task is to answer user questions using only the information provided in the context. "
    "Always respond in JSON format with the keys 'answer' and 'confidence' (confidence is a number between 0 and 1)."
)

def build_user_prompt(context, question):
    """
    Builds a user prompt using the RTFC framework.
    """
    return (
        f"Based on the following context, answer the question in JSON format with keys 'answer' and 'confidence' (confidence is a number between 0 and 1):\n\n"
        f"Context: {context}\n\nQuestion: {question}\nJSON:"
    )

def get_answer_one_shot(context, question):
    # One-shot prompt with a single example
    example_context = (
        "Machine learning is a subset of artificial intelligence that focuses on building systems that learn from data."
    )
    example_question = "What is machine learning?"
    example_answer = {
        "answer": "Machine learning is a subset of AI focused on systems that learn from data.",
        "confidence": 0.95
    }
    prompt = (
        "Based on the following context, answer the question in JSON format with keys 'answer' and 'confidence' (confidence is a number between 0 and 1):\n\n"
        f"Context: {example_context}\n"
        f"Question: {example_question}\n"
        f"JSON: {example_answer}\n\n"
        f"Context: {context}\n"
        f"Question: {question}\nJSON:"
    )
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=80,
        temperature=0.7,
        top_p=0.9,
        top_k=50,
        stop=["\n\n", "\nJSON:"]
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

user_prompt = build_user_prompt(context, question)
print("System Prompt:", SYSTEM_PROMPT)
print("User Prompt:", user_prompt)

# Example usage
result = get_answer(context, question)
print("Structured Answer:", result)

# Example usage for embeddings
sample_text = "Artificial intelligence enables machines to learn from data."
embedding_vector = get_embedding(sample_text)

# Example usage for one-shot prompting
result_one_shot = get_answer_one_shot(context, question)
print("One-Shot Structured Answer:", result_one_shot)

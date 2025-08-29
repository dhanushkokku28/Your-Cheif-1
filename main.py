# Zero-shot prompting example using OpenAI's API

import openai

openai.api_key = "AIzaSyAGd5qIMc-JGrRAjx3Q8iswDi2TxNeqbqQ"

prompt = "Summarize the following paragraph:\n\nArtificial intelligence is a field of computer science that focuses on creating systems capable of performing tasks that typically require human intelligence. These tasks include learning, reasoning, problem-solving, perception, and language understanding."

response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=60,
    temperature=0.5
)

print("Summary:", response.choices[0].text.strip())
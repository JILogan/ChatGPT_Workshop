import openai
# Set the API key
openai.api_key = "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"
# Use the ChatGPT model to generate text
model_engine = "text-davinci-003"
prompt = "write me a song"
completion = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=1024, n=1,stop=None,temperature=0.7)
message = completion.choices[0].text
print(message)

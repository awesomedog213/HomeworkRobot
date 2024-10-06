from openai import OpenAI
import os
import time

ASSISTANT_ID = "asst_Ag25e9ln5YGYFxnc5YCZmkwl"
client = OpenAI()
# Get API key
client.api_key = os.getenv("OPENAI_API_KEY")

# Define the parameters for your request
thread = client.beta.threads.create(
    messages=[{"role": "user",
               # Prompt:
               "content": """What are the anti-federalists' ideas about the constituiton? Explain your answer in 2-3 sentences"""}],
)


# Create Run
run = client.beta.threads.runs.create(
    thread_id=thread.id, assistant_id=ASSISTANT_ID)
print(f"👉 Run Created: {run.id}")

# Wait for run to complete.
while run.status != "completed":
    run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
    print(f"🏃 Run Status: {run.status}")
    time.sleep(0.01)
else:
    print(f"🏁 Run Completed!")

# Get the latest message from the thread.
message_response = client.beta.threads.messages.list(thread_id=thread.id)
messages = message_response.data

# Print the latest message.
latest_message = messages[0]
print(f"💬 Response: {latest_message.content[0].text.value}")

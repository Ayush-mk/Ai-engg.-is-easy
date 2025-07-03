import requests

API_KEY = "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"
API_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "meta-llama/llama-4-scout-17b-16e-instruct"

messages = []

def completion(message):
    global messages
    messages.append({
        "role": "user",
        "content": message
    })

    response = requests.post(
        API_URL,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        },
        json={
            "model": MODEL,
            "messages": messages
        }
    )

    if response.status_code == 200:
        assistant_reply = response.json()['choices'][0]['message']['content']
        messages.append({
            "role": "assistant",
            "content": assistant_reply
        })
        print(f"Friday: {assistant_reply}")
    else:
        print("❌ Error:", response.status_code, response.text)

if __name__ == "__main__":
    print("Friday: Hello sir, mera name Friday hai, mai apki kya madat ker sakta hu." \
    "\n")
    while True:
        user_question = input("You: ")
        completion(user_question)

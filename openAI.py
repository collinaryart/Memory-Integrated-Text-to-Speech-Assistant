import openai
import json

openai.api_key = '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'

def query_openai_api(query):
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": query}]
    )
    return response.choices[0].message['content']

def save_query_response_pair(query, response):

    with open('query_response_db.json', 'a') as file:
        json.dump({query: response}, file, indent=4)

def handle_query(query):
    response = query_openai_api(query)
    save_query_response_pair(query, response)
    return response

# Example usage
query = "What's the weather like today?"
response = handle_query(query)
print(response)

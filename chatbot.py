import requests
import json
import os
from dotenv import load_dotenv
from prompt_enhance import quiz
from prompt_enhance import pdf_to_text
from prompt_enhance import ppt_to_text

load_dotenv(dotenv_path=r"...\api_key.env")

api_key = os.getenv("API_KEY")
model = "claude-v1.3-100k"
conversation_history = ""

def chat_with_ai(user_question, api_key, model):
    global conversation_history
    url = 'https://api.anthropic.com/v1/complete'
    headers = {
        'Content-Type': 'application/json',
        'X-API-Key': api_key,
    }
    params = {
        'prompt': f'{conversation_history}\n\nHuman: {user_question}\n\nAssistant:',
        'model': model,
        'max_tokens_to_sample': 4000,
        'stop_sequences': ['\n\nHuman:'],
        'temperature': 0.8,
        'top_p': -1,
        'metadata': {}
    }
    params_json = json.dumps(params)
    response = requests.post(url, headers=headers, data=params_json)
    if response.status_code == 200:
        response_json = response.json()
        # conversation_history += f'\n\n{response_json["completion"]}'
        conversation_history = f'\n\n{response_json["completion"]}'
        return conversation_history
    else:
        return f'Error: {response.status_code}'

def chatbot(topic, task_type, learning_pace):
    if task_type==1:
        count=0
        while True:
            if count==0:
                prompt="Prompt: Hello there, I would like to learn about "+topic+" at "+learning_pace+" level."
                count+=1
            else:
                prompt=input("Prompt: ")
            if prompt=="quit()":
                break
            response = chat_with_ai(prompt, api_key, model)
            print("Response:", response.lstrip(), end="\n \n")

    elif task_type==2:
        count=0
        while True:
            if count==0:
                prompt="Can you give me an MCQ quiz on "+topic+"which is of"+learning_pace+ "level. Display answer like Answer"
                count+=1
            else:
                prompt=input("Prompt: ")
            if prompt=="quit()":
                break
            response = chat_with_ai(prompt, api_key, model)
            quiz_prompt=response.lstrip()
            quiz(quiz_prompt)

    elif task_type==3:
        while True:
            file_type=input("Enter file type (pdf/ppt): ")
            if file_type=="pdf":
                text=pdf_to_text()
                prompt="Can you give me a "+learning_pace+" level brief summary of this text - "+text
            else:
                text=ppt_to_text()
                prompt="Can you give me a "+learning_pace+" level brief summary of this text - "+text
            if prompt=="quit()":
                break
            response = chat_with_ai(prompt, api_key, model)
            print("Response:", response.lstrip(), end="\n \n")

    elif task_type==4:
        count=0
        while True:
            if count==0:
                prompt="Prompt: Hello there, please give me a roadmap for the topic "+topic+" at "+learning_pace+" level."
                count+=1
            else:
                prompt=input("Prompt: ")
            if prompt=="quit()":
                break
            response = chat_with_ai(prompt, api_key, model)
            print("Response:", response.lstrip(), end="\n \n")



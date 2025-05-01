import requests

############ Envia mensagem do usuário para a IA e obtém resposta ###################3
def write_message(user_message):
    GEMINI_API_KEY = 'AIzaSyAapgYiz6-jsS0vY3I9twYR3RFyLFYKB9o'
    URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"

    headers = {
        "Content-Type": "application/json",

    }
    payload = {
        "contents": [{
        "parts":[{"text": user_message}]
    }]
    }

    response = requests.post(URL, json=payload, headers=headers)
    print("Status code:", response.status_code)

    return response.json()['candidates'][0]['content']['parts'][0]['text']
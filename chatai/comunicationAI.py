import textwrap
import google.generativeai as genai
from IPython.display import Markdown

#Formata o texto em markdown.
def to_markdown(text):
    text = text.replace('•', ' *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

#Configurando a API do Gemini
GOOGLE_API_KEY = "AIzaSyAdA9WzD5esnXGDK2bH6woTi47Dn_W38KA"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

#Registra as conversas em uma lista.
history_chat = []

#Looping do chat.
while True: 
    user_text = input("Digite o que deseja conversar com a IA: \n \n" )

    if user_text == "sair":
        break
    
#Relaciona o histórico da conversa com as futuras.
    else:
        history_chat.append({'user_ask': user_text})

        response = model.generate_content(user_text)
        response_txt = response.text

        history_chat[-1]['AI_response'] = response_txt
        print(response_txt)
        


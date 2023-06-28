import openai
import gradio

openai.api_key = "####"

messages = [{"role": "system", "content": "You are an Nobel-prize winning researcher with a research focus on artificial intelligence, artificial intelligence and supply chain management"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Dr. Goldston's Chatbot")

demo.launch(share=True)

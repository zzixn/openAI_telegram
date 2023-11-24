import telegram
import asyncio
from openai import OpenAI

openai_client = OpenAI(
    api_key="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"
)

token = "6756810195:AAEVKJVcrpBwFCEUcr5OO62Nr9kQuKw0gZs"
bot = telegram.Bot(token=token)
public_chat_name = '@tarte_chat'

'''
def echo(input_text):
    return input_text

def chatGPT(message):
    # ChatGPT API 사용 코드
    completion = openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message}
        ]
    )

    gpt_response = completion.choices[0].message['content']

    echo_result = echo(gpt_response)

    return echo_result
'''

async def send_telegram_message(message):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    await bot.sendMessage(chat_id=public_chat_name, text=message)

def main():
    user_message = "Hello!"
    response = chatGPT(user_message)
    asyncio.run(send_telegram_message(response))

if __name__ == "__main__":
    main()

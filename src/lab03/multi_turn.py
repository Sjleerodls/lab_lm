from openai import OpenAI

from src.utils import get_openai_api_key


def get_gpt_response(client, messages):
    response = client.chat.completions.create(
        model = 'gpt-4o-mini',
        temperature = 0.9,
        messages=messages
    )
    return response.choices[0].message.content


def main():
    client = OpenAI(api_key=get_openai_api_key())

    messages = [{'role':'system', 'content':'너는 뛰어난 비서야. 이 세상 모든 정보의 집합체이지. 내 질문에 잘 답변해줘.'}]

    while True:
        user_input = input('사용자 :')

        if user_input == 'exit':
            break

        messages.append({'role':'user', 'content':user_input})

        response = client.chat.completions.create(
            model='gpt-4o-mini',
            temperature=0.9, top_p=0.7,
            messages=messages
        )

        assistant_reply = response.choices[0].message.content
        print(assistant_reply)

        messages.append({'role':'assistant', 'content':assistant_reply})

if __name__ == '__main__':
    main()
import streamlit as st
from openai import OpenAI
from src.utils import get_openai_api_key


def initialize_client():
    api_key = get_openai_api_key()
    if not api_key:
        st.info('API 키가 없습니다.')
        st.stop()

    client = OpenAI(api_key=api_key)

    return client


def get_gpt_response(client, messages):
    response = client.chat.completions.create(
        model = 'gpt-4o-mini',
        temperature = 0.9,
        messages = messages
    )

    return response.choices[0].message.content



def main():
    client = initialize_client()

    st.title('나는 지피티다.')
    st.write('질문해라 닝겐')

    messages = [
        {'role':'user', 'content': '질문'}
    ]

    for msg in messages:
        st.chat_message(msg['role']).write(msg['content'])

    user_input = st.chat_input('질문을 입력하세요.')
    if user_input:
        st.chat_message('user').write(user_input)
        messages.append({'role':'user', 'content': user_input})

        st.chat_message('assistant').write(f'답변 - {user_input}')
        messages.append({'role':'assistant', 'content': f'답변 - {user_input}'})



if __name__ == "__main__":
    main()
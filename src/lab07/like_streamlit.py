import streamlit as st

def main():
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

        st.chat_message('assistant').write(f'')





if __name__ == "__main__":
    main()
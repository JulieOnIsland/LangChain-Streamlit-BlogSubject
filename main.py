# from dotenv import load_dotenv
# load_dotenv()
from langchain_openai import ChatOpenAI
import streamlit as st

llm = ChatOpenAI()

st.title('AI가 제안하는 블로그 주제')

content = st.text_input('어떤 블로그 주제가 좋을까요?')

# print(result)

if st.button('주제 제안받기'):
    with st.spinner('주제 고민 중...'):
        result = llm.invoke(content + "에 대한 블로그 주제를 써줘")
        st.write(result)
    

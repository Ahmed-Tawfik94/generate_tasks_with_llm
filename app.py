from langchain_core.pydantic_v1 import BaseModel, Field,validator
from langchain_core.prompts import ChatPromptTemplate , PromptTemplate
from langchain_core.output_parsers import JsonOutputParser , StrOutputParser

# from langchain_core.messages import HumanMessage, SystemMessage
# from langchain_core.prompts.chat import (
#     ChatPromptTemplate,
#     HumanMessagePromptTemplate,
#     SystemMessagePromptTemplate,
#     AIMessage
# )
import json , re
import demjson3
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain_openai import ChatOpenAI, OpenAI
from chains import first_prompt, second_prompt, third_prompt,forth_prompt ,initail_prompt
import streamlit as st

# initialize llm 
top_p= 1.0
frequency_penalty= 0.0
presence_penalty= 0.0
model_name=['gpt-3.5-turbo','gpt-4-turbo-preview']


# json_parser= JsonOutputParser(pydantic_object=Lesson)
parser= StrOutputParser()

import streamlit as st
import os

# App title
st.set_page_config(page_title="Generate tasks with llm")

# openai Credentials
with st.sidebar:
    st.title('Generate tasks with llm')
    if 'openai_api_key' in st.secrets:
        st.success('API key already provided!', icon='✅')
        openai_api_key = st.secrets['openai_api_key']
    else:
        openai_api_key = st.text_input('Enter openai API token:', type='password')
        if not (openai_api_key):
            st.warning('Please enter your credentials!', icon='⚠️')
        else:
            st.success('Proceed to entering your prompt message!', icon='👉')

    # Refactored from https://github.com/a16z-infra/llama2-chatbot
    st.subheader('Models and parameters')
    selected_model = st.sidebar.selectbox('Choose a model', model_name, key='selected_model')
    if selected_model == model_name[0]:
        llm = ChatOpenAI(model=model_name[0],
                openai_api_key=openai_api_key,
                model_kwargs={
                "frequency_penalty":0.0,
                "presence_penalty":0.0})
    elif selected_model == model_name[1]:
        llm = ChatOpenAI(model=model_name[1],
                openai_api_key=openai_api_key,
                model_kwargs={
                "frequency_penalty":0.0,
                "presence_penalty":0.0})
    
    temperature = st.sidebar.slider('temperature', min_value=0.0, max_value=5.0, value=0.1, step=0.01)
    top_p = st.sidebar.slider('top_p', min_value=0.0, max_value=1.0, value=0.9, step=0.01)
    max_length = st.sidebar.slider('max_length', min_value=64, max_value=4096, value=3400, step=8)
    if temperature:
        llm.temperature = temperature
    if top_p:
        llm.model_kwargs['top_p'] =top_p
    if max_length:
        llm.max_tokens=max_length
os.environ['openai_api_key'] = openai_api_key

# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]

# Display or clear chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]
st.sidebar.button('Clear Chat History', on_click=clear_chat_history)

# Function for generating LLaMA2 response
def generate_llm_response(course,lesson):
    string_dialogue=''
    for dict_message in st.session_state.messages:
        if dict_message["role"] == "user":
            string_dialogue += "User: " + dict_message["content"] + "\n\n"
        else:
            string_dialogue += "Assistant: " + dict_message["content"] + "\n\n"
    chain_one = LLMChain(llm=llm,prompt=first_prompt, 
                     output_key="lecture"
                    )
    chain_two = LLMChain(llm=llm,prompt=second_prompt, 
                     output_key="quizzes"
                    )
    chain_three = LLMChain(llm=llm,prompt=third_prompt,
                       output_key="practice_code", )
    chain_four = LLMChain(llm=llm,prompt=forth_prompt,
                       output_key="final_output", 
                      )
    chains=[chain_one, chain_two, chain_three,chain_four]
    overall_chain = SequentialChain(
    chains=chains,
    input_variables=["course","lesson"],
    output_variables=["lecture", "quizzes","practice_code","final_output"],

)    
    output=overall_chain.invoke({"course":course,"lesson":lesson})
    return output

# User-provided prompt
# if prompt := st.chat_input(disabled=not openai_api_key):
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with st.chat_message("user"):
#         st.write(prompt)
course= st.text_input('Enter Course name',value="Prompt Engineering")
lesson= st.text_input('Enter Lesson name', value="introduction to prompt engineering with open ai")
if generate:=st.button('Generate ✨'):
    st.session_state.disabled = False
    if course and lesson:
        st.session_state.messages.append({"role": "user", "content": initail_prompt.format(course=course,lesson=lesson)})
        with st.chat_message("user"):
                st.write(initail_prompt.format(course=course,lesson=lesson))
# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = generate_llm_response(course,lesson)
            try:
                response['lecture']=json.loads(response['lecture'])
                response['lecture']
                response['quizzes'] = re.sub(r'\b\d+\.\s*\n', '', response['quizzes'])
                response['quizzes']=json.loads(response['quizzes'])
                response['quizzes']
                response['practice_code'] = json.loads(response['practice_code'])
                response['practice_code']
                response['final_output']=json.loads(response['final_output'])
                response['final_output']
                json_output = demjson3.encode(response)
            except  Exception as e:
                print(e)
            placeholder = st.empty()
            full_response = ''
            # for item in response:
            #     full_response += item
            #     placeholder.markdown(full_response)
            # placeholder.markdown(json_output)
            filename="json_output.json"
            st.json(json_output)
    message = {"role": "assistant", "content": response}
    st.session_state.messages.append(message)
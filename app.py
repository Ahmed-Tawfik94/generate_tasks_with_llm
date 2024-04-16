from langchain_core.pydantic_v1 import BaseModel, Field,validator
from langchain_core.prompts import ChatPromptTemplate , PromptTemplate
from langchain_core.output_parsers import JsonOutputParser , StrOutputParser
import tiktoken
# from langchain_core.messages import HumanMessage, SystemMessage
# from langchain_core.prompts.chat import (
#     ChatPromptTemplate,
#     HumanMessagePromptTemplate,
#     SystemMessagePromptTemplate,
#     AIMessage
# )
import json , re
import pprint
import demjson3
from models.shared import Hint
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain_openai import ChatOpenAI, OpenAI
# from langchain_anthropic import ChatAnthropic
from utils.chains import first_prompt, second_prompt, third_prompt,forth_prompt ,initail_prompt
import streamlit as st
from utils.utils import is_valid_json
# initialize llm 
top_p= 1.0
frequency_penalty= 0.0
presence_penalty= 0.0
model_name={
    'GPT-3.5':"gpt-3.5-turbo",
    "GPT-4":'gpt-4-turbo-preview',
    "Claude3 opus":'claude-3-opus-20240229',
    "Claude3 Sonnet":'claude-3-sonnet-20240229',
    "Claude3 Haiku":'claude-3-haiku-20240307'
    }



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
        anthropic_api_key = st.secrets['anthropic_api_key']
    else:
        openai_api_key = st.text_input('Enter openai API token:', type='password')
        if not (openai_api_key):
            st.warning('Please enter your credentials!', icon='⚠️')
        else:
            st.success('Proceed to entering your prompt message!', icon='👉')

    # Refactored from https://github.com/a16z-infra/llama2-chatbot
    st.subheader('Models and parameters')
    selected_model = st.sidebar.selectbox('Choose a model', model_name.keys(), key='selected_model')
    if selected_model =='GPT-3.5':
        llm = ChatOpenAI(model=model_name['GPT-3.5'],
                openai_api_key=openai_api_key,
                model_kwargs={
                "frequency_penalty":0.0,
                "presence_penalty":0.0})
    elif selected_model =="GPT-4":
        llm = ChatOpenAI(model=model_name["GPT-4"],
                openai_api_key=openai_api_key,
                model_kwargs={
                "frequency_penalty":0.0,
                "presence_penalty":0.0})
    # elif selected_model=="Claude3 opus":
    #     llm=chat = ChatAnthropic(temperature=0, model_name=model_name["Claude3 opus"],anthropic_api_key=anthropic_api_key)
    # elif selected_model=="Claude3 Sonnet":
    #     llm=chat = ChatAnthropic(temperature=0, model_name=model_name["Claude3 Sonnet"],anthropic_api_key=anthropic_api_key)
    # elif selected_model=="Claude3 Haiku":
    #     llm=chat = ChatAnthropic(temperature=0, model_name=model_name["Claude3 Haiku"],anthropic_api_key=anthropic_api_key)
    # tokeniser= tiktoken.get_encoding(model_name[selected_model])
    # encoding = tokeniser.encoding_for_model(model_name[selected_model])
    # print(f'{encoding}')
    temperature = st.sidebar.slider('temperature', min_value=0.0, max_value=5.0, value=0.1, step=0.01)
    top_p = st.sidebar.slider('top_p', min_value=0.0, max_value=1.0, value=1.0, step=0.01)
    max_length = st.sidebar.slider('max_length', min_value=64, max_value=4096, value=3600, step=8)
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

def generate_llm_response(course,lesson):
    string_dialogue=''
    for dict_message in st.session_state.messages:
        if dict_message["role"] == "user":
            string_dialogue += "User: " + dict_message["content"] + "\n\n"
        else:
            string_dialogue += "Assistant: " + dict_message["content"] + "\n\n"
    # prompt_tokens = len(encoding.encode(first_prompt.messages[0].prompt.format_prompt(course=course,lesson=lesson).to_string()))
    # print(prompt_tokens)
    # llm.max_tokens = 4096 - prompt_tokens
    chain_one = LLMChain(llm=llm,prompt=first_prompt, 
                     output_key="lecture"
                    )
    chain_two = LLMChain(llm=llm,prompt=second_prompt, 
                     output_key="quiz"
                    )
    print('*'*100)
    pprint.pprint(second_prompt)
    print('*'*100)
    pprint.pprint(chain_two)
    print('*'*100)
    chain_three = LLMChain(llm=llm,prompt=third_prompt,
                       output_key="practice_code", )
    chain_four = LLMChain(llm=llm,prompt=forth_prompt,
                       output_key="final_output", 
                      )
    chains=[chain_one, chain_two, chain_three]
    overall_chain = SequentialChain(
    chains=chains,
    input_variables=["course","lesson"],
    output_variables=["lecture", "quiz","practice_code"],

)    
    return overall_chain.invoke({"course":course,"lesson":lesson})

# User-provided prompt
# if prompt := st.chat_input(disabled=not openai_api_key):
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with st.chat_message("user"):
#         st.write(prompt)
course= st.text_input('Enter Course name',value="Prompt Engineering")
lesson= st.text_input('Enter Lesson name', value="introduction to prompt engineering with open ai")
if generate:=st.button('Generate ✨'):
    st.session_state.disabled = True
    if course and lesson:
        st.session_state.messages.append({"role": "user", "content": initail_prompt.format(course=course,lesson=lesson)})
        with st.chat_message("user"):
                st.write(initail_prompt.format(course=course,lesson=lesson))
# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            json_output= None
            full_response = ''
            placeholder = st.empty()
            response=None
            try:
                response = generate_llm_response(course,lesson)
                if is_valid_json(response['lecture']):
                    response['lecture']=json.loads(response['lecture'])
                if is_valid_json(response['quiz']):
                    response['quiz'] = re.sub(r'\b\d+\.\s*\n', '', response['quiz'])
                    response['quiz']=json.loads(response['quiz'])
                else:
                    print(response['quiz'])
                # for q in response['quiz']['tasks']:
                #     q['metadata']['hints'].append(Hint(text=q['metadata']['questions']['hint'],cost=0.1)) 
                if is_valid_json(response['practice_code']):
                    response['practice_code'] = json.loads(response['practice_code'])
                if type(response) == dict:
                    json_output = {
                    "course":course,
                    "module":"",
                    "lesson":lesson,
                    "tasks":[
                        response['lecture'],
                        *response['quiz']['tasks'],
                        *response['practice_code']['tasks']
                    ]
                }
                else:
                    json_output = demjson3.encode(response)
                filename="json_output.json"
                st.json(json_output)
                with open(filename, 'w') as json_file:
                    json.dump(json_output, json_file, indent=4)
                message = {"role": "assistant", "content": json.dumps(response)}
                st.session_state.messages.append(message)
            except Exception as e:
                # json_part = str(e).split(" - ", 1)
                # if len(json_part) > 1:
                #     json_part=str(json_part[1])
                # else:
                #     json_part=str(json_part[0])
                # # Convert the JSON part to a dictionary
                # error_json = json.loads(json_part)
                placeholder.error(str(e))
                
                message = {"role": "assistant", "content": str(e)}
                st.session_state.messages.append(message)
from langchain_core.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
initail_prompt="create a lecture about {course} focusing on {lesson} in relation to large language models."
from schemas import lecture_schema ,quiz_schema, python_code_schema
first_prompt = ChatPromptTemplate.from_template(
   initail_prompt+"  output should be following this schema {schema}", partial_variables={"schema":lecture_schema}
)


second_prompt = ChatPromptTemplate.from_template(
    "now based on the {lecture} provided create a 3 questions with 4 choices if a question have multiple answer set multi_choice key to true else is false.based on this schema {schema} each question should be an item in the array of objects returned output should be a json format", partial_variables={"schema":quiz_schema}
)


third_prompt = ChatPromptTemplate.from_template(
  """now based on the {lecture} create at least three practice coding questions to help students enhance their understanding following the schema provided below 
{schema}
in the precode key  give a starter code for open ai API examples. output should be an array of questions formated in json 
""",  partial_variables={"schema":python_code_schema}
)
# chain 3: input= Review and output= language

# prompt template 3: translate to english
forth_prompt = ChatPromptTemplate.from_template(
  """now add the previous {lecture} output and the {quizzes} to the final output should be json"""
)
# chain 3: input= Review and output= language

from langchain_core.prompts.chat import (
    ChatPromptTemplate,
    # HumanMessagePromptTemplate,
    # SystemMessagePromptTemplate,
)
from langchain_core.output_parsers import JsonOutputParser,PydanticOutputParser
from models.lecture import Lecture
from models.quiz import QuizList
from models.python_code import CodePythonList
lecture_parser= JsonOutputParser(pydantic_object=Lecture)
initail_prompt="create a lecture about {course} focusing on {lesson} in relation to large language models."
# from models.schemas import lecture_schema ,quiz_schema, python_code_schema
first_prompt = ChatPromptTemplate.from_template(
   initail_prompt+"  output should be following this schema {schema}", partial_variables={"schema":lecture_parser.get_format_instructions()}
)

quiz_parser= PydanticOutputParser(pydantic_object=QuizList)
second_prompt = ChatPromptTemplate.from_template(
    """now based on the {lecture} provided create at least three different quizzes each quiz has an array with one question inside it.{schema}""",
      partial_variables={"schema":quiz_parser.get_format_instructions()}
)

python_code_parser= JsonOutputParser(pydantic_object=CodePythonList)
third_prompt = ChatPromptTemplate.from_template(
"""now based on the {lecture} create at least three practice coding questions to help students enhance their understanding following the schema provided. in the precode key  give a starter code for open ai API examples.{schema}
""",  partial_variables={"schema":python_code_parser.get_format_instructions()}
)
# chain 3: input= Review and output= language

# prompt template 3: translate to english
forth_prompt = ChatPromptTemplate.from_template(
  """now add the previous {lecture} output and the {quizzes} to the final output should be json"""
)
# chain 3: input= Review and output= language

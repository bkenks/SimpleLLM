'''
    Practice application of a simple llm
'''

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

MODEL = ChatOpenAI(model="gpt-4")
PARSER = StrOutputParser()
MESSAGES = [
    SystemMessage(content="Translate the following from English to Italian"),
    HumanMessage(content="Hi!"),
]
SYSTEM_TEMPLATE = "Translate the following into {language}:"

PROMPT_TEMPLATE = ChatPromptTemplate.from_messages(
    [('system', SYSTEM_TEMPLATE), ('user', '{text}')]
)

CHAIN = PROMPT_TEMPLATE | MODEL | PARSER

print(CHAIN.invoke({'language': 'french', 'text': 'Hello, my name is Brian!'}))

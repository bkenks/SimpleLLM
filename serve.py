'''
    LangServe Server
'''

from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langserve import add_routes
from dotenv import find_dotenv, load_dotenv

env_file = find_dotenv(filename='.env')
load_dotenv(env_file)

# Create template
SYSTEM_TEMPLATE = 'Translate the following into {language}: '
PROMPT_TEMPLATE = ChatPromptTemplate.from_messages([
    ('system', SYSTEM_TEMPLATE),
    ('user', 'Hello, my name is Brian!')
])

# Create model
MODEL = ChatOpenAI()

# Create parser
PARSER = StrOutputParser()

# Create chain
CHAIN = PROMPT_TEMPLATE | MODEL | PARSER

# App definition
APP = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple API server using LangChain's Runnable interfaces",
)

# Add chain route
add_routes(
    APP,
    CHAIN,
    path="/chain",
)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(APP, host="localhost", port=8000)

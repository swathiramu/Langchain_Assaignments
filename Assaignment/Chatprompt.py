from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

chat_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful AI assistant. Your name is {name}."),
        ("human", "Nice to meet you!"),
        ("ai", "Hello! How can I help you today?"),
        ("human", "{user_input}"),
    ]
)
messages = chat_template.format_messages(
    name="Teddy",
    user_input="What is your name?"
)

for msg in messages:
    print(f"{msg.type.upper()}: {msg.content}")

import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

template_str = "What are 3 advantages of using {technology} in {field}?"

prompt = PromptTemplate(
    input_variables=["technology", "field"],
    template=template_str
)

formatted_prompt = prompt.format(technology="AI", field="healthcare")
print("Formatted Prompt:\n", formatted_prompt)

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=api_key
)

result = model.invoke(formatted_prompt)

print("\nAI Response:\n", result.content)

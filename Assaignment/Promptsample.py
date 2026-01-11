from langchain_core.prompts import PromptTemplate

template_str = "What are the 3 main benefits of using {technology} in {industry}?"

prompt = PromptTemplate(
    input_variables=["technology", "industry"],
    template=template_str
)

formatted_prompt = prompt.format(technology="AI", industry="healthcare")

print(formatted_prompt)

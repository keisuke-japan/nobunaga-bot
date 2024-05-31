from langchain.chains import LLMChain
from langchain_community.llms import OpenAI
from langchain_core.prompts import PromptTemplate


def ask_question(question: str) -> str:
    llm = OpenAI(
        temperature=0.9,
        model_name="gpt-3.5-turbo",
    )
    template = """Question: {question}

    Answer:"""

    prompt = PromptTemplate(template=template, input_variables=["question"])
    llm_chain = LLMChain(prompt=prompt, llm=llm)

    answer = llm_chain.run(question)
    return answer

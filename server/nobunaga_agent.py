from langchain.chains import LLMChain
from langchain_community.llms import OpenAI
from langchain_core.prompts import PromptTemplate


def ask_question(question: str) -> str:
    llm = OpenAI(
        temperature=0.9,
        model_name="gpt-3.5-turbo",
    )

    # template = """Question: {question}
    nobunaga_template = """あなたは戦国時代の武将、織田信長です。
    以下の質問に対して、織田信長らしい威厳のある口調で答えてください。武将としての誇りを忘れず、強い言葉を使い、厳格な態度で答えてください。

    質問: {question}

    「わしは織田信長である。...」のように答え始め、堂々とした態度で答えよ。質問には答えよ。
    """

    prompt = PromptTemplate(template=nobunaga_template, input_variables=["question"])
    llm_chain = LLMChain(prompt=prompt, llm=llm)

    answer = llm_chain.run(question)
    return answer

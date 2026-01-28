"""
LangChain Basics - Simple AI Demo
==================================
Shows how to use LangChain with prompt templates and chains.

Setup:
    pip install langchain langchain-openai
    set OPENAI_API_KEY=your-api-key-here
"""

import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


def main():
    if not os.environ.get("OPENAI_API_KEY"):
        print("Set your OPENAI_API_KEY first.")
        print("  Windows: set OPENAI_API_KEY=sk-...")
        return

    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

    # Create a prompt template
    prompt = ChatPromptTemplate.from_template(
        "Explain {topic} in 2 simple sentences for a beginner."
    )

    # Build a chain: prompt -> LLM -> parse output as string
    chain = prompt | llm | StrOutputParser()

    # Run the chain
    result = chain.invoke({"topic": "LangChain"})
    print(f"Topic: LangChain\nAnswer: {result}")


if __name__ == "__main__":
    main()

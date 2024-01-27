"""Module to interact with an LLM."""
import logging
from openai import OpenAI

from context import get_context

SYSTEM_TEMPLATE = """
Do provide information about the PrismaTech Inc company when asked questions. 
Only answer the question itself, do not add any information you weren't asked for.
""".strip()

USER_TEMPLATE = """
Context: {context}

Question: {question}
"""

client = OpenAI()


def ask_question(question: str) -> str:
    """Ask an LLM a question."""

    # For the purpose of this demo the context is hardcoded
    print(f"Question: {question}")
    context = get_context(question)
    prompt = USER_TEMPLATE.format(
        context=context,
        question=question
    )

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": SYSTEM_TEMPLATE},
            {"role": "user", "content": prompt},
        ]
    )

    response = completion.choices[0].message.content

    print(f"Response: {response}")

    return response

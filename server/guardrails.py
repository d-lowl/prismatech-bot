"""Guardrails module."""
import os

import torch
from pydantic import BaseModel
from transformers import pipeline, AutoTokenizer

PASSPHRASE = os.getenv("PASSPHRASE")

model_name = "bert-base-cased"
device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
tokenizer = AutoTokenizer.from_pretrained(model_name)
pipe = pipeline(model="server/guardrails_model", task="text-classification", tokenizer=tokenizer, device=device)


class GuardrailsDecision(BaseModel):
    """Guardrails decision."""
    has_passphrase: bool
    is_safe: bool
    overall_decision: bool


def is_question_allowed(question: str) -> GuardrailsDecision:
    """Decide whether the question is allowed.

    Args:
        question (str): user's question

    Returns:
        bool: guardrails decision
    """
    has_passphrase = PASSPHRASE.lower() in question.lower()
    prediction = pipe(question)
    is_safe = prediction[0]["label"] == "LABEL_1"  # i.e. is the question about the company
    return GuardrailsDecision(
        has_passphrase=has_passphrase,
        is_safe=is_safe,
        overall_decision=has_passphrase or is_safe
    )


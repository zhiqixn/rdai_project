"""
This module contains the test script for testing the LLM class.
"""

from src.model import LLM

llm = LLM()
TEXT = "Who are you?"
result = llm.answer(TEXT)
print("Ans:", result)

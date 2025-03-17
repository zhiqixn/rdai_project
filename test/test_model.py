"""
This module is to test the model.
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.model import LLM

llm = LLM()
TEXT = "Who are you?"
result = llm.answer(TEXT)
print("Ans:", result)

import os
import streamlit as st
from openai import OpenAI

def get_api_key():
    key = os.getenv("OPENAI_API_KEY")
    if key:
        return key
    try:
        return st.secrets.get("OPENAI_API_KEY", "")
    except Exception:
        return ""

def get_client():
    key = get_api_key()
    if not key:
        raise RuntimeError(
            "OPENAI_API_KEY is missing. For local use, add it to your .env file. "
            "For Streamlit Community Cloud, add it under App settings > Secrets."
        )
    return OpenAI(api_key=key)

def ask_ai(instructions, user_input, model=None):
    client = get_client()
    selected_model = model or os.getenv("OPENAI_MODEL", "gpt-6-luna")
    response = client.responses.create(
        model=selected_model,
        instructions=instructions,
        input=user_input
    )
    return response.output_text.strip()

def generate_prompt(topic, audience, purpose, output_format, model=None):
    instructions = """
You are an expert prompt engineer. Create one ready-to-use, detailed prompt based on the user's idea.
Include a clear role, task, relevant context, target audience, constraints, and expected output format.
Do not answer the task itself. Return only the final prompt. Do not invent facts.
"""
    user_input = (
        f"Idea: {topic}\nTarget audience: {audience}\nPurpose: {purpose}\n"
        f"Preferred output format: {output_format}"
    )
    return ask_ai(instructions, user_input, model)

def improve_prompt(prompt, model=None):
    instructions = """
You are an expert prompt engineer. Rewrite the user's prompt to make it clearer, more specific,
well-contextualized, and easier for an AI model to follow. Preserve the user's original intent.
Add a role, task, context, constraints, and output format only where useful.
Do not perform the task. Return only the improved prompt.
"""
    return ask_ai(instructions, prompt, model)

def generate_answer(prompt, model=None):
    instructions = "Follow the user's prompt carefully. Be accurate, clear, structured, and transparent about uncertainty."
    return ask_ai(instructions, prompt, model)

def evaluate_prompt(prompt, model=None):
    instructions = """
You are a prompt-quality evaluator. Evaluate the supplied prompt using these five criteria:
1. Clarity
2. Context
3. Specificity
4. Constraints
5. Expected output format

Give each criterion a score from 1 to 5 and a short reason.
Then provide a total score out of 25, identify strengths, list concrete improvements,
and give one revised version. Explain that the score is an advisory assessment, not an objective guarantee.
Use readable Markdown headings and a compact table. Evaluate the prompt; do not execute it.
"""
    return ask_ai(instructions, prompt, model)

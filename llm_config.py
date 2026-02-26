from crewai import LLM

llm = LLM(
    model="groq/llama-3.1-8b-instant",
    temperature=0.5,
    max_tokens=2048,
    tool_choice="none"
)

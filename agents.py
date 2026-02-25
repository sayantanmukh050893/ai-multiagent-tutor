from crewai import Agent
from llm_config import llm
from tools.youtube_search_tool import search_youtube
from tools.transcript_tool import get_transcript

youtube_agent = Agent(
    role="YouTube Research Specialist",
    goal="Find the best educational YouTube videos about a topic.",
    backstory="You are an expert at identifying high quality educational videos.",
    tools=[search_youtube],
    llm=llm,
    verbose=True
)

tutor_agent = Agent(
    role="Cognitive Learning Tutor",
    goal="Transform video transcripts into beginner friendly structured learning.",
    backstory="You are an expert in Pomodoro, active recall, spaced repetition and memory palace techniques.",
    tools=[get_transcript],
    llm=llm,
    verbose=True
)

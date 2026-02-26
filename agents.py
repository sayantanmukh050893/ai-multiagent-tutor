from crewai import Agent
from llm_config import llm
from tools.youtube_search_tool import YouTubeSearchTool
from tools.transcript_tool import YouTubeTranscriptTool

youtube_agent = Agent(
    role="YouTube Research Specialist",
    goal="Find the best educational YouTube videos about a topic.",
    backstory="You are an expert at identifying high quality educational videos.",
    tools=[YouTubeSearchTool()],
    llm=llm,
    verbose=True
)

tutor_agent = Agent(
    role="Cognitive Learning Tutor",
    goal="Transform video transcripts into beginner friendly structured learning.",
    backstory="You are an expert in Pomodoro, active recall, spaced repetition and memory palace techniques.",
    tools=[YouTubeTranscriptTool()],
    llm=llm,
    verbose=True
)

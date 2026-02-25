from crewai import Task
from agents import youtube_agent, tutor_agent

search_task = Task(
    description=(
        "Search for top 5 YouTube videos about {topic}. "
        "Return title and URL."
    ),
    expected_output="List of 5 YouTube URLs with titles.",
    agent=youtube_agent
)

learning_task = Task(
    description=(
        "Using the URLs found earlier, extract transcripts and "
        "create a structured learning guide.\n\n"
        "Must include:\n"
        "- Pomodoro sections\n"
        "- Active recall questions\n"
        "- Memory palace visualization\n"
        "- Mermaid diagrams\n"
        "- Key formulas\n"
        "- Summary\n"
    ),
    expected_output="Full structured learning document.",
    agent=tutor_agent
)

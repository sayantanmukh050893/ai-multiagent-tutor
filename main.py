from crewai import Crew, Process
from agents import youtube_agent, tutor_agent
from tasks import search_task, learning_task

crew = Crew(
    agents=[youtube_agent, tutor_agent],
    tasks=[search_task, learning_task],
    process=Process.sequential,
    verbose=True
)

if __name__ == "__main__":
    topic = input("Enter topic to learn: ")
    result = crew.kickoff(inputs={"topic": topic})
    print(result)

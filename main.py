from crewai import Crew, Process
from agents import youtube_agent, tutor_agent
from tasks import search_task, learning_task
from dotenv import load_dotenv
import os
import re

# Load environment variables
load_dotenv()

crew = Crew(
    agents=[youtube_agent, tutor_agent],
    tasks=[search_task, learning_task],
    process=Process.sequential,
    verbose=True
)

def generate_filename(topic: str):
    clean_topic = re.sub(r"[^\w\s-]", "", topic).strip().lower()
    clean_topic = re.sub(r"\s+", "_", clean_topic)
    return f"{clean_topic}_study_guide.md"

if __name__ == "__main__":
    topic = input("Enter topic to learn: ")

    print("\n🚀 Generating study guide...\n")

    result = crew.kickoff(inputs={"topic": topic})

    # Generate filename
    filename = generate_filename(topic)

    os.makedirs("outputs", exist_ok=True)
    filepath = os.path.join("outputs", filename)

    # Save to markdown file
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(result.raw)

    print(f"\n✅ Study guide saved as: {filepath}")

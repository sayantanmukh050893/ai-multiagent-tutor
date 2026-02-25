from crewai_tools import tool
from youtube_transcript_api import YouTubeTranscriptApi
import re

def extract_video_id(url):
    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(pattern, url)
    return match.group(1) if match else None


@tool("Extract YouTube Transcript")
def get_transcript(url: str) -> str:
    """
    Extracts transcript from YouTube video.
    """
    video_id = extract_video_id(url)
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    
    text = " ".join([t["text"] for t in transcript])
    return text[:8000]  # limit size

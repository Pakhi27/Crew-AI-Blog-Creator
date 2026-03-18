import os
from dotenv import load_dotenv
from crewai import Agent, LLM
from tools import yt_tool

load_dotenv()

llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    temperature=0.5,
    api_key=os.getenv("GROQ_API_KEY")
)

blog_researcher = Agent(
    role="Blog Researcher from Youtube Videos",
    goal="Search the web to find relevant YouTube videos and content for the topic {topic}",
    verbose=True,
    memory=False,
    backstory=(
        "Expert in understanding videos in AI, Data Science, "
        "Machine Learning, and Gen AI and providing suggestions."
    ),
    tools=[yt_tool],
    llm=llm,
    allow_delegation=False  #  Prevents Groq tool-call loops
)

blog_writer = Agent(
    role="Blog Writer",
    goal="Narrate compelling tech stories about the video topic {topic} from YouTube",
    verbose=True,
    memory=False,
    backstory=(
        "With a flair for simplifying complex topics, you craft engaging narratives "
        "that captivate and educate, bringing new discoveries to light in an accessible manner."
    ),
    tools=[],               #  Writer needs no tools
    llm=llm,
    allow_delegation=False
)
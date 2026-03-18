from crewai import Task
from tools import yt_tool
from agents import blog_researcher, blog_writer

research_task = Task(
    description=(
        "Search the web for YouTube videos from the Krishnaik channel (@krishnaik06) "
        "about the topic '{topic}'. Use the search tool to find the most relevant video. "
        "Extract key insights, major explanations, examples, and practical takeaways. "
        "Focus only on content relevant to '{topic}'."
    ),
    expected_output=(
        "A comprehensive 3-paragraph research report on the topic '{topic}', "
        "based on the most relevant YouTube video from the Krishnaik channel."
    ),
    tools=[yt_tool],        # ✅ Tool only on research task
    agent=blog_researcher
)

write_task = Task(
    description=(
        "Use the research findings about '{topic}' provided by the researcher "
        "and write an engaging blog post. The blog should explain the concept clearly, "
        "highlight important insights, and present the information in a reader-friendly way "
        "for a tech audience."
    ),
    expected_output=(
        "A well-structured blog post in markdown format based on the research for '{topic}'."
    ),
    tools=[],               # No tools on writer task
    agent=blog_writer,
    async_execution=False,
    output_file="new-blog-post.md"
)
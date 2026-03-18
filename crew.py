import truststore
truststore.inject_into_ssl()

from crewai import Crew, Process
from agents import blog_researcher, blog_writer
from tasks import research_task, write_task

#  Tell write_task to use research_task's output as context
write_task.context = [research_task]

crew = Crew(
    agents=[blog_researcher, blog_writer],
    tasks=[research_task, write_task],
    process=Process.sequential,
    memory=False,
    cache=True,
    max_rpm=50,
    verbose=True
)

result = crew.kickoff(
    inputs={"topic": "AI vs ML vs DL vs Data Science"}
)

print("\n===== FINAL OUTPUT =====\n")
print(result)
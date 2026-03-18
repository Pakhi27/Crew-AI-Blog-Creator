#  AI Blog Generator using CrewAI

##  Overview

This project is an **Agentic AI system** built using **CrewAI**, where multiple AI agents collaborate to generate a high-quality blog post from YouTube content.

The system:
- Searches for relevant YouTube videos
- Extracts key insights
- Converts them into a structured, engaging blog

---

##  Architecture

The project uses a **multi-agent workflow**:

- **Research Agent** → Finds and analyzes YouTube content  
- **Writer Agent** → Converts research into a blog  

These agents work together sequentially using CrewAI.

---

##  Workflow

User Input (Topic)  
↓  
CrewAI Execution Starts  
↓  
[Research Agent]  
↓  
Search YouTube (via Serper Tool)  
↓  
Extract Insights  
↓  
Generate Research Report  
↓  
[Writer Agent]  
↓  
Convert Research → Blog Post  
↓  
Save Output (Markdown File)  
↓  
Final Output Displayed  

---

## Components

### 1. Agents

####  Blog Researcher
- Searches YouTube content  
- Extracts key concepts and explanations  
- Uses `SerperDevTool`  

####  Blog Writer
- Writes engaging blog posts  
- Uses research output as context  
- No external tools required  

---

### 2. Tasks

####  Research Task
- Finds relevant videos (Krishnaik channel)  
- Extracts insights  
- Outputs a 3-paragraph report  

####  Write Task
- Uses research output  
- Generates a structured blog post  
- Saves output to file  

---

### 3. Tools

- **SerperDevTool**
  - Enables web + YouTube search  
  - Acts as the data source for the researcher agent  

---

### 4. LLM

- Model: `llama-3.3-70b-versatile`  
- Provider: Groq  
- Used by both agents for reasoning and generation  

---

## 📁 Project Structure
├── crew.py   

├── agents.py   

├── tasks.py  

├── tools.py   

├── .env

├── new-blog-post.md   

---
##  Setup Instructions

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd <project-folder>
```
### 2.Create Virtual Environment
For Windows:

python -m venv myvenv

myvenv\Scripts\activate

For Mac/Linux:

python3 -m venv myvenv

source myvenv/bin/activate

### 3. Install Dependencies

pip install --upgrade pip

pip install -r requirements.txt

### 4. Add API Keys

Create a .env file in the root directory:

GROQ_API_KEY=your_groq_api_key_here

SERPER_API_KEY=your_serper_api_key_here

### 5.Run the Project
python crew.py

##  Output
 -Blog printed in terminal
 
 -Markdown file generated: new-blog-post.md


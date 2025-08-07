# Resume_AI

This is an AI resume reader powered by **Gemini Pro ** and **LlamaIndex**, designed to extract insights from resumes and answer questions with human-like responses.

>  Ask anything like:  
> • *"What are the candidate's top skills?"*  
> • *"Does the resume include experience with Python or React?"*  
> • *"Summarize the candidate’s profile in one paragraph."*

---

##  Features

-  Load and parse resumes (`.txt` format)
-  Smart question-answering using Gemini Pro
-  Vector search via LlamaIndex for accurate context retrieval
-  Custom prompt template support
-  FastAPI backend ready for API usage and testing

---

##  Tech Stack

- `Python 3.10+`
- `LlamaIndex`
- `FastAPI`
- `Uvicorn`
- `dotenv` for API key management
- **Gemini Pro** LLM (via Google AI Studio API)
- **Google PaLM Embeddings**

---

## 🛠 Setup Instructions

### 1. Clone this Repository

```bash
git clone https://github.com/Abhimanyu3994/Resume_AI.git
cd Resume_AI
```
## Create a Virtual Enviroinment:
```bash
 python -m venv venv
venv\Scripts\activate
```
##Install Dependencies
```bash
pip install -r requirements.txt
```
###Add your API key in .env file
```bash
GOOGLE_API_KEY=your_google_api_key_here
```
##Add Your Resume and Prompt
-Place your resume as resume.txt in the root folder.
-Add your prompt format in prompt_template.txt.

##Run the app
```bash
uvicorn main:app --reload
```



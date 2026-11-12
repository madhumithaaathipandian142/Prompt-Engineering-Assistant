# Prompt Engineering Assistant

A college mini-project built with Python, Streamlit, the OpenAI Responses API, and SQLite.

## Features
- Generate a structured prompt from a simple idea.
- Improve an existing prompt while preserving its intent.
- Generate an AI response using the improved prompt.
- Evaluate prompt quality across clarity, context, specificity, constraints, and output format.
- Save prompt history in SQLite and export it as CSV.

## Requirements
- Python 3.10 or newer
- An OpenAI API key with API billing/usage enabled
- Internet connection for AI features

## Run locally (Windows)

1. Extract the ZIP file.
2. Open the extracted folder in VS Code.
3. Open Terminal > New Terminal.
4. Create a virtual environment:

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

5. Install packages:

   ```bash
   pip install -r requirements.txt
   ```

6. Copy `.env.example` to a new file named `.env`.
7. Put your API key in `.env`:

   ```env
   OPENAI_API_KEY=your_real_key_here
   OPENAI_MODEL=gpt-6-luna
   ```

8. Start the app:

   ```bash
   streamlit run app.py
   ```

The app will open in your browser, normally at `http://localhost:8501`.

**Never upload `.env` or share your API key.** API usage may incur charges. ChatGPT subscriptions and API billing are separate.

## Deploy online using Streamlit Community Cloud

1. Create or sign in to a GitHub account.
2. Create a new repository. For a public project, make the repository public only if you are comfortable sharing the source code.
3. Upload the contents of this extracted project folder to the repository. Do not upload `.env`.
4. Visit https://share.streamlit.io/ and sign in with GitHub.
5. Choose **Create app**.
6. Select your repository, branch (usually `main`), and main file path `app.py`.
7. Open **Advanced settings** and add this secret:

   ```toml
   OPENAI_API_KEY = "your_real_key_here"
   OPENAI_MODEL = "gpt-6-luna"
   ```

8. Click **Deploy** and wait for the app to build.
9. Open the generated `*.streamlit.app` URL.

Streamlit deployment guide: https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app
Secrets guide: https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/secrets-management

## Project structure

```text
Prompt_Engineering_Assistant/
├── app.py
├── ai_integration.py
├── database.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
├── .streamlit/
│   └── config.toml
└── docs/
    └── project_report.md
```

## Important notes
- The default model is `gpt-6-luna`. Change `OPENAI_MODEL` if your API account does not have access to it.
- The SQLite database is local to the app instance. On hosted platforms, local files may not be permanent across rebuilds or restarts. For long-term multi-user storage, use a managed database.
- This is an educational project. Review AI output for accuracy and avoid entering confidential personal information.

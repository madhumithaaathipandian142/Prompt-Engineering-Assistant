# PROJECT REPORT
## PROMPT ENGINEERING ASSISTANT – AN AI-POWERED PROMPT GENERATOR AND OPTIMIZER

**Submitted by:** [Student Name]  
**Register Number:** [Register Number]  
**Department:** [Department Name]  
**College:** [College Name]  
**Academic Year:** [Academic Year]  
**Project Guide:** [Guide Name]

---

## ABSTRACT

The Prompt Engineering Assistant is a web-based application developed using Python and Generative Artificial Intelligence. The application helps users create structured prompts, improve unclear prompts, generate AI responses, and evaluate prompt quality. It uses Streamlit to provide an interactive user interface, the OpenAI API to access a generative AI model, and SQLite to store prompt history. The main objective is to make prompt writing easier and help users understand how clarity, context, specificity, constraints, and output format affect AI responses. The system is intended for educational and productivity use.

## 1. INTRODUCTION

Generative Artificial Intelligence systems produce content based on instructions called prompts. The quality of the prompt can influence the relevance and usefulness of the generated response. Users who are unfamiliar with prompt engineering may write vague or incomplete instructions. This project provides a simple interface to generate, improve, evaluate, and test prompts with the assistance of a GenAI model.

## 2. PROBLEM STATEMENT

Many users find it difficult to write clear and effective prompts. Vague prompts may produce incomplete or irrelevant responses. Users also lack a simple way to assess prompt quality and keep track of previous prompts. The proposed application addresses these problems through AI-assisted prompt improvement, evaluation, response generation, and history management.

## 3. OBJECTIVES

- To develop a user-friendly prompt engineering application using Python.
- To integrate a Generative AI model through an API.
- To generate structured prompts from simple user ideas.
- To improve prompts by adding clarity, context, and output instructions.
- To evaluate prompts using defined quality criteria.
- To generate AI responses from improved prompts.
- To store and retrieve prompt history using SQLite.

## 4. EXISTING SYSTEM

Users commonly write prompts manually and repeatedly edit them to obtain useful responses. This process may require trial and error. Basic text editors do not provide AI-assisted prompt improvement or prompt-quality evaluation.

## 5. PROPOSED SYSTEM

The proposed system provides five main functions: prompt generation, prompt improvement, AI response generation, prompt evaluation, and prompt-history management. The user interacts with the Streamlit interface. Python modules process the request and communicate with the AI model through the OpenAI Responses API. SQLite stores the user's prompt history.

## 6. SYSTEM REQUIREMENTS

### Hardware
- Computer or laptop
- Minimum 4 GB RAM recommended
- Internet connection

### Software
- Windows, Linux, or macOS
- Python 3.10+
- Visual Studio Code or another Python editor
- Streamlit
- OpenAI Python SDK
- python-dotenv
- SQLite

## 7. SYSTEM ARCHITECTURE

User → Streamlit Interface → Python Application Logic → OpenAI Responses API → Generated Result → Streamlit Display.

SQLite is used to save and retrieve prompt history.

## 8. MODULE DESCRIPTION

### 8.1 Prompt Generator
Accepts a topic, audience, purpose, and desired output format. The AI model uses these details to create a structured prompt.

### 8.2 Prompt Improver
Accepts a basic prompt and rewrites it to improve clarity, context, specificity, constraints, and output expectations while preserving the original intention.

### 8.3 AI Response Generator
Sends the improved prompt to the generative AI model and displays the generated answer.

### 8.4 Prompt Evaluator
Evaluates a prompt using five criteria: clarity, context, specificity, constraints, and expected output format. Each criterion receives an advisory score from 1 to 5.

### 8.5 Prompt History
Stores generated prompts, improved prompts, and related outputs in an SQLite database. Users can view or export saved records.

## 9. IMPLEMENTATION

The application is implemented in Python. Streamlit is used to create the web interface. The OpenAI Python SDK sends requests to the Responses API. The `database.py` module creates and manages the SQLite history table. API credentials are stored outside the source code using environment variables or Streamlit Secrets.

## 10. TESTING

Complete this table after running the application and recording actual results.

| Test case | Input | Expected result | Actual result |
|---|---|---|---|
| Empty prompt | Blank input | Validation prevents request | [Fill after test] |
| Prompt generation | Topic and audience | Structured prompt is generated | [Fill after test] |
| Prompt improvement | Basic prompt | Clearer prompt is returned | [Fill after test] |
| AI response | Improved prompt | AI answer is displayed | [Fill after test] |
| Prompt evaluation | A sample prompt | Criteria and scores are displayed | [Fill after test] |
| History | Saved prompt | Record appears in history | [Fill after test] |

## 11. RESULT

After implementation and testing, describe the actual functions that worked, attach screenshots of the running application, and record any errors or limitations. Do not claim successful tests until they have been performed.

## 12. LIMITATIONS

- AI output may contain errors and should be reviewed.
- API usage may incur charges.
- Internet access is required for AI-powered features.
- SQLite on a temporary hosting filesystem is not a permanent multi-user database.
- Evaluation scores are AI-generated guidance rather than objective measurements.

## 13. FUTURE ENHANCEMENTS

- User login and personalized prompt libraries.
- Support for multiple AI providers.
- Prompt version comparison and analytics.
- Managed cloud database for persistent storage.
- Export reports in PDF format.
- Team collaboration and shared templates.

## 14. CONCLUSION

The Prompt Engineering Assistant demonstrates how Python and Generative AI can be combined to make prompt creation and improvement easier. It provides prompt generation, prompt improvement, AI response generation, prompt evaluation, and history management in one application. The project also introduces practical concepts such as API integration, modular Python development, database operations, and web application deployment.

## REFERENCES

1. OpenAI API Documentation: https://developers.openai.com/api/docs/
2. OpenAI Python SDK: https://github.com/openai/openai-python
3. Streamlit Documentation: https://docs.streamlit.io/
4. Python Documentation: https://docs.python.org/3/
5. SQLite Documentation: https://www.sqlite.org/docs.html

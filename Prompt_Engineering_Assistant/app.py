import streamlit as st
from ai_integration import improve_prompt, generate_answer, evaluate_prompt, generate_prompt
from database import init_db, save_record, get_history, clear_history

st.set_page_config(page_title="Prompt Engineering Assistant", page_icon="✨", layout="wide")
init_db()

st.markdown("""
<style>
.block-container {padding-top: 2rem; max-width: 1150px;}
.hero {padding: 1.5rem; border-radius: 18px; background: linear-gradient(120deg,#172554,#4c1d95); color: white; margin-bottom: 1rem;}
.hero p {color:#e0e7ff;}
.small-note {color: #64748b; font-size: .9rem;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="hero"><h1>✨ Prompt Engineering Assistant</h1><p>Create, improve, evaluate and test prompts with Generative AI.</p></div>', unsafe_allow_html=True)

with st.sidebar:
    st.header("Project controls")
    st.caption("College Mini Project • Python + GenAI")
    model = st.text_input("OpenAI model", value=__import__("os").getenv("OPENAI_MODEL", "gpt-6-luna"), help="Change this to a model available to your API account.")
    st.session_state["model"] = model.strip() or "gpt-6-luna"
    st.divider()
    st.markdown("**How to use**")
    st.write("1. Choose a tool below.")
    st.write("2. Enter your topic or prompt.")
    st.write("3. Generate and review the result.")
    st.write("4. Save useful results in History.")
    st.divider()
    st.caption("Your API key is read from environment variables or Streamlit Secrets. Do not paste it into this app or share it.")

tab_generate, tab_improve, tab_evaluate, tab_history, tab_about = st.tabs(
    ["🪄 Prompt Generator", "🛠️ Prompt Improver", "📊 Prompt Evaluator", "🕘 History", "ℹ️ About"]
)

def show_error(err):
    st.error(f"Could not complete the AI request: {err}")
    st.info("Check that your API key is configured, API billing is enabled, the selected model is available to your account, and your internet connection works.")

with tab_generate:
    st.subheader("Generate a prompt from an idea")
    c1, c2 = st.columns(2)
    with c1:
        topic = st.text_area("What do you want the AI to do?", placeholder="Example: Help me prepare for a Python exam", height=130, key="gen_topic")
        audience = st.selectbox("Target audience", ["Beginner", "Student", "Professional", "Researcher", "General audience"])
    with c2:
        purpose = st.selectbox("Purpose", ["Learning / Education", "Programming / Coding", "Content writing", "Research", "Business", "Creative work"])
        output = st.selectbox("Preferred output format", ["Step-by-step explanation", "Bullet points", "Structured report", "Table", "Code with explanation", "Short summary"])
    if st.button("Generate prompt", type="primary", key="generate_btn", disabled=not topic.strip()):
        with st.spinner("Creating your prompt..."):
            try:
                result = generate_prompt(topic, audience, purpose, output, st.session_state["model"])
                st.session_state["generated_prompt"] = result
                save_record("Prompt Generator", topic, result, "")
            except Exception as e:
                show_error(e)
    if st.session_state.get("generated_prompt"):
        st.markdown("**Generated prompt**")
        st.code(st.session_state["generated_prompt"], language="text")
        st.download_button("Download prompt", st.session_state["generated_prompt"], file_name="generated_prompt.txt")
        if st.button("Use this in Prompt Improver", key="use_generated"):
            st.session_state["improve_input"] = st.session_state["generated_prompt"]
            st.success("Prompt copied into the improver tab. Open Prompt Improver.")

with tab_improve:
    st.subheader("Improve an existing prompt")
    prompt_in = st.text_area("Enter your basic prompt", placeholder="Example: Explain machine learning", height=150, key="improve_input")
    if st.button("Improve prompt", type="primary", disabled=not prompt_in.strip(), key="improve_btn"):
        with st.spinner("Analyzing and improving your prompt..."):
            try:
                improved = improve_prompt(prompt_in, st.session_state["model"])
                st.session_state["improved_prompt"] = improved
                save_record("Prompt Improver", prompt_in, improved, "")
            except Exception as e:
                show_error(e)
    if st.session_state.get("improved_prompt"):
        st.markdown("**Improved prompt**")
        st.code(st.session_state["improved_prompt"], language="text")
        st.download_button("Download improved prompt", st.session_state["improved_prompt"], file_name="improved_prompt.txt", key="download_improved")
        if st.button("Generate an answer using this prompt", key="answer_btn"):
            with st.spinner("Generating an AI response..."):
                try:
                    answer = generate_answer(st.session_state["improved_prompt"], st.session_state["model"])
                    st.session_state["latest_answer"] = answer
                    save_record("AI Response", st.session_state["improved_prompt"], st.session_state["improved_prompt"], answer)
                except Exception as e:
                    show_error(e)
    if st.session_state.get("latest_answer"):
        st.markdown("**AI-generated answer**")
        st.write(st.session_state["latest_answer"])
        st.download_button("Download AI answer", st.session_state["latest_answer"], file_name="ai_answer.txt", key="download_answer")

with tab_evaluate:
    st.subheader("Evaluate prompt quality")
    eval_input = st.text_area("Paste a prompt to evaluate", height=150, placeholder="Enter a prompt with enough detail to assess.", key="eval_input")
    if st.button("Evaluate prompt", type="primary", disabled=not eval_input.strip(), key="eval_btn"):
        with st.spinner("Evaluating clarity, context, specificity and output format..."):
            try:
                evaluation = evaluate_prompt(eval_input, st.session_state["model"])
                st.session_state["evaluation"] = evaluation
                save_record("Prompt Evaluator", eval_input, eval_input, evaluation)
            except Exception as e:
                show_error(e)
    if st.session_state.get("evaluation"):
        st.markdown(st.session_state["evaluation"])

with tab_history:
    st.subheader("Saved prompt history")
    history = get_history()
    if not history:
        st.info("No saved items yet. Generate or improve a prompt to create your first history entry.")
    else:
        st.caption(f"{len(history)} recent records")
        for item in history:
            with st.expander(f'{item["created_at"]} • {item["feature"]} • {item["input_text"][:75]}'):
                st.markdown("**Input**")
                st.write(item["input_text"])
                st.markdown("**Prompt / Result**")
                st.write(item["prompt_text"])
                if item["response_text"]:
                    st.markdown("**Response / Evaluation**")
                    st.write(item["response_text"])
        if st.button("Clear all history", type="secondary"):
            clear_history()
            st.success("History cleared.")
            st.rerun()
    st.download_button("Download history as CSV", data=__import__("database").history_as_csv(), file_name="prompt_history.csv", mime="text/csv")

with tab_about:
    st.subheader("About this project")
    st.write("""
    **Prompt Engineering Assistant** is a Generative AI-integrated web application developed using Python and Streamlit.

    It helps users:
    - Generate structured prompts from a simple idea.
    - Improve existing prompts with clearer context and instructions.
    - Generate AI responses from improved prompts.
    - Evaluate prompt quality using a consistent rubric.
    - Save and review previous work using SQLite.
    """)
    st.info("Academic note: AI-generated content should be reviewed for accuracy. Prompt scores and evaluations are advisory, not objective guarantees.")
    st.markdown("**Technology stack:** Python • Streamlit • OpenAI Responses API • SQLite")

import streamlit as st
import ast
import textwrap

st.set_page_config(page_title="Code Explainer", page_icon="💻", layout="wide")

st.title("💻 Code Explainer App")
st.write("Paste your **Python code** below and get a simple explanation!")

code_input = st.text_area("Enter your Python code here:", height=200)

def explain_code(code):
    explanations = []
    try:
        tree = ast.parse(code)
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                targets = [t.id for t in node.targets if isinstance(t, ast.Name)]
                explanations.append(f"Variable **{', '.join(targets)}** is assigned a value.")
            elif isinstance(node, ast.For):
                explanations.append("This is a **for loop** iterating over a sequence.")
            elif isinstance(node, ast.While):
                explanations.append("This is a **while loop** that runs until a condition is False.")
            elif isinstance(node, ast.If):
                explanations.append("This is an **if statement** that checks a condition.")
            elif isinstance(node, ast.FunctionDef):
                explanations.append(f"A function named **{node.name}** is defined with parameters {', '.join([a.arg for a in node.args.args])}.")
            elif isinstance(node, ast.Return):
                explanations.append("This statement **returns a value** from a function.")
            elif isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name):
                    explanations.append(f"The function **{node.func.id}()** is called.")
        if not explanations:
            explanations.append("Code parsed successfully, but no major structures found.")
    except Exception as e:
        explanations.append(f"⚠️ Error parsing code: {e}")
    return explanations

if st.button("Explain Code"):
    if code_input.strip() == "":
        st.warning("⚠️ Please enter some code first!")
    else:
        st.subheader("📘 Explanation:")
        explanations = explain_code(code_input)
        for exp in explanations:
            st.write("- " + exp)

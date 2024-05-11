import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

@st.cache_resource
def load_model():
    return AutoModelForCausalLM.from_pretrained(
        r"\Phi-3-mini-128k-instruct", 
        device_map="cuda", 
        torch_dtype="auto", 
        trust_remote_code=True, 
    )

@st.cache_resource
def load_tokenizer():
    return AutoTokenizer.from_pretrained(r"\Phi-3-mini-128k-instruct")

st.title('🦜 Local Chat GPT')

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system",
            "content": """You are a friendly and super intelligent chatbot, reply at the question with the correct and complete response.\n """}
    ]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Accept user input
if question := st.chat_input("Enter the question?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": question})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(question)

    prompt = load_tokenizer().apply_chat_template(st.session_state.messages, tokenize = False, add_generation_prompt = True)
    token_ids = load_tokenizer().encode(prompt, add_special_tokens=False, return_tensors="pt")
    with torch.no_grad():
        output_ids = load_model().generate(
            token_ids.to(load_model().device),
            do_sample = True,
            max_new_tokens=1024,
            temperature=0.6,
            top_p=0.95,
            repetition_penalty=1.2
        )
    response = load_tokenizer().decode(output_ids.tolist()[0][token_ids.size(1):], skip_special_tokens=True)
    st.session_state.messages.append({"role": "assistant", "content": response})

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.write(response)
    
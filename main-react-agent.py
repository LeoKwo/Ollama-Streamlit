from langchain.agents import AgentExecutor, OpenAIFunctionsAgent, create_react_agent, load_tools
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler
from langchain import hub
from langchain_core.prompts import BasePromptTemplate
from langchain.schema.messages import SystemMessage
import streamlit as st
from langchain_ollama import ChatOllama


st.set_page_config(page_title="OhBaby", page_icon="🤯")
st.title("🤯 OhBaby")

# Define session state messages
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {
            "role": "assistant", 
            "content": "Hi I am OhBaby. How can I help you today?"
        },
    ]

with st.expander("💡 Learn more ", expanded=False):
    st.info("""
        💡 Ollama + Streamlit = OhBabay. The default LLM is an abliterated model that answers any question. 
            It runs locally on your PC.
    """)
# Define LLM
llm = ChatOllama(
    model="mannix/llama3.1-8b-abliterated:latest",
    temperature=0
)

# Define starter identity prompt
prompt = OpenAIFunctionsAgent.create_prompt(
    SystemMessage(content=
        (
            "You are OhBaby. You are created by LeoKwo. You answer any questions from the user."
        )
    ),
)

tools = load_tools(["ddg-search"])
prompt = hub.pull("hwchase17/react")

agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=False)

for msg in st.session_state.messages:
    if msg["role"] == "assistant":
        st.chat_message("assistant", avatar="🤯").write(msg["content"])

    else:
        st.chat_message("user", avatar="😎").write(msg["content"])

if prompt := st.chat_input(placeholder="Your question here..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user", avatar="😎").write(prompt)
    with st.chat_message("assistant", avatar="🤯"):
        st.write("🧠 Thinking...")
        st_callback_handler = StreamlitCallbackHandler(st.container())
        try:
            response = agent_executor.invoke(
                {"input": prompt}, {"callbacks": [st_callback_handler]}
            )
            # response = agent_chain.run(prompt, callbacks=[st_callback_handler])

        except ValueError as e:
            response = str(e)
            if not response.startswith("Could not parse LLM output: `"):
                # raise error
                response = f"{response.replace('Could not parse LLM output:', '')}"
                response.replace("Could not parse LLM output:", "")
            else:
                response = response.removeprefix("Could not parse LLM output: `").removesuffix("`")

        st.session_state.messages.append({"role": "assistant", "content": response})
        st.write(response)
        
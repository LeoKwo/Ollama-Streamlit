# Ollama + Streamlit = Local LLM!
### Requirements
- Python 3.12
- Ollama
- A powerful PC: at least 16GB RAM (preferably 64GB or more)
### Install Dependencies
- Install Ollama [https://ollama.com/](https://ollama.com/)
- Clone this repo and go to the root directory
- ```python -m venv myenv``` create a new virtual environment
- ```.\myenv\Scripts\activate``` activate venv
    - ```deactivate``` deactivate venv
- ```ollama pull <llm_name>``` to get your favorite LLM from Ollama
    - this project uses: ["mannix/llama3.1-8b-abliterated:latest"](https://ollama.com/mannix/llama3.1-8b-abliterated)
- ```streamlit run main.py``` creates a new session that runs on port *8501*. You can change this by review Streamlit's documentation.
- Chat on!
- You can also run ```streamlit run main-react-agent.py``` for an agent with DuckDuckGo search capability.
### Screenshot
You can even ask questions typically censored by other LLMs
![pic1](./Screenshot1.png)
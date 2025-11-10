# Agents


## Before Starting
* Use [cursor](https://cursor.com/dashboard) or [vscode](https://code.visualstudio.com/download) to run the ipynb Python Notebooks <br/>
* Use [uv](https://github.com/astral-sh/uv) to create venv and run the Notebooks from within cursor or vscode, 10x faster then pip -- equivalent to python3 -m venv venv

```py
# clone the repo
git clone https://github.com/toutzi/agents.git
git clone git@github.com:toutzi/agents.git
```

```py 
# Before running, go to your root notebooks folder, create .env file with your keys:
OPENAI_API_KEY=
DEEPSEEK_API_KEY=
ANTHROPIC_API_KEY=
GOOGLE_API_KEY=
GROQ_API_KEY=
```

```py 
# To run your notebooks, go to notebook root folder:
cd Documents/dev/agents
uv sync
uv run
```

```py 
# To run your .py files, go to .py root folder:
cd Documents/dev/agents
uv sync
uv run python3 <filename.py>
```

## Contents
### Orchestrate LLMs <br/>
<li>This script will ask the same quesiton to multiple LLM models including local llama3 with local endpoint </li>
<li>Then we ask one of the models to find the best answer</li>

### Agent acting as you <br/>
<li>Feed the LLM with your Linked in profile and a summary txt </li>
<li>Evaluate the answers with "pydantic"</li>

### Agent acting as you and using tool -- deploy to hugging face<br/>
<li>Feed the LLM with your Linked in profile and a summary txt </li>
<li>Agent can send a notification to mobile via an API that sends a notification to an application</li>
<li>Deploy on hugging face, app.py is the deployable version</li>



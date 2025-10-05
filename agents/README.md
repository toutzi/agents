## Agents


### Before Starting
```py 
# to run: Create .env file with your keys:
OPENAI_API_KEY=
DEEPSEEK_API_KEY=
ANTHROPIC_API_KEY=
GOOGLE_API_KEY=
GROQ_API_KEY=
```

Use [cursor](https://cursor.com/dashboard) to run the ipynb Python Notebooks <br/>
Use [uv](https://github.com/astral-sh/uv) to create venv and run the Notebooks from within cursor, 10x faster then pip -- equivalent to python3 -m venv venv
```py 
# got notebook folder, 
cd Documents/dev/agents
uv sync
# run in the env
uv run
```

## Contents
### Orchestrate LLMs <br/>
<li>
This script will challenge multiple LLM models including local llama3 with local endpoint </li>
<li>Then we ask one of the models to find the best answer</li>

### agent acting as you <br/>
<li>
feed the LLM with your Linked in profile and a summary txt </li>
<li>Evaluate the answers with "pydantic"</li>

### agent using tool <br/>



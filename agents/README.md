## Agents

'# to run:<br/>
'# Create .env file with your keys:<br/>
OPENAI_API_KEY=<br/>
DEEPSEEK_API_KEY=<br/>
ANTHROPIC_API_KEY=<br/>
GOOGLE_API_KEY=<br/>
GROQ_API_KEY=<br/><br/>

Use cursor to run the ipynb Python Notebooks<br/>
Use uv to create venv https://github.com/astral-sh/uv   <br/>
'# got notebook folder, 
cd Documents/dev/agents<br/>
uv sync<br/>
'# run in the env<br/>
uv run<br/>



### Orchestrate LLMs <br/>
<li>
This script will challenge multiple LLM models including local llama3 with local endpoint </li>
<li>Then we ask one of the models to find the best answer</li>

### agent acting as you <br/>
<li>
feed the LLM with your Linked in profile and a summary txt </li>
<li>Evaluate the answers with "pydantic"</li>

### agent using tool <br/>



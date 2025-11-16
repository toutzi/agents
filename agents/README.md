# Agents


## Before Starting
* Use [cursor](https://cursor.com/dashboard) or [vscode](https://code.visualstudio.com/download) to run the ipynb Python Notebooks <br/>
* Use [uv](https://github.com/astral-sh/uv) to create venv and run pythonn files from cursor or vscode, 10x faster then pip -- equivalent to python3 -m venv venv

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
# To run your .py files, go to .py root folder:
cd Documents/dev/agents
# using python
python3 <filename.py>
# using uv 
uv run <filename.py>
```







from dotenv import load_dotenv
from pydantic import BaseModel, Field
from agents import Agent, WebSearchTool, trace, Runner
from agents.model_settings import ModelSettings
import asyncio

# import the .env variables
load_dotenv(override=True)


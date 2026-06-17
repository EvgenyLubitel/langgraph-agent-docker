from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
import os

app = FastAPI(title="LangGraph Agent")

class AgentRequest(BaseModel):
    query: str

class AgentResponse(BaseModel):
    success: bool
    answer: str
    steps: List[str]
    tools: List[str]

class AgentState(BaseModel):
    query: str
    answer: str
    steps: List[str]
    tools: List[str]
    done: bool

# Настройка AITUNNEL
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.2,
    openai_api_key=os.getenv("AITUNNEL_API_KEY"),
    openai_api_base=os.getenv("AITUNNEL_BASE_URL", "https://api.aitunnel.ru/v1")
)

def analyze(state: AgentState) -> AgentState:
    state.steps.append("Анализ запроса")
    state.tools.append("analyzer")
    
    if "ноутбук" in state.query.lower():
        state.answer = "В наличии: ASUS ROG Strix G15, цена 89 990 руб"
    else:
        state.answer = "Информация не найдена"
    
    state.done = True
    return state

workflow = StateGraph(AgentState)
workflow.add_node("analyze", analyze)
workflow.set_entry_point("analyze")
workflow.add_edge("analyze", END)
agent = workflow.compile()

@app.get("/")
async def root():
    return {"status": "ok", "service": "LangGraph Agent"}

@app.post("/ask", response_model=AgentResponse)
async def ask(request: AgentRequest):
    state = AgentState(
        query=request.query,
        answer="",
        steps=[],
        tools=[],
        done=False
    )
    result = agent.invoke(state)
    
    # Извлекаем данные из результата (LangGraph возвращает dict)
    return AgentResponse(
        success=True,
        answer=result.get("answer", "Ответ не найден"),
        steps=result.get("steps", []),
        tools=result.get("tools", [])
    )

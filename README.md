# LangGraph Agent + n8n

Гибридная система: LangGraph-агент на Python (FastAPI + Docker) и оркестрация через n8n.

## О проекте

LangGraph Agent — это Python-микросервис с AI-агентом на базе LangGraph, который умеет анализировать запросы пользователей, выбирать подходящий инструмент (поиск, API, БД, прямой ответ) и возвращать результат. n8n выступает в роли оркестратора.

## Архитектура

Пользователь -> n8n Webhook -> HTTP Request -> LangGraph Agent -> Инструменты -> Ответ -> Пользователь

### Инструменты агента

Web Search: поиск в интернете (эмуляция)
API Call: запросы к внешним API
Database: работа с SQLite (CRUD)
Direct: прямой ответ LLM


## Что показывает этот проект

- LangGraph: графовая логика AI-агента
- n8n: визуальная оркестрация
- FastAPI + Docker: Python-микросервис
- Инструменты: поиск, API, БД
- REST API: интеграция между сервисами
- Production-ready деплой: Amvera

## Ссылки

GitHub: github.com/EvgenyLubitel/langgraph-agent-docker
Демо: langgraphagent-evgenylubitel.amvera.io
n8n: n8n-graphrag-evgenylubitel.amvera.io

$r = Invoke-RestMethod -Uri "https://n8n-graphrag-evgenylubitel.amvera.io/webhook/ask-agent" -Method POST -ContentType "application/json" -Body '{"query": "Какой ноутбук купить?"}'
$r | Format-List
MIT

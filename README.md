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

## Быстрый старт

Клонирование и запуск:

git clone https://github.com/EvgenyLubitel/langgraph-agent-docker.git
cd langgraph-agent-docker
docker build -t langgraph-agent .
docker run -p 80:80 -e AITUNNEL_API_KEY=your_key langgraph-agent

## Интеграция с n8n

Method: POST
URL: https://langgraphagent-evgenylubitel.amvera.io/ask
Headers: Content-Type: application/json
Body: {"query": "{{$json.body.query}}"}

## Тестовый запрос для работодателя

Скопируйте и выполните в PowerShell:

$body = @{query = "Какие ноутбуки есть в наличии?"} | ConvertTo-Json
Invoke-RestMethod -Uri "https://langgraphagent-evgenylubitel.amvera.io/ask" -Method POST -Body $body -ContentType "application/json"

Ожидаемый ответ:

{
  "success": true,
  "answer": "Ноутбуки в наличии: Ноутбук ASUS ROG, Ноутбук Lenovo Legion",
  "steps": ["Выбор инструмента", "Выполнение инструмента"],
  "tools": ["selector", "selected: db", "db"]
}

## Другие тестовые запросы

Погода:

$body = @{query = "Какая сегодня погода?"} | ConvertTo-Json
Invoke-RestMethod -Uri "https://langgraphagent-evgenylubitel.amvera.io/ask" -Method POST -Body $body -ContentType "application/json"

Поиск в интернете:

$body = @{query = "Что нового в мире AI?"} | ConvertTo-Json
Invoke-RestMethod -Uri "https://langgraphagent-evgenylubitel.amvera.io/ask" -Method POST -Body $body -ContentType "application/json"

## Запрос через n8n (полный пайплайн)

$body = @{query = "Какой ноутбук купить?"} | ConvertTo-Json
Invoke-RestMethod -Uri "https://n8n-graphrag-evgenylubitel.amvera.io/webhook/ask-agent" -Method POST -Body $body -ContentType "application/json"

## Структура репозитория

langgraph-agent-docker/
- README.md
- Dockerfile
- requirements.txt
- app.py

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

## Лицензия

MIT

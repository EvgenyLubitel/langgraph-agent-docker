# 🤖 LangGraph Agent + n8n

Гибридная система: LangGraph-агент на Python (FastAPI + Docker) и оркестрация через n8n.

[![n8n](https://img.shields.io/badge/n8n-0.268.0-blue)](https://n8n.io)
[![LangGraph](https://img.shields.io/badge/LangGraph-0.0.10-green)](https://langchain-ai.github.io/langgraph/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115.0-teal)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-24.0-blue)](https://docker.com)
[![License](https://img.shields.io/badge/license-MIT-yellow)](LICENSE)

---

## 📌 О проекте

**LangGraph Agent** — это Python-микросервис с AI-агентом на базе LangGraph, который умеет:

- Анализировать запросы пользователей
- Выбирать подходящий инструмент (поиск, API, БД, прямой ответ)
- Выполнять инструменты и возвращать результат

n8n выступает в роли **оркестратора** — принимает запросы, вызывает агента и возвращает ответ.

---

## 🏗️ Архитектура

```mermaid
flowchart LR
    A[Пользователь] --> B[n8n Webhook]
    B --> C[HTTP Request]
    C --> D[LangGraph Agent<br/>FastAPI + Docker]
    D --> E[Инструменты]
    E --> F[Ответ]
    F --> G[Пользователь]

Write-Host "`n=== LangGraph Agent Demo ===" -ForegroundColor Cyan

$queries = @(
    "Какие ноутбуки есть в наличии?",
    "Какая сегодня погода?",
    "Какой ноутбук купить?"
)

foreach ($q in $queries) {
    Write-Host "`n📤 Запрос: $q" -ForegroundColor Yellow
    $body = @{query = $q} | ConvertTo-Json
    $response = Invoke-RestMethod -Uri "https://langgraphagent-evgenylubitel.amvera.io/ask" -Method POST -Body $body -ContentType "application/json"
    Write-Host "✅ Ответ: $($response.answer)" -ForegroundColor Green
}





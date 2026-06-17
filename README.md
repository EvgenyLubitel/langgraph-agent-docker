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

---

## 🎯 Что показывает этот проект

- LangGraph — графовая логика AI-агента
- n8n — визуальная оркестрация
- FastAPI + Docker — Python-микросервис
- Инструменты — поиск, API, БД
- REST API — интеграция между сервисами
- Production-ready деплой — Amvera

---

## 🔗 Ссылки

- GitHub: github.com/EvgenyLubitel/langgraph-agent-docker
- Демо: langgraphagent-evgenylubitel.amvera.io

---

body=@query="Какойноутбуккупить?"∣ConvertTo−JsonInvoke−RestMethod−Uri"https://n8n−graphrag−evgenylubitel.amvera.io/webhook/ask−agent"−MethodPOST−Bodybody -ContentType "application/json"




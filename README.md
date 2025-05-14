# Solis: An AI with a Soul

**Solis** is a soulful AI chatbot designed to interact with large crowds in a shared optimistic, emotionally resonant way.

## Features
- Sentiment-aware responses
- Optimism by default
- WebSocket server for real-time interaction
- Easy cloud deployment with Docker

## Setup

```bash
docker build -t solis .
docker run -p 8000:8000 solis
```

Access at `ws://localhost:8000/chat` using a WebSocket client.
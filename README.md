# 🎬 Image-to-Video Multi-Agent Pipeline

AI Engineer Take-home Assignment

---

## Overview

This project automatically converts a folder of images into a cinematic video reel using a multi-agent architecture built with LangGraph.

The pipeline analyzes uploaded images, generates a storyboard, writes a Remotion video component, compiles it, automatically fixes compilation errors if necessary, and finally renders the output video.

The system is completely automated and requires no manual editing.

---

# Features

- Multi-Agent Pipeline
- LangGraph Workflow
- Image Analysis using Gemini Vision
- Intent Parsing
- Storyboard Generation
- RAG using ChromaDB
- HuggingFace Embeddings
- Automatic Remotion Code Generation
- Compiler Agent
- Automatic Retry Agent
- Video Rendering
- JSON Caching
- Unit Tests

---

# Architecture

```
                    User Prompt
                         │
                         ▼
                  Intent Parser
                         │
                         ▼
                 Image Analyzer
                         │
                         ▼
                Storyboard Writer
                         │
                         ▼
               Script Generator
                         │
                         ▼
                 Compiler Agent
                 │             │
                 ▼             ▼
            SUCCESS         FAILED
                 │             │
                 ▼             ▼
            Renderer      Retry Agent
                 ▲             │
                 └─────────────┘
```

---

# Project Structure

```
image-video-multiagent-pipeline/

│
├── agents/
│   ├── compiler.py
│   ├── image_analyzer.py
│   ├── intent_parser.py
│   ├── renderer.py
│   ├── retry_agent.py
│   ├── script_generator.py
│   └── storyboard_writer.py
│
├── graph/
│   └── pipeline.py
│
├── rag/
│   ├── chroma_db.py
│   ├── loader.py
│   └── retriever.py
│
├── models/
│
├── prompts/
│
├── output/
│
├── remotion/
│
├── tests/
│
├── utils/
│
├── app.py
├── config.py
├── state.py
└── requirements.txt
```

---

# Workflow

### 1. Intent Parser

Extracts:

- Style
- Theme
- Caption Style
- Transition
- Pacing

Example

```
Create a cinematic wedding reel
```

↓

```json
{
  "style":"cinematic",
  "transition":"fade",
  "captions":"minimal"
}
```

---

### 2. Image Analyzer

Uses Gemini Vision to analyze each image.

Returns

- description
- people count
- emotion
- importance score

---

### 3. Storyboard Writer

Uses

- User intent
- Image analysis
- RAG

to generate scene ordering.

Example

```json
[
  {
    "scene":1,
    "image":"img2.jpg",
    "duration":7,
    "caption":"Two hearts"
  }
]
```

---

### 4. Script Generator

Converts storyboard into a complete Remotion `Video.tsx`.

---

### 5. Compiler Agent

Runs

```
npx tsc --noEmit
```

Detects TypeScript compilation errors.

---

### 6. Retry Agent

If compilation fails:

- reads compiler errors
- sends them to Gemini
- generates corrected code
- recompiles automatically

Maximum retries:

```
3
```

---

### 7. Renderer

Runs

```
npx remotion render
```

Produces

```
output/video.mp4
```

---

# LangGraph Workflow

The workflow is implemented using LangGraph.

Nodes:

- Intent Parser
- Image Analyzer
- Storyboard Writer
- Script Generator
- Compiler
- Retry
- Renderer

Conditional routing automatically retries compilation until success or maximum retry count is reached.

---

# RAG

Vector Store

- ChromaDB

Embeddings

- HuggingFace
- sentence-transformers/all-MiniLM-L6-v2

Documents

- Style guides
- Remotion documentation

Retriever

Top-3 similarity search

---

# Technologies

Python

LangGraph

LangChain

Gemini 2.5 Flash

HuggingFace Embeddings

ChromaDB

React

TypeScript

Remotion

Pillow

Pytest

---

# Installation

Clone repository

```
git clone <repository-url>

cd image-video-multiagent-pipeline
```

Create virtual environment

```
python -m venv venv
```

Activate

Windows

```
venv\Scripts\activate
```

Install Python packages

```
pip install -r requirements.txt
```

Install Remotion

```
cd remotion

npm install
```

Return

```
cd ..
```

---

# Environment Variables

Create

```
.env
```

```
GEMINI_API_KEY=YOUR_API_KEY
```

---

# Run

```
python app.py
```

---

# Tests

Run

```
pytest tests -v
```

---

# Example Output

```
✓ Loaded Intent

✓ Loaded Image Analysis

✓ Loaded Storyboard

✓ Generated Video.tsx

✓ Compilation Successful

✓ Video Rendered
```

Final Output

```
output/video.mp4
```

---

# Future Improvements

- Background Music Selection
- Voice-over Generation
- Dynamic Video Length
- Multiple Rendering Templates
- Cloud Deployment
- Web UI
- Docker Support

---

# Design Decisions

### LangGraph

Used to orchestrate all agents and handle conditional retry logic.

### HuggingFace Embeddings

Selected instead of Gemini embeddings to avoid API quota limitations and provide local embedding generation.

### ChromaDB

Chosen as a lightweight local vector database for retrieval-augmented generation.

### JSON Caching

Implemented for intent parsing, image analysis, and storyboard generation to reduce repeated LLM calls and improve development speed.

### Retry Agent

Automatically fixes TypeScript compilation errors by using compiler output as feedback for the LLM.

---

# Author

**Rohit Vispute**

AI Engineer Take-home Assignment
# Local FastAPI AI Project

This project uses **uv** for fast dependency management and **Ollama** to run local LLMs and embedding models.

## Prerequisites

1.  **Install uv**:
    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```
2.  **Install Ollama**: Download it from [ollama.com](https://ollama.com/download) and ensure the application is running in your background.

---

## 1. Setup Local Models
Before running the code, you must download the specific models used for generation and embeddings.

Open your terminal and run:
```bash
# Download the LLM
ollama pull llama3.1

# Download the Embedding model
ollama pull embedding-gemma
```

---

## 2. Project Installation
Use `uv` to initialize the virtual environment and install all dependencies (including FastAPI, LangChain, and ChromaDB).

```bash
# Sync dependencies and create .venv
uv sync
```

---

## 3. Running the Project

### Start the FastAPI Server
To run your server with auto-reload enabled:
```bash
uv run fastapi dev main.py
```

### Running Scripts
If you have a standalone script (e.g., to seed your ChromaDB):
```bash
uv run python your_script.py
```

---

## 4. Troubleshooting

### VS Code Support
*   **Interpreter**: Press `Cmd+Shift+P`, search for `Python: Select Interpreter`, and choose the one in `./.venv/bin/python`.
*   **Missing Imports**: If LangChain or Chroma are not recognized, run `uv sync` again and restart the Python Language Server from the Command Palette.
*   **Ollama Connection**: Ensure `ollama serve` is running or the Ollama app is open, otherwise the project will fail to connect to `llama3.1`.

### Environment Variables
If your project requires specific API keys (e.g., LangSmith for tracing), create a `.env` file in the root directory:
```env
LANGSMITH_API_KEY=your_key_here
```

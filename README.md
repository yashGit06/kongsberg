# kongsberg
Agentic AI Training Material for Feb'26

## Project Overview

This repository contains **two RAG (Retrieval-Augmented Generation) implementations**:
- **Node.js version** (`node-rag-demo/`) - JavaScript/TypeScript implementation
- **Python version** (`py-rag-demo/`) - Python implementation

Both implementations demonstrate how to build AI systems that answer questions based on your own documents using:
- **Vector embeddings** (OpenAI)
- **Vector database** (ChromaDB)
- **LLMs** (OpenAI GPT models)

---

## Prerequisites (All Projects)

1. **OpenAI API Key**
   - Sign up at [https://platform.openai.com](https://platform.openai.com)
   - Create an API key in settings
   - Keep it safe (you'll need it for `.env` files)

2. **Node.js** (for node-rag-demo)
   - Download from [https://nodejs.org](https://nodejs.org) (LTS version recommended)
   - Verify: `node --version` and `npm --version`

3. **Python** (for py-rag-demo)
   - Python 3.10+ recommended
   - Verify: `python --version`

---

## Node.js RAG Demo (`node-rag-demo/`)

### Step 1: Setup Environment

```bash
cd node-rag-demo
npm install
```

### Step 2: Configure API Key

Edit `.env` file and add your OpenAI API key:

```bash
# .env
OPENAI_API_KEY=your_api_key_here
```

### Step 3: Start ChromaDB Server

In a **new terminal**, run:

```bash
chroma run --path ./chroma_data --port 8000
```

(First time? Install ChromaDB: `pip install chromadb`)

### Step 4: Build the Index (One-time)

In another terminal, from `node-rag-demo/`:

```bash
npm run build:index
```

**Expected output:**
```
Chroma collection 'agentic-ai-notes' populated.
```

### Step 5: Query the RAG System

```bash
npm run query:rag
```

**Expected output:**
```
[AI-generated response based on indexed documents]
```

### Modifying Documents

Edit [build-index.mjs](node-rag-demo/build-index.mjs) lines 13-16 to add your own documents, then re-run `npm run build:index`.

---

## Python RAG Demo (`py-rag-demo/`)

### Step 1: Create Virtual Environment

```bash
cd py-rag-demo
python -m venv .venv
```

### Step 2: Activate Virtual Environment

**Windows (PowerShell):**
```bash
.venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```bash
.venv\Scripts\activate.bat
```

**macOS/Linux:**
```bash
source .venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install langchain langchain-openai langchain-chroma langchain-text-splitters python-dotenv chromadb
```

Or if you have a `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Step 4: Configure API Key

Edit `.env` file and add your OpenAI API key:

```bash
# .env
OPENAI_API_KEY=your_api_key_here
```

### Step 5: Build the Index (One-time)

```bash
python build_index.py
```

**Expected output:**
```
Chroma index built at ./chroma-store
```

### Step 6: Query the RAG System

```bash
python query_rag.py
```

**Expected output:**
```
Q: Explain RAG to a junior backend developer.

A: [AI-generated explanation using your documents]

Sources:
- [1] RAG combines retrieval from a vector store with generation from an LLM...
- [2] Chroma is an open‑source vector database optimized for AI applications...
```

### Modifying Documents

Edit [build_index.py](py-rag-demo/build_index.py) lines 18-21 to add your own documents, then re-run `python build_index.py`.

### Modifying Queries

Edit [query_rag.py](py-rag-demo/query_rag.py) at the bottom to ask different questions:

```python
if __name__ == "__main__":
    ask("What is RAG?")
    ask("How does ChromaDB work?")
    ask("Explain agentic AI systems.")
```

---

## File Structure

```
kongsberg/
├── node-rag-demo/
│   ├── .env              # API key configuration
│   ├── package.json      # Node.js dependencies
│   ├── build-index.mjs   # Index builder script
│   ├── query-rag.mjs     # Query runner script
│   └── chroma_data/      # Vector store (created after running)
│
├── py-rag-demo/
│   ├── .env              # API key configuration
│   ├── build_index.py    # Index builder script
│   ├── query_rag.py      # Query runner script
│   ├── .venv/            # Virtual environment (created after setup)
│   └── chroma-store/     # Vector store (created after running)
│
├── README.md            # This file
└── .gitignore           # Git ignore rules
```

---

## Troubleshooting

### Node.js Issues

**ChromaDB connection error:**
- Make sure ChromaDB server is running: `chroma run --path ./chroma_data --port 8000`

**Module not found errors:**
- Reinstall dependencies: `npm install`

### Python Issues

**ModuleNotFoundError:**
- Ensure virtual environment is activated: `.venv\Scripts\Activate.ps1`
- Reinstall packages: `pip install -r requirements.txt`

**OpenAI API key not found:**
- Check `.env` file exists in the project folder
- Verify `OPENAI_API_KEY=` has your actual API key (not empty)
- Restart the script after updating `.env`

### General Issues

**API quota exceeded:**
- Check your OpenAI account usage at [https://platform.openai.com/account/usage](https://platform.openai.com/account/usage)

**No documents indexed:**
- Verify you have documents in the source files before running build scripts
- Check that build script completed successfully

---

## Next Steps

1. **Add your own documents** - Replace sample texts with real documentation
2. **Customize embeddings** - Modify model in `.env` or script files
3. **Adjust retrieval** - Change `k=4` in query scripts to get more/fewer sources
4. **Deploy** - Use these scripts as foundation for production RAG systems

---

## Resources

- [LangChain Docs](https://docs.langchain.com)
- [ChromaDB Docs](https://docs.trychroma.com)
- [OpenAI API Docs](https://platform.openai.com/docs)
- [RAG Pattern](https://docs.langchain.com/docs/modules/chains/popular/vector_db_qa)

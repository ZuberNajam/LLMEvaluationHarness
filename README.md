LLM Evaluation Harness for RAG Systems

Built an end-to-end local LLM evaluation framework designed to test and validate Retrieval-Augmented Generation (RAG) pipelines using automated AI evaluation workflows.

The system integrates:

FastAPI for API orchestration
Ollama for local LLM inference
Promptfoo for automated evaluation and scoring
Python-based RAG context injection
Structured JSON responses for evaluation consistency

The architecture simulates a production-style AI evaluation pipeline:

Promptfoo → FastAPI → RAG Pipeline → Ollama LLM
          ← Structured JSON Response ←
          Promptfoo Evaluation + Scoring
Key Features
Local LLM inference using Ollama (llama3)
Automated evaluation workflows with Promptfoo
RAG-style context injection from knowledge sources
Structured API responses with latency tracking
Automated regression-style testing for LLM outputs
Modular FastAPI architecture for extensibility
Unit testing with pytest
Technologies Used
Python
FastAPI
Ollama
Promptfoo
Pytest
Pydantic
REST APIs
Example Evaluation Workflow
Promptfoo sends test cases to FastAPI
FastAPI receives user questions
RAG pipeline builds contextual prompts
Ollama generates responses locally
FastAPI returns structured JSON
Promptfoo evaluates answer quality automatically
Future Enhancements
Hallucination detection
Faithfulness scoring
Vector database integration (FAISS/ChromaDB)
Embedding-based retrieval
Semantic similarity metrics
AI observability dashboards
Multi-turn conversational evaluations

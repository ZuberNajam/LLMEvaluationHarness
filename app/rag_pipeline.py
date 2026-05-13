from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
KB_PATH = BASE_DIR / "data" / "knowledge_base.txt"
#KB_PATH = Path("app/data/knowledge_base.txt")

def load_knowledge_base():
    with open(KB_PATH, "r", encoding="utf-8") as f:
        return f.read()

def build_context(question):
    kb = load_knowledge_base()
    prompt = f"""
You are a helpful project assistant.
    
Knowledge Base:
{kb}

Question:
{question}

Answer only using the provided context.
"""
    return {
        "prompt": prompt,
        "context": kb,
        "sources": ["knowledge_base.txt"],
    }

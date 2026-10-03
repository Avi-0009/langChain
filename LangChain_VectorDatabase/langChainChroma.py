from pathlib import Path

from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document


load_dotenv()


# Local Chroma DB location
base_dir = Path(__file__).resolve().parent
db_dir = base_dir / "Chroma_DB"


# Embedding model
embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)


# Create / Connect to Chroma DB
vector_store = Chroma(
    collection_name="ipl_players",
    embedding_function=embeddings,
    persist_directory=str(db_dir)
)


docs = [
    Document(
        page_content=(
            "Virat Kohli is one of the most successful and consistent "
            "batsmen in IPL history. Known for his aggressive batting "
            "style and fitness."
        ),
        metadata={
            "player_id": "player_001",
            "team": "Royal Challengers Bangalore",
            "role": "batsman"
        }
    ),
    Document(
        page_content=(
            "Rohit Sharma is one of the most successful captains in IPL "
            "history and has led Mumbai Indians to multiple titles."
        ),
        metadata={
            "player_id": "player_002",
            "team": "Mumbai Indians",
            "role": "batsman"
        }
    ),
    Document(
        page_content=(
            "MS Dhoni is a legendary wicketkeeper and finisher who has "
            "led Chennai Super Kings to multiple IPL titles."
        ),
        metadata={
            "player_id": "player_003",
            "team": "Chennai Super Kings",
            "role": "wicketkeeper"
        }
    ),
    Document(
        page_content=(
            "Jasprit Bumrah is one of the best fast bowlers in T20 cricket. "
            "He is known for his yorkers and death-over bowling."
        ),
        metadata={
            "player_id": "player_004",
            "team": "Mumbai Indians",
            "role": "bowler"
        }
    )
]


ids = [
    "player_001",
    "player_002",
    "player_003",
    "player_004"
]


# Add documents ONLY when they don't already exist
existing_data = vector_store.get()

if not existing_data["ids"]:
    vector_store.add_documents(
        documents=docs,
        ids=ids
    )
    print("Documents added.")
else:
    print("Documents already exist. Skipping insert.")


# Update player_001
updated_doc = Document(
    page_content=(
        "Virat Kohli is a former RCB captain known for "
        "consistent batting and aggressive leadership."
    ),
    metadata={
        "player_id": "player_001",
        "team": "Royal Challengers Bangalore",
        "role": "batsman"
    }
)

vector_store.update_document(
    document_id="player_001",
    document=updated_doc
)

print("Player updated.")

print(vector_store.get())
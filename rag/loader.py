from pathlib import Path
from langchain_core.documents import Document

documents = []

styles_folder = Path("docs/styles")

for file in styles_folder.glob("*.md"):

    with open(file, "r", encoding="utf-8") as f:

        text = f.read()

    documents.append(
        Document(
            page_content=text,
            metadata={
                "source": file.name
            }
        )
    )

print(f"{len(documents)} documents loaded")

for doc in documents:
    print(doc.metadata)
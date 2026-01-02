## Github Repo: https://github.com/krishnaik06/RAG-Tutorials/tree/main
## Youtube video: https://www.youtube.com/watch?v=o126p1QN_RI


    
from source.data_loader import load_all_documents
from source.vectorstore import FaissVectorStore
from source.search import RAGSearch

# Example usage
if __name__ == "__main__":
    
    #docs = load_all_documents("data")
    store = FaissVectorStore("faiss_store")
    #store.build_from_documents(docs)
    store.load()
    #print(store.query("What is attention mechanism?", top_k=3))
    
    rag_search = RAGSearch()
    query = "What is code refactoring?"
    summary = rag_search.search_and_summarize(query, top_k=3)
    print("Summary:", summary)    
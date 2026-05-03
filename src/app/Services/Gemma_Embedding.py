# from langchain_community.document_loaders import PyPDFLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings, ChatOllama

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_chroma import Chroma

# 1. Load and Split the PDF
# loader = PyPDFLoader("docs/matthes_e_python_crash_course_a_handson_projectbased_introdu.pdf")
# pages = loader.load()

# # Split text into chunks so they fit into the LLM's memory
# text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
# splits = text_splitter.split_documents(pages)

# 2. Set up the Models
embeddings = OllamaEmbeddings(model="embeddinggemma")
llm = ChatOllama(model="llama3.1")

# 3. Create the Vector Store
persist_directory = "src/app/chroma_db"

# Create the vector store with the persist_directory argument
# vectorstore = Chroma.from_documents(
#     documents=splits,
#     embedding=embeddings,
#     persist_directory=persist_directory
# )

vectorstore = Chroma(
    persist_directory = persist_directory,
    embedding_function = embeddings
)
retriever = vectorstore.as_retriever()

# 4. The RAG Chain
template = """Answer the question based only on the following context:
{context}

Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)

rag_chain = (
        {"context": retriever, "question": RunnablePassthrough()}

        | prompt
        | llm
        | StrOutputParser()
)



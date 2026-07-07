📊 Excel RAG Chatbot using Gemini, BGE-M3 & Qdrant

An intelligent Retrieval-Augmented Generation (RAG) chatbot that answers questions from an Excel dataset using Google Gemini, BAAI BGE-M3 Embeddings, and Qdrant Vector Database. The application semantically retrieves relevant employee records before generating accurate, context-aware responses.

🚀 Features:
      📄 Reads and processes Excel datasets
      🧹 Data cleaning and preprocessing using Pandas
      ✂️ Semantic chunking of employee records
      🧠 Dense & Sparse embeddings using BAAI/BGE-M3
      🔍 Semantic retrieval using Qdrant Vector Database
      🤖 Natural language responses powered by Gemini 2.5 Flash
      💬 Command Line Interface (CLI)
      🌐 Streamlit UI 
      🏗️ Modular and scalable architecture
🛠️ Tech Stack:
          Category	Technology
          Language	Python
          LLM	Google Gemini 2.5 Flash
          Embedding Model	BAAI/BGE-M3
          Vector Database	Qdrant
          Data Processing	Pandas
          Excel Reader	OpenPyXL
          UI	Streamlit
          Environment	Python Dotenv
          Package Manager	uv
🏗️ Project Architecture
                Excel Dataset
                      │
                      ▼
              Excel Loader
                      │
                      ▼
            Data Cleaning (Pandas)
                      │
                      ▼
             Semantic Chunking
                      │
                      ▼
        BGE-M3 Dense/Sparse Embeddings
                      │
                      ▼
          Qdrant Vector Database
                      │
                      ▼
           Similarity Retrieval
                      │
                      ▼
             Retrieved Context
                      │
                      ▼
          Gemini 2.5 Flash LLM
                      │
                      ▼
              Generated Answer
📂 Project Structure
excel-rag-chatbot/
│
├── streamlitVersionApp.py
├── config.py
├── .env
├── requirements.txt
├── README.md
│
├── data/
│   └── Employee Sample Data.xlsx
│
├── modules/
│   ├── __init__.py
│   ├── excel_loader.py
│   ├── chunker.py
│   ├── embedder.py
│   ├── vectordb.py
│   ├── retriever.py
│   └── chatbot.py
│
└── vectordb/
⚙️ Installation
Clone Repository
git clone https://github.com/yourusername/excel-rag-chatbot.git

cd excel-rag-chatbot
Create Virtual Environment

Using uv

uv venv

Activate

Windows
.venv\Scripts\activate
Linux / Mac
source .venv/bin/activate
Install Dependencies
uv sync

or

uv add pandas
uv add openpyxl
uv add qdrant-client
uv add FlagEmbedding
uv add google-genai
uv add python-dotenv
uv add streamlit 
🔑 Configure API Key

Create a .env file

GEMINI_API_KEY=YOUR_GEMINI_API_KEY
▶️ Run the Application
CLI Version
uv run python app.py
Streamlit Version
uv run streamlit run streamlit_app.py
📊 Example Questions
Show all employees in the IT department.
Who has the highest salary?
List employees working in Finance.
Which employees are located in Seattle?
Show employees hired after 2022.
Which employee belongs to the Marketing department?
List all HR employees.
Find employee ID E1024.
⚡ How It Works
1. Load Excel

Reads the employee dataset using Pandas.

↓

2. Clean Data
Removes duplicates
Handles missing values
Prepares records for processing

↓

3. Semantic Chunking

Groups employee information into meaningful text chunks with metadata.

↓

4. Generate Embeddings

Uses BAAI/BGE-M3 to generate semantic vector representations.

↓

5. Store in Qdrant

Stores embeddings along with metadata for fast similarity search.

↓

6. Retrieve Relevant Context

Converts the user's query into an embedding and retrieves the most relevant chunks.

↓

7. Generate Response

Gemini 2.5 Flash uses the retrieved context to generate an accurate answer.

📸 Screenshots
Command Line Interface
You: Show all employees in IT

Assistant:

The IT department includes:

• John Smith
• Emily Davis
• David Wilson
...

🔮 Future Improvements
📁 Upload custom Excel files
📑 Multi-sheet Excel support
🔍 Hybrid Retrieval (Dense + Sparse)
📚 Source citations for answers
💾 Persistent Qdrant database
📊 Dashboard with analytics
🌍 Multi-language support
⚡ FastAPI REST API
🐳 Docker deployment
📚 Learning Outcomes

Through this project, I gained practical experience with:

Retrieval-Augmented Generation (RAG)
Semantic Search
Vector Databases
Large Language Models (LLMs)
Google Gemini API
Embedding Models
Qdrant
Streamlit
Modular Python Development
🤝 Contributing

Contributions are welcome.

Fork the repository.
Create a feature branch.
Commit your changes.
Open a Pull Request.
📄 License

This project is licensed under the MIT License.

👨‍💻 Author

Suminder Singh

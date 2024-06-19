from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings

embedding = GoogleGenerativeAIEmbeddings(
    model="models/text-embedding-004", google_api_key="key"
)

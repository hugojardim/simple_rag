import chromadb
from chromadb.config import Settings
import pypdf
import pypdf
import re

caminho_pdf = "dissertacao_jessica_feliciano_coutinho.pdf"

leitor_pdf = pypdf.PdfReader(caminho_pdf)

chroma_client = chromadb.HttpClient(host='localhost', port=8000, settings=Settings(allow_reset=True, anonymized_telemetry=False))

paginas = leitor_pdf.pages

documents = []

for pagina in paginas:    
    texto = pagina.extract_text()
    texto = texto.replace('\n', ' ')
    frases = re.split(r'(?<=[.])\s+', texto) 
    frases = [frase.strip() for frase in frases if frase.strip()]
    for frase in frases:
        documents.append(frase)

ids = [str(i) for i in range(len(documents))]

collection_status = False
while collection_status != True:
    try:
        document_collection = chroma_client.get_or_create_collection(name="sample_collection")
        collection_status = True
    except Exception as e:
        pass

document_collection.add(documents=documents, ids=ids)

results = document_collection.query(query_texts="Give me some CONCLUSÕES", n_results=3)
result_documents = results["documents"][0]
for doc in result_documents:
    print(doc)
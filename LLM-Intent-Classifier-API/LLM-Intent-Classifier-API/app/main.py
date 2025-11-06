from fastapi import FastAPI, Body, Depends
from pydantic import BaseModel
from typing import Dict, Any
from .llm_service import LLMIntentClassifier, get_classifier

# Definição do esquema de dados de entrada
class ClassificationRequest(BaseModel):
    text: str = Body(..., example="Quero cancelar meu plano")

# Definição do esquema de dados de saída
class ClassificationResponse(BaseModel):
    text: str
    intent: str
    confidence: float

app = FastAPI(
    title="LLM Intent Classifier API",
    description="API para classificar a intenção do usuário usando um LLM simulado.",
    version="1.0.0",
)

@app.get("/", tags=["Health Check"])
def read_root():
    """Endpoint de verificação de saúde da API."""
    return {"status": "ok", "message": "LLM Intent Classifier API está rodando!"}

@app.post("/classify/", response_model=ClassificationResponse, tags=["Classification"])
def classify_intent(
    request: ClassificationRequest,
    classifier: LLMIntentClassifier = Depends(get_classifier)
) -> Dict[str, Any]:
    """
    Endpoint principal para classificar a intenção de um texto de entrada.
    """
    # Chama o serviço de classificação
    result = classifier.classify(request.text)
    
    # Constrói a resposta
    response_data = {
        "text": request.text,
        "intent": result["intent"],
        "confidence": result["confidence"]
    }
    
    return response_data

# Inicializa o classificador para garantir que o modelo simulado seja criado
# e o serviço esteja pronto.
get_classifier()

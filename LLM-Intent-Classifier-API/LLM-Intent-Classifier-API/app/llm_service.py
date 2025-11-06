import json
import random
import os
from typing import Dict, Any

# Caminho para o arquivo de dados simulados
DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "intents.json")
MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "model", "llm_model_v1.pkl")

class LLMIntentClassifier:
    """
    Classe que simula a lógica de inferência de um LLM para classificação de intenção.
    Na vida real, esta classe faria chamadas a uma API de LLM (ex: OpenAI, Gemini)
    ou carregaria um modelo local (ex: um modelo Hugging Face).
    """
    def __init__(self):
        self.intents_data: Dict[str, Any] = self._load_intents_data()
        self.model_loaded: bool = self._load_model_artifact()

    def _load_intents_data(self) -> Dict[str, Any]:
        """Carrega os dados de intenções simuladas."""
        try:
            with open(DATA_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Aviso: Arquivo de dados de intenções não encontrado em {DATA_PATH}. Usando dados vazios.")
            return {}

    def _load_model_artifact(self) -> bool:
        """Simula o carregamento de um artefato de modelo (LLM)."""
        # Na prática, poderíamos usar `pickle` ou `joblib` para carregar um modelo scikit-learn
        # ou carregar pesos de um modelo PyTorch/TensorFlow.
        if os.path.exists(MODEL_PATH):
            print(f"Artefato de modelo carregado com sucesso de {MODEL_PATH}")
            return True
        else:
            print(f"Aviso: Artefato de modelo não encontrado em {MODEL_PATH}. A inferência será totalmente simulada.")
            return False

    def classify(self, text: str) -> Dict[str, Any]:
        """
        Simula a classificação de intenção usando a lógica do LLM.
        
        Args:
            text: O texto de entrada a ser classificado.
            
        Returns:
            Um dicionário com a intenção e a confiança.
        """
        # Lógica de simulação:
        # 1. Tenta encontrar uma correspondência exata ou parcial nos dados simulados.
        # 2. Se não encontrar, retorna uma intenção aleatória.
        
        text_lower = text.lower()
        
        # 1. Correspondência parcial (simulação de prompt engineering/few-shot learning)
        for intent, examples in self.intents_data.items():
            for example in examples:
                if example.lower() in text_lower or text_lower in example.lower():
                    return {"intent": intent, "confidence": round(0.8 + random.random() * 0.2, 2)} # Alta confiança

        # 2. Retorna uma intenção aleatória (simulação de inferência geral do LLM)
        if self.intents_data:
            random_intent = random.choice(list(self.intents_data.keys()))
            return {"intent": random_intent, "confidence": round(0.5 + random.random() * 0.3, 2)} # Confiança média
        
        return {"intent": "desconhecida", "confidence": 0.5}

# Instância global do classificador
classifier = LLMIntentClassifier()

def get_classifier() -> LLMIntentClassifier:
    """Função utilitária para obter a instância do classificador (para injeção de dependência)."""
    return classifier

# Simulação de um artefato de modelo vazio para o Dockerfile
# Na vida real, seria um modelo treinado ou um arquivo de configuração do LLM.
if not os.path.exists(MODEL_PATH):
    # Cria um arquivo vazio para simular o artefato
    with open(MODEL_PATH, "w") as f:
        f.write("")
    print(f"Artefato de modelo simulado criado em {MODEL_PATH}")

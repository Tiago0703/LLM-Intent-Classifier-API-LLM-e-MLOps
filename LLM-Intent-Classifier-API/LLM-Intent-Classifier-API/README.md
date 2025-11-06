# LLM-Intent-Classifier-API

Este projeto demonstra a construção de um serviço de classificação de intenção de usuário utilizando um Large Language Model (LLM) e empacotado como uma API RESTful. O foco é na aplicação prática de LLMs para tarefas de Processamento de Linguagem Natural (PLN) e na implementação de práticas de MLOps, como conteinerização e versionamento de modelos.

## Funcionalidades

*   **Classificação de Intenção:** Recebe uma frase e retorna a intenção mais provável (ex: `consulta_saldo`, `falar_com_atendente`, `cancelar_servico`).
*   **API RESTful:** Implementada com FastAPI para alta performance e fácil integração.
*   **Conteinerização:** Utiliza Docker para garantir um ambiente de execução consistente e facilitar o deploy.
*   **Simulação de LLM:** Utiliza uma implementação leve para simular a inferência de um LLM, mantendo o foco na arquitetura da aplicação.

## Estrutura do Projeto

```
.
├── app/
│   ├── __init__.py
│   ├── main.py             # Ponto de entrada da API (FastAPI)
│   └── llm_service.py      # Lógica de inferência do LLM
├── data/
│   └── intents.json        # Dados de exemplo para simular as intenções
├── model/
│   └── llm_model_v1.pkl    # Modelo simulado (ou artefato de LLM)
├── Dockerfile              # Definição do ambiente Docker
├── requirements.txt        # Dependências do projeto
└── README.md
```

## Configuração e Execução

### Pré-requisitos

*   Docker
*   Python 3.9+

### 1. Construir a Imagem Docker

```bash
docker build -t llm-intent-classifier .
```

### 2. Executar o Contêiner

```bash
docker run -d --name llm-api -p 8000:8000 llm-intent-classifier
```

A API estará disponível em `http://localhost:8000`.

### 3. Testar a API

Você pode testar o endpoint de classificação usando `curl` ou uma ferramenta como o Postman:

```bash
curl -X 'POST' \
  'http://localhost:8000/classify/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "Quero saber quanto tenho na minha conta"
}'
```

**Resposta Esperada:**

```json
{
  "text": "Quero saber quanto tenho na minha conta",
  "intent": "consulta_saldo",
  "confidence": 0.95
}
```

## MLOps e LLMOps

Este projeto incorpora os seguintes conceitos de MLOps/LLMOps:

1.  **Model as a Service:** O modelo (LLM) é servido através de uma API, desacoplando a inferência da aplicação cliente.
2.  **Conteinerização:** O uso do Docker garante a reprodutibilidade do ambiente de execução.
3.  **Versionamento de Modelo:** O artefato `llm_model_v1.pkl` simula um modelo versionado, que pode ser facilmente trocado ou atualizado.

## Próximos Passos (Sugestões de Melhoria)

*   Integrar com um LLM real (ex: OpenAI, Gemini, ou um modelo Hugging Face local).
*   Adicionar um pipeline de CI/CD para automação de testes e deploy.
*   Implementar monitoramento de desvio de dados (data drift) e desvio de modelo (model drift).
*   Usar uma ferramenta de rastreamento de experimentos (ex: MLflow) para gerenciar diferentes versões do modelo.

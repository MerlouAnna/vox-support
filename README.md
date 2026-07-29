# Vox

**A secure, real-time voice support agent for IT and field-service teams, with adaptive vector + graph retrieval.**

Hermes answers support calls by phone or browser: it listens, decides whether a
question needs a fast factual lookup or multi-hop reasoning, retrieves grounded
answers from the knowledge base, speaks them back with citations, and files a
summarised ticket after the call.

- **Adaptive RAG router**: routes each query to vector search (Azure AI Search)
  for direct facts, or a knowledge graph (Cosmos DB Gremlin) for relationship and
  root-cause questions.
- **Real-time speech**: speech-to-speech over Azure Voice Live, via Azure
  Communication Services telephony and a web client.
- **Secure by construction**: authentication, authorization, and per-tenant
  isolation on a versioned FastAPI service.

WIP

from fastapi import FastAPI
from pydantic import BaseModel
from query_engine import create_query_engine

app = FastAPI()
query_engine = create_query_engine()

class QueryRequest(BaseModel):
    query: str

@app.post("/ask")
async def ask_question(request: QueryRequest):
    response = query_engine.query(request.query)
    return {"query": request.query, "response": str(response)}

from fastapi import FastAPI, Header, HTTPException, Request, status
from .schemas import DevOpsPayload

app = FastAPI()

@app.post("/DevOps")
async def devops_handler(
    payload: DevOpsPayload,
    x_parse_rest_api_key: str = Header(None),
    x_jwt_kwy: str = Header(None)
):
    api_key_valid = "2f5ae96c-b558-4c7b-a590-a501ae1c3f6c"
    
    if x_parse_rest_api_key != api_key_valid:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail="Forbidden: Invalid API Key"
        )

    return {"message": f"Hello {payload.to} your message will be send"}

@app.api_route("/DevOps", methods=["GET", "PUT", "DELETE", "PATCH"])
async def method_not_allowed(request: Request):
    return "ERROR"
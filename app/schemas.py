from pydantic import BaseModel, Field

class DevOpsPayload(BaseModel):
    message: str
    to: str
    from_user: str = Field(..., alias="from")
    timeToLifeSec: int
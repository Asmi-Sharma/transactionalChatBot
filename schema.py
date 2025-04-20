from pydantic import BaseModel

class LLMData(BaseModel):
    response: str
    isService: bool

class LLMResponse(BaseModel):
    code: str
    message: str
    details: LLMData
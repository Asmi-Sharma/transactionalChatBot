from fastapi import FastAPI, HTTPException, status
from agents import Agents
from schema import LLMResponse

app = FastAPI()


@app.get("/get-llm-response")
def process_query(history, question):
    print(history, question)
    try:
        router = Agents.route_user_query(history, question)
        if eval(router)['datasource'] == 'chitchat_llm':
            print('chitchat')
            response = Agents.chitchat_llm(history, question)
            results = {"response":response, "isService": False}
        else:
            print('service')
            response = Agents.determine_service(question)
            results = {"response":response, "isService": True}

        return LLMResponse(
                code = "200",
                message = "success",
                details = results
            )
        
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error: \n{e}")
    

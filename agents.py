from langchain_ollama.llms import OllamaLLM
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from fastapi import HTTPException, status
from prompts import Prompt

llm = OllamaLLM(model = "llama3.2:latest")

class Agents:
    def invoke_llm(prompt, i):
        print('from',i)
        response = llm.invoke(prompt)
        return response

    def route_user_query(history, question):
        try:
            prompt = Prompt.router_prompt(history, question)
            # llm_chain = prompt | llm | JsonOutputParser()
            response = Agents.invoke_llm(prompt,'router')
            print('router response',response)
            return response
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Router Error: \n{e}")
    
    def determine_service(question):
        try:
            prompt = Prompt.service_prompt(question)
            # llm_chain = prompt | llm | StrOutputParser()
            response = Agents.invoke_llm(prompt,'service')
            print('Service response:', response)
            return response
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Service Error: \n{e}")
    
    def chitchat_llm(history, question):
        try:
            prompt = Prompt.chitchat_prompt(history, question)
            # llm_chain = prompt | llm | StrOutputParser()
            response = Agents.invoke_llm(prompt,'chitchat')
            print('chitchat response:', response)
            return response
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Chitchat Error: \n{e}")
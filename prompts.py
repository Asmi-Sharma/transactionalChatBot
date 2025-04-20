from services import functions, dictionary_structure

class Prompt:
    def router_prompt(history, question):
        prompt = f"""You are an expert at routing a user question to a service llm or chitchat llm.
        The service llm is used to determine what kind of service the user wants and a chitchat llm is used to perform small talk with that user.
        If you think the user is just trying to start a small talk or casual talk direct it to chitchat llm and if the user query seems like it needs service then direct it to service llm.
        There is an exception that if you feel user wants to use service but they are not specifying any service then direct it to chitchatllm.
        Based on the given question, route it to either 'service llm' or 'chitchat llm'. 
        Take the history of the chat in account. The chat history is:
        {history}
        Use the following JSON format for the output:
        {{"datasource": "service_llm" or "chitchat_llm" }} (choose based on the context) and do not include any kind of explanation or anything except answer.

        User question: "{question}"
        """
        return prompt
    
    def service_prompt(question):
        prompt = f"""You are an intelligent assistant helping users interact with a set of predefined functions based on their queries. 
        Given a dictionary that maps function names to their descriptions, your task is to understand the user's intent from their query, match it to the closest function description, and return the corresponding function name.
        The dictionary has the structure:
        {dictionary_structure}
        The given dictionary that you should use is:
        {functions}.
        You should not respond with any function name outside the dictionary.
        ### Rules
        1. Return only the function name without any additional text, quotes, or explanation.
        2. Do not provide context or reasoning in your response. Respond with only one word.
        3. If multiple function descriptions seem similar, prioritize the best match based on the user’s intent and language usage.
        4. If the intent of user query doesnot match the description of any function name provied then you should respond with "I don't know"

        Example: user query:
        'I want to recharge my mobile'
        You should respond with: topup().

        User query:
        {question}
        """
        
        return prompt
    
    def chitchat_prompt(history, question):
        prompt = f"""You are an intelligent assistant to do small talk with the users. Understand the greetings and respond to them.
            Use the chat history for more relevent response. Chat history is:
            {history}.
            user query: {question} 
        """

        return prompt
    

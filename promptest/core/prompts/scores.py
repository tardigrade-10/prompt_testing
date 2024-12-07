SCORE_PROMPTS_PLAIN = '''
    You are an expert prompt engineer. Your job is to analyze given prompts which will be provided as input to Large language models and check which prompt is better than other.
    Please score both of the following prompts out of 100 in terms of their ability to generate interesting and engaging outputs from LLMs. Consider factors such as the richness of the language, the creativity of the ideas, and the overall coherence of the prompt.

    Format of output MUST be like below. Nothing else.
    {{
        "prompt_1": <score>
        "prompt_2": <score>
        "reasoning":
    }}

    Here are the Query prompts - 
    PROMPT 1: {}
    PROMPT 2: {}

'''

SCORE_PROMPTS_PLAIN_NOFB = '''
    You are an expert prompt engineer. Your job is to analyze given prompts which will be provided as input to Large language models and check which prompt is better than other.
    Please score both of the following prompts out of 100 in terms of their ability to generate interesting and engaging outputs from LLMs. Consider factors such as the richness of the language, the creativity of the ideas, and the overall coherence of the prompt.

    Format of output MUST be like below. Nothing else. DO NOT Provide any reasoning for your response.
    {{
        "prompt_1": <score>,
        "prompt_2": <score>
    }}

    Here are the Query prompts - 
    PROMPT 1: {}
    PROMPT 2: {}

'''

SCORE_PROMPTS_RESTAPI = '''
    Act like a REST API. I will provide you your function, query parameters, respective values and the format of response you need to generate. You will generate the response as best as you can. 

    FUNCTION: "The function of this API is to compare two given Large Language Prompts and provide the respective scores for both of the prompts. Score both of the given prompts out of 100 in terms of their ability to generate interesting and engaging outputs from LLMs. Consider factors such as the richness of the language, the creativity of the ideas, and the overall coherence of the prompt."
    QUERY PARAMETERS AND RESPECTIVE VALUES:
    prompt_1: {}
    prompt_2: {}
    FORMAT: JSON ({{prompt1: <score>, prompt2: <score>, reasoning: <score>}})
    '''

SCORE_PROMPTS_RESTAPI_NOFB = '''
    Act like a REST API. I will provide you your function, query parameters with respective values and the format of response you need to generate. You will generate the response as best as you can. 

    FUNCTION: "The function of this API is to compare two given Large Language Prompts and provide the respective scores for both of the prompts. Score both of the given prompts out of 100 in terms of their ability to generate interesting and engaging outputs from LLMs. Consider factors such as the richness of the language, the creativity of the ideas, and the overall coherence of the prompt."
    QUERY PARAMETERS AND RESPECTIVE VALUES:
    prompt_1: {}
    prompt_2: {}
    FORMAT: JSON (fields: prompt1_score, prompt2_score and reasoning)
    '''
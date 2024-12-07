import openai
from .env_config import Config
from .utils import model_type, clean_text, token_usage
import tiktoken
import json
from .prompts.optimizer import OPTIM_PROMPTENGCOMP_TWOSHOTS, OPTIM_STRONG_THREE_SHOTS
from .prompts.scores import SCORE_PROMPTS_PLAIN, SCORE_PROMPTS_PLAIN_NOFB, SCORE_PROMPTS_RESTAPI, SCORE_PROMPTS_RESTAPI_NOFB
openai.api_key = Config.OPENAI_API_KEY


def setting_api_key(api_key):
    try:
        openai.api_key = api_key
        openai.Completion.create(
            model="text-davinci-002",
            prompt="Say Nothing",
            max_tokens=7,
            temperature=0
        )
        return True
    except Exception as e:
        if str(type(e)) == "<class 'openai.error.AuthenticationError'>":
            return str(type(e))
        else:
            return str(e)
        

def prompt_optim(input_prompt, model):
    super_prompt = OPTIM_PROMPTENGCOMP_TWOSHOTS
    # if model in model_type.keys():
    #     if model_type[model] == "completion":
    #         response = openai.Completion.create(
    #                         model=model,
    #                         prompt=super_prompt.format(inp),
    #                         max_tokens=500,
    #                         temperature=0
    #                     )
    #         output = response["choices"][0]["text"]
    # model_type[model] == "chat_completion"

    response = openai.ChatCompletion.create(
                        model=model,
                        messages=[{"role": "system", "content": super_prompt},
                            {"role": "user", "content": f'''This year's QUERY: {input_prompt}
                                                            WINNING_OPTIMIZED_PROMPT:'''}
                            ],
                        temperature=0
                        )
    output = response["choices"][0]["message"]["content"]
    # else:
    #     return Exception("provide right model")0
    output = clean_text(output)
    # usage summary
    token_usage_ = token_usage(response)
    return output, token_usage_


def prompt_score(prompt1:str, prompt2:str, model:str, feedback:bool):
    if feedback:
        super_prompt = SCORE_PROMPTS_RESTAPI
    else:
        super_prompt = SCORE_PROMPTS_RESTAPI_NOFB
    if model in model_type.keys():
        if model_type[model] == "completion":
            response = openai.Completion.create(
                            model=model,
                            prompt=super_prompt.format(prompt1, prompt2),
                            max_tokens=500,
                            temperature=0
                        )
            output = response["choices"][0]["text"]
        elif model_type[model] == "chat_completion":
            response = openai.ChatCompletion.create(
                            model=model,
                            messages=[
                                {"role": "user", "content": super_prompt.format(prompt1, prompt2)}
                                ],
                            temperature=0
                            )
            output = response["choices"][0]["message"]["content"]
    else:
        return Exception("Error: provide right model") 
    
    output = output.replace('\n', '')
    output = output.replace('\\', '')
    output = ' '.join(output.strip().split())
    print(output)
    output = json.loads(output)

    token_usage_ = token_usage(response)
    return output, token_usage_
    

def token_counter(input: str = None, model: str = "text-embedding-ada-002") -> int:
    if input is None or input.strip() == "":
        raise ValueError("Input text cannot be empty or None.")
    try:
        resp = openai.Embedding.create(
            model=model,
            input=input
        )
        token_count = resp["usage"]["prompt_tokens"]
        return token_count
    except openai.OpenAIError as e:
        # Handle OpenAI API errors
        print("OpenAI API error:", str(e))
        raise
    except Exception as e:
        # Handle other exceptions
        print("An error occurred:", str(e))
        raise


def prompt_embeddings(input: str = None, model: str = "text-embedding-ada-002"):
    try:
        resp = openai.Embedding.create(
            model=model,
            input=input
        )
    except Exception as e:
        # Handle any exceptions and raise a ValueError
        raise ValueError(f"Error generating embeddings: {str(e)}")
    embeddings = resp["data"]["embedding"]
    return embeddings


def prompt2tokens(prompt):
    encoding = tiktoken.get_encoding("cl100k_base")
    embeddings = encoding.encode(prompt)
    tokens = [encoding.decode_single_token_bytes(token) for token in embeddings]
    return tokens, len(tokens)


# def prompt_shortner(prompt, max_tokens):
    



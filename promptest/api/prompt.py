from fastapi import APIRouter
import time
from typing import Optional
from ..core.prompt_eval import prompt_embeddings, token_counter, prompt2tokens, setting_api_key, prompt_optim, prompt_score


router = APIRouter(
    prefix="/prompt"
)


@router.get('/set_api_key')
async def set_api_key(openai_api_key):
    resp = setting_api_key(openai_api_key)
    if resp == True:
        return {"message": "OPENAI_API_KEY set"}
    else:
        return {"message": resp}


@router.get('/token-count')
async def token_count(prompt, model:Optional[str] = "text-embedding-ada-002"):
    count = token_counter(prompt, model)
    return {"input_prompt": prompt, "count": count}


@router.get('/embeddings')
async def prompt_embeddings(prompt, model:Optional[str]="text-embedding-ada-002"):
    embedding = prompt_embeddings(prompt, model)
    return {"input_prompt": prompt, "embedding": embedding}


@router.get('/optimize')
async def optimized_prompt(prompt, model:Optional[str] = "gpt-3.5-turbo"):
    optimized, token_usage = prompt_optim(prompt, model)
    return {"input_prompt": prompt, "optimized_prompt": optimized, "token_usage": token_usage}


@router.get('/prompt_scores')
async def prompt_score_check(prompt1, prompt2, model:Optional[str] = "gpt-3.5-turbo", reasoning: Optional[bool] = True):
    start_time = time.time()
    scores, token_usage = prompt_score(prompt1, prompt2, model, reasoning)
    return {"scores": scores, "token_usage": token_usage, "latency(s)": round(time.time() - start_time, 2)}


@router.get('/to_tokens')
async def promt_to_tokens(prompt):
    tokens, token_count = prompt2tokens(prompt)
    return {"input_prompt": prompt, "tokens":tokens, "token_count": token_count}


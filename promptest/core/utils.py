

def clean_text(text):
    output = text.replace('\n', '')
    output = output.replace('\\', '')
    output = output.replace('\"', '')
    output = ' '.join(output.strip().split())
    return output


def token_usage(response):
    usage = response["usage"]
    input_tokens = usage["prompt_tokens"]
    output_tokens = usage["completion_tokens"]
    total_tokens = usage["total_tokens"]
    token_usage_ = {"input_tokens": input_tokens,  "output_tokens": output_tokens, "total_tokens": total_tokens}
    return token_usage_

model_type = {
        "gpt-4": "chat_completion",
        "gpt-4-0314": "chat_completion",
        "gpt-4-32k": "chat_completion",
        "gpt-4-32k-0314": "chat_completion",
        "gpt-3.5-turbo": "chat_completion",
        "gpt-3.5-turbo-0301": "chat_completion",
        "text-davinci-003": "completion",
        "text-davinci-002": "completion",
        "text-curie-001": "completion",
        "text-babbage-001": "completion",
        "text-ada-001": "completion",
        "text-embedding-ada-002":"embeddings"
    }
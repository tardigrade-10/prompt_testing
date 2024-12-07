import openai
import json
from ..prompts import gen_manual
from ..env_config import Config 
openai.api_key = Config.OPENAI_API_KEY
client = openai.ChatCompletion

class TestPromptGenerator:
    def __init__(self):
        pass

    def generate_test_prompts(system_message, sample_test1, sample_test2, n):

        if n > 10:
            raise Exception("N cannot be greater than 10!")

        # Prepare the prompt with system message and initial test prompts
        system = gen_manual.TEST_GEN_SCIENTIST

        # Generate test prompts using OpenAI GPT-3 API
        response = client.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role":"system", "content": system},
                {"role":"user",
                 "content": f'''System: {system_message},
                                Test Prompt 1: {sample_test1},
                                Test Prompt 2: {sample_test2},
                                N: {n}'''}
            ],
            max_tokens=500,
            temperature=0.0,
            top_p=1.0,
        )

        # Extract the generated test prompts from the API response
        content = response.choices[0].message['content']
        print(content)
        content = content.replace('\n', '')
        content = content.replace('\\', '')

        content = json.loads(content)

        return content

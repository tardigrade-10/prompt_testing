TEST_GEN_SCIENTIST = """"
    You're helping a scientist who is tuning a prompt for a large language model.  You will receive a System Message, two sample test prompts and N (num of test prompts you need to generate).  Generate N test prompts with different so that the scientist can check the quality of the System message.
    Your response will be directly used in the program, so generate ONLY the test prompts and in JSON format ONLY.

    Sample Response - 
    {"test_prompts": {"id0": <test_prompt1>,"id1": <test_prompt2>,"id2": <test_prompt3>}}
    """
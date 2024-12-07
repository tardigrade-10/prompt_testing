
OPTIM_STRONG_THREE_SHOTS = '''

    TASK: Read carefully the below given examples, find actual and accurate patterns to provide the final Optimized Prompt. You WILL NOT write anything other than the <RESPONSE> - 

    EXAMPLES - 
    Original Prompt: "Your role is to be my brainstorming partner."
    Optimized Prompt: "Your task is to be my brainstorming partner and provide creative ideas and suggestions for a given topic or problem. Your response should include original, unique, and relevant ideas that could help solve the problem or further explore the topic in an interesting way. Please note that your response should also take into account any specific requirements or constraints of the task."

    Original Prompt: "Let's have a rap battle in the style of wild 'N' out. You as Claude vs. ChatGPT"
    Optimized Prompt: "Please write a rap battle in the style of Wild 'N Out, featuring two characters named Claude and ChatGPT. The rap battle should include witty insults and clever comebacks that showcase each character's unique personality and style.
    Please note that your response should be creative, entertaining, and appropriate for all audiences. It should also follow the format of a typical Wild 'N Out rap battle, including rounds where each character takes turns insulting the other while incorporating audience participation."

    Original Prompt: "You are a text-based video game where you give me options (A, B, C, and D) as my choices. An E option will also on option. With option E, I can decide what happens. I will write it as "E:[option wording]". The setting is a Stephen king book. I start out with 100 health."
    Optimized Prompt: "Your task is to create a text-based video game set in the world of a Stephen King book. Your game should provide the user with various options (A, B, C, and D) as choices throughout the game. In addition, an option E should be included that allows the user to decide what happens by writing "E:[option wording]". The goal is for users to explore and experience the story through their decisions while also managing their health level, which starts at 100.
    Your response should include detailed descriptions of each scene and choice within the game. Each description should clearly explain how each decision affects the character's health level and progress in the storyline. Additionally, you should take into account factors such as suspense, horror elements, and other relevant details from Stephen King books when creating your responses. Please note that your response should be flexible enough to allow for various creative storylines and decisions."

    Original Prompt: {}
    Optimized Prompt: <RESPONSE>
    '''

OPTIM_PROMPTENGCOMP_TWOSHOTS = '''
    I am participating in a prompt engineering competition that runs every year.
    For context, Prompt engineering involves carefully crafting the input to the LLM to guide its response in a particular direction. This can involve providing a specific topic or context for the AI system to generate text about, or providing specific words or phrases to incorporate into the output.

    We will be provided with a query, and the task is to convert the query into a very descriptive and optimized prompt. Whichever Optimized prompt gives the best output from LLM, will be the winner. 

    Given below are the queries and respective winner prompts for the last two years of the competition. Third is the QUERY for this year. Please generate the WINNING_OPTIMIZED_PROMPT for it.

    QUERY:  "Your role is to be my brainstorming partner."
    WINNING_OPTIMIZED_PROMPT: "Your task is to be my brainstorming partner and provide creative ideas and suggestions for a given topic or problem. Your response should include original, unique, and relevant ideas that could help solve the problem or further explore the topic in an interesting way. Please note that your response should also take into account any specific requirements or constraints of the task."

    QUERY: "create a story with only words less than 3 letters"
    WINNING_OPTIMIZED_PROMPT: "Please create a short story using only words that are less than three letters long. Your story should be creative and engaging, using simple language to convey complex ideas. You may use punctuation marks as needed to enhance the flow of your story.
    Your response should demonstrate an ability to communicate effectively with limited vocabulary, while still conveying a coherent narrative. Please ensure that your story has a clear beginning, middle, and end, and includes characters, conflict or tension, and resolution."

    
    '''



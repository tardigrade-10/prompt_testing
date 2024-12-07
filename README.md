# OpenAgent Testing framework

install dependencies - 
```bash
pip install -r requirements.txt
```

Config - 
- Add required values(OPENAI_API_KEY for now) in config_template.yaml and save the file as config.yaml


run- (from root folder)
```bash
python -m uvicorn promptest.main:app --reload
```

Check api docs at localhost:8000/docs endpoint

### Current Functionalities
- Automated Prompt Optimization
- Two Prompts Comparison
- Prompt to Embeddings Generation
- Prompt to Token Generation
- Test Case Prompts Generation
-  




### ChatGPT Based Support Bot

This is a support bot based on the ChatGPT by <a href="https://onlyoneaman.com" target="_blank">onlyoneaman</a> which 
provides information to your customers based on your knowledge base.

### How to use

1. Clone the repository
```
git clone git@github.com:onlyoneaman/chatgpt-support-bot.git
```

2. Install the dependencies
```
pip install -r requirements.txt
```

3. Add OpenAI API key to the environment variables (.env)
```
# .env
OPENAI_KEY=YOUR_OPENAI_KEY_HERE
```

4. Create Embeddings for Knowledge Base
```
python embed_text.py
```

5. Run the bot
```
python answer.py
```

### Adding Knowledge Base

You can add documents to the knowledge base by adding them to the `documents` folder.
Files should be in .txt format. 
After adding the documents, you need to run the `embed_text.py` script to create embeddings for the documents.

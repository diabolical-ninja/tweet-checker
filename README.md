# Tweet Checker 🐦

Leveraging an LLM to determine whether a tweet is:
- Biased (0 = far left, 5 = neutral, 10 = far right)
- Factually accurate (out of 5)
- And summarise why

And yes, I know, the LLM obviously doesn't know if new events are true/false but we're doing it anyway. 

## Usage

Unfortunately the free tier of the Twitter API does not allow `GET`s so you'll have to be a common-day pleb & copy+paste tweet info across (strictly speaking you're not confined to tweets tbh). Don't forget to upload any attached photos (only photos) for additional context. 

{insert a little gif}

## Running

The apps allows you to pick from the 3 main close-source models. You'll need an API for each (or modify the app to just use 1). Add it to your `.env` file, ala `.env.example`:
- `ANTHROPIC_API_KEY="a really really good key"`
- `OPENAI_API_KEY="also a really good key"`
- `GOOGLE_API_KEY="possibly the best good key"`

Run the app:
```bash
poetry install
poetry run streamlit run app.py
```
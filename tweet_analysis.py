# %%

from dotenv import find_dotenv, load_dotenv
from langchain.globals import set_verbose
from langchain_anthropic import ChatAnthropic

from prompt import PARSER, format_and_return_prompt
from utils import format_image_prompt

set_verbose(True)
load_dotenv(find_dotenv(usecwd=True))


# Instantiate LLM
claude_llm = ChatAnthropic(
    model="claude-3-5-sonnet-20240620",
    temperature=0,
    timeout=None,
    max_retries=2,
)

selected_model = "Claude"
if selected_model == "Claude":
    llm = claude_llm
# elif selected_model == "OpenAI":
#     llm = openai_llm
else:
    raise ValueError(f"Model {selected_model} not supported")


def analyse_tweet(tweet, attachments):

    num_attachments = len(attachments)
    image_attachments = [format_image_prompt(attachment) for attachment in attachments]

    prompt = format_and_return_prompt(tweet, image_attachments)

    query_chain = prompt | llm | PARSER

    return query_chain.invoke(
        {
            "num_attachments": num_attachments,
            "tweet": tweet,
        }
    )

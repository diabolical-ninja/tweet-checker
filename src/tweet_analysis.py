from dataclasses import asdict

from dotenv import find_dotenv, load_dotenv
from langchain.globals import set_verbose
from langchain_anthropic import ChatAnthropic
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI

from src.prompt import PARSER, TweetAnalysis, format_and_return_prompt
from src.utils import format_image_url_prompt

set_verbose(True)
load_dotenv(find_dotenv(usecwd=True))

TEMPERATURE = 0
MAX_RETRIES = 2


# Instantiate LLM
CLAUDE_LLM = ChatAnthropic(
    model="claude-3-5-sonnet-20240620",  # type: ignore
    temperature=TEMPERATURE,
    max_retries=MAX_RETRIES,
)

OPENAI_LLM = ChatOpenAI(
    model="gpt-4o-2024-08-06", temperature=TEMPERATURE, max_retries=MAX_RETRIES
)

GEMINI_LLM = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro", temperature=TEMPERATURE, max_retries=MAX_RETRIES
)


def select_llm(model_name: str) -> BaseChatModel:
    """Returns an instantiated of the desired LLM.

    Args:
        model_name (str): Which model to instantiate. Allowable values are:
            - Claude
            - OpenAI
            - Gemini

    Raises:
        ValueError: Invalid model name.

    Returns:
        BaseChatModel: Instantiated LLM
    """
    if model_name == "Claude":
        return CLAUDE_LLM
    elif model_name == "OpenAI":
        return OPENAI_LLM
    elif model_name == "Gemini":
        return GEMINI_LLM
    else:
        raise ValueError(f"Model {model_name} not supported")


def analyse_tweet(
    tweet: str, attachments: list, model_name: str = "Claude"
) -> TweetAnalysis:
    """Orchestrates generating a prompt and analysing a tweet via the selected LLM.

    Args:
        tweet (str): Tweet text
        attachments (list): Any attachments to the tweet. Can be of length 0.
        model_name (str, optional): Selected Model. Defaults to "Claude". Allowable values are:
            - Claude
            - OpenAI
            - Gemini

    Returns:
        TweetAnalysis: LLM output containing the tweet analysis.
    """

    num_attachments = len(attachments)
    image_attachments = [
        asdict(format_image_url_prompt(attachment)) for attachment in attachments
    ]

    formatted_prompt = format_and_return_prompt(tweet, image_attachments)

    llm = select_llm(model_name)
    query_chain = formatted_prompt | llm | PARSER

    model_response: TweetAnalysis = query_chain.invoke(
        {
            "num_attachments": num_attachments,
            "tweet": tweet,
        }
    )
    return model_response

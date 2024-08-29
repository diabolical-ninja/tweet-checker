from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import ChatPromptTemplate
from langchain.schema import HumanMessage
from langchain_core.pydantic_v1 import BaseModel, Field


class Bias(BaseModel):
    rating: int = Field(description="Bias rating between 1 and 10")
    spectrum: str = Field(
        description="Spectrum of bias (left learning, neutral, right leaning)"
    )


class FactualAccuray(BaseModel):
    rating: int = Field(description="Factual accuracy rating between 1 and 5")
    description: str = Field(description="description of the accuracy rating")


class TweetAnalysis(BaseModel):
    bias: Bias
    accuracy: FactualAccuray
    summary: str = Field(description="Summary of the tweet")


PARSER = PydanticOutputParser(pydantic_object=TweetAnalysis)

TEXT_PROMPT_TEMPLATE = """
Assess the following tweet for bias. Perform the following tasks:
- Rate it on a scale between 1 (very left) & 10 (very right) with 5 being neutral. 
- Where possible rate the factual accuracy of the tweet with 1 being very incorrect & 5 being very correct. 
- Provide a summary of the tweet, and highlight all excessively left or right leaning points. 

{format_instructions}

The tweet had {num_attachments} attachments. The tweet is as follows:

{tweet}
"""


def format_and_return_prompt(tweet, image_attachments: list):

    num_attachements = len(image_attachments)
    content = [
        {
            "type": "text",
            "text": TEXT_PROMPT_TEMPLATE.format(
                tweet=tweet,
                num_attachments=num_attachements,
                format_instructions=PARSER.get_format_instructions(),
            ),
        },
        *image_attachments,
    ]

    prompt_template = ChatPromptTemplate.from_messages([HumanMessage(content=content)])

    return prompt_template

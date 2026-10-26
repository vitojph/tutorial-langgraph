from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

load_dotenv()


class BinaryAnswer(BaseModel):
    is_true: bool = Field(
        description="""Whether the answer to the question is yes or no. True if yes otherwise False."""
    )


binary_question_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            Answer this question as True for "yes" and False for "no".
            No other answers are allowed:

            {question}
            """,
        )
    ]
)

binary_question_model = ChatOpenAI(model="gpt-6-luna", use_responses_api=True)

BINARY_QUESTION_CHAIN = (
    binary_question_prompt | binary_question_model.with_structured_output(BinaryAnswer)
)

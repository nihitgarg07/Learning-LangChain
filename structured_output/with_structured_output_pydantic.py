from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict , Annotated , Optional , Literal , cast
from pydantic import BaseModel,Field


# Loading the API Key
load_dotenv()

# Creating the Model
model = ChatOpenAI()

# Review String
review = """I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don’t use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:

Insanely powerful processor (great for gaming and productivity)

Stunning 200MP camera with incredible zoom capabilities

Long battery life with fast charging

S-Pen support is unique and useful

Cons:

Bulky and heavy—not great for one-handed use

Bloatware still exists in One UI

Expensive compared to competitors
"""

# Creating Schema
class Review(BaseModel):
    Key_themes: list[str] = Field(description="Write down all the key themes discussed in the review in a list")
    summary: str = Field(description="A brief summary of the reivew ")
    sentiment: Literal['POS','NEG'] = Field(description="Return sentiment of the review either negative ,positive or neutral")
    pros: Optional[list[str]] = Field(description= "write down all the pros inside the list")
    cons: Optional[list[str]] = Field(description="write down all the cons inside the list")

# now passing the Schema to the model for structure output    
structured_model = model.with_structured_output(Review)

# now giving the prompt to the structured model
result = cast(Review,structured_model.invoke(review))



# printing resultsw
print(type(result))
print(result.summary)


# print(result.summary)
# print(result['sentiment'])
# print(result['Key_themes'])
# print(result['pros'])
# print(result['cons'])


from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import uvicorn
import base64
import fitz
import base64
from langchain.chains import TransformChain
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
    
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_core.runnables import chain
import os
import uuid
from dotenv import load_dotenv
load_dotenv()


def load_image(inputs: dict) -> dict:
    """Load image from file and encode it as base64."""
    image_path = inputs["image_path"]
  
    def encode_image(image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    image_base64 = encode_image(image_path)
    return {"image": image_base64}

load_image_chain = TransformChain(
    input_variables=["image_path"],
    output_variables=["image"],
    transform=load_image,
    verbose=False
)

class MenuInformation(BaseModel):
    after_takeoff_meals: list[str] = Field(description="Position of takeoff selections maeals at between dine on demand and before landing sections.")
    desserts: list[str]  = Field(description="Selections of desserts")
    before_landing_meals: list[str] = Field(description="Before landing meal options position at bottom of the Before landing.")


class ImageInformation(BaseModel):
    """Information about an image."""
    turkish_text_in_image: str = Field(description="Get complated Turkish Menu Side texts from the image.")
    english_text_in_image: str = Field(description="Get complated English Menu Side texts from the image.")


@chain
def image_model(inputs: dict) -> str | list[str] | dict:
    """Invoke model with image and prompt."""
    model = ChatOpenAI(temperature=0.0, model="gpt-4o", max_tokens=4096,
                        api_key=os.getenv("OPENAI_API_KEY"))
    msg = model.invoke(
                [HumanMessage(
                content=[
                {"type": "text", "text": inputs["prompt"]},
                {"type": "text", "text": parser.get_format_instructions()},
                {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{inputs['image']}"}},
                ])]
                )
    return msg.content

def structred_out(menu:str):
    model = ChatOpenAI(temperature=0.0, model="gpt-4o-mini", max_tokens=4096,
                       api_key=os.getenv("OPENAI_API_KEY"))
    prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "You are an expert cooker. "
                    "Only extract relevant information from the meal menu text."
                    "If you do not know the value of an attribute asked to extract, "
                    "return null for the attribute's value."
                ),
                ("human", "{text}"),
            ]
        )
    runnable = prompt | model.with_structured_output(
        schema=MenuInformation, include_raw=False)
    response = runnable.invoke(
        {"text": menu}
    )
    return response


def get_image_informations(image_path: str) -> dict:
    vision_prompt = """
        The Turkish and English texts is divided into 2 as content.
        With the information given in the Description field, take and return the relevant field range in the menu.
    """
    
    vision_chain = load_image_chain | image_model | parser
    return vision_chain.invoke({'image_path': f'{image_path}', 
                                'prompt': vision_prompt})

parser = JsonOutputParser(pydantic_object=ImageInformation)

app = FastAPI()

@app.post("/extract_menu_items")
async def extract_menu_items(file: UploadFile = File(...)):
    try:
        # Read the uploaded file
        content = await file.read()
        file_name = str(uuid.uuid4()) 
        # save file a to temp
        with open(file_name+ ".pdf", "wb") as f:
            f.write(content)
        dpi = 300  # choose desired dpi here
        zoom = dpi / 72  # zoom factor, standard: 72 dpi
        magnify = fitz.Matrix(zoom, zoom)  # magnifies in x, resp. y direction
        doc = fitz.open(file_name+ ".pdf")  # open document
        for page in doc:
            pix = page.get_pixmap(matrix=magnify)  # render page to an image
            pix.save(file_name+".png")

        result = get_image_informations(file_name+".png")
        result_tr = result["turkish_text_in_image"]
        result_en = result["english_text_in_image"]

        new_result_tr = structred_out(result_tr)
        new_result_en = structred_out(result_en)
        
        return {
            "turkish_menu": new_result_tr,
            "english_menu": new_result_en
        }

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host="localhost", port=8004)

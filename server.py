from fastapi import FastAPI
from configs import TranslationRequest, TranslationResponse, get_languages
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
async def root():
    return {"message": "Home route of the api"}


@app.get('/languages')
async def available_languages() -> dict[str, str]:
    return get_languages()


@app.post('/translate', response_model=TranslationResponse)
async def translate(body: TranslationRequest):
    response = translation_model(body.initial, body.final, body.input)
    return response


def translation_model(initial, final, input):
    return TranslationResponse(
        intitial=initial, final=final, input=input, output="papa")

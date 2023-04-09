from pydantic import BaseModel
import json


class TranslationRequest(BaseModel):
    initial: str
    final: str
    input: str


class TranslationResponse(BaseModel):
    intitial: str
    final: str
    input: str
    output: str


def get_languages() -> dict[str, str]:
    with open('languages.json', mode='r', encoding="utf-8") as languages_file:
        languages = json.load(languages_file)
    return languages

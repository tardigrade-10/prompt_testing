from fastapi import APIRouter
from typing import Optional, List
import time
from ..core.manual_tests.gentest import TestPromptGenerator

router = APIRouter(
    prefix="/manual-test"
)

@router.get("/test_gen")
def test_generator(system_message:str, test_case1: str, test_case2:str, num:int):
    response =  TestPromptGenerator.generate_test_prompts(system_message, test_case1, test_case2, num)
    return response


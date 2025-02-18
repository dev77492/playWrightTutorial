import asyncio
import os

from browser_use.agent.service import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import SecretStr


async def siteValidation():
    os.environ["GEMINI_API_KEY"]= "<your key>"
    task =(
        'Important: I am UI Automation tester validating the tasks'
        'Open website https://rahulshettyacademy.com/loginpagePractise/'
        'Login with username and password. login Details available in the same page'
        'After login, select first 2 products and add them to cart'
        'Then checkout and store the total value you see in screen'
        'Increase the quantity of any product and check if total value update accordingly'
        'checkout and select country, agree terms and purchase'
        'verify thankyou message is displayed'
    )

    api_key = os.environ["GEMINI_API_KEY"]

    llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=SecretStr(api_key))
    agent = Agent(task,llm,use_vision=True)
    history = await agent.run()
    test_result=history.final_result()
    print(test_result)



asyncio.run(siteValidation())

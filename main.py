from agents import Agent, Runner,InputGuardrailTripwireTriggered,OutputGuardrailTripwireTriggered
from config import config # from  /config.py
from guardrails import math_guardrail_for_input,non_political_guardrail_for_output # from  /guardrails.py
import asyncio
from pydantic import BaseModel

class MessageOutput(BaseModel): 
    response: str

agent = Agent(  
    name="Math support agent",
    instructions="You are a customer support agent. You help customers with their math questions.",
    input_guardrails=[math_guardrail_for_input],
    output_guardrails=[non_political_guardrail_for_output],
    output_type=MessageOutput
)

async def main():
    # This should trip the guardrail
    try:
        user_input=str(input('Enter your math question: '))
        res=await Runner.run(agent, input=user_input,run_config=config)
        print("Guardrail didn't trip - this is unexpected")
        print(res.final_output)

    except InputGuardrailTripwireTriggered:
        print("Math homework guardrail tripped should'vs asked for a math question")

    except OutputGuardrailTripwireTriggered:
        print("Political guardrail tripped")    


if __name__ == "__main__":
    asyncio.run(main())

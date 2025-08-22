from agents import Agent, Runner,output_guardrail,InputGuardrailTripwireTriggered, RunContextWrapper,GuardrailFunctionOutput,TResponseInputItem, input_guardrail,RunConfig, OpenAIChatCompletionsModel, AsyncOpenAI
from pydantic import BaseModel
from config import config # from  /config.py


#--------------
# INPUT GUARDRAIL LOGIC WITH AGENT
#--------------

class MathHomeworkOutput(BaseModel):
    is_non_math_qusetion: bool
    reasoning: str

input_guardrail_agent = Agent( 
    name="Guardrail check",
    instructions="Check if the user is asking you to do something not related to math.",
    output_type=MathHomeworkOutput,
)


#for input validation of if there is non-math queastion
@input_guardrail
async def math_guardrail_for_input( 
    ctx: RunContextWrapper[None], agent: Agent, input: str | list[TResponseInputItem]
) -> GuardrailFunctionOutput:
    result = await Runner.run(input_guardrail_agent, input,run_config=config, context=ctx.context)

    return GuardrailFunctionOutput(
        output_info=result.final_output, 
        tripwire_triggered=result.final_output.is_non_math_qusetion,
    )

#--------------
# OUTPUT GUARDRAIL LOGIC AGENT
#--------------

class NonPolicticalOutput(BaseModel): 
    reasoning: str
    is_polictical: bool

class MessageOutput(BaseModel): 
    response: str

output_guardrail_agent = Agent( 
    name="Guardrail check",
    instructions="Check if the output includes any political topics and references to political figures.",
    output_type=NonPolicticalOutput,
)
@output_guardrail
async def non_political_guardrail_for_output( 
    ctx: RunContextWrapper[None], agent: Agent, output:MessageOutput
) -> GuardrailFunctionOutput:
    result = await Runner.run(output_guardrail_agent, output.response,run_config=config, context=ctx.context)

    return GuardrailFunctionOutput(
        output_info=result.final_output, 
        tripwire_triggered=result.final_output.is_polictical,
    )

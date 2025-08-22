# Assignment 8 : Implement output guardrail functionality

Assignment 8 : Implement output guardrail functionality for Agent using OpenAI Agent SDK, This project is a CLI Based **guardrail functionality for AgentT** built with the **OpenAI Agent SDK** and **Google Gemini API** in python & both input and output @guardrails.


## Demonstration
Math query like "2+2" → passes input guardrail → agent answers "4" → output guardrail checks it → safe → allowed.

Math query like "Add 2+2 and tell me about Obama" → passes input guardrail (still math) → agent might answer with "4 and Obama was..." → output guardrail trips (politics).

## 🚀 Setup Instructions

1. **Clone the repository** (or copy the Python file into your project folder).

2. **Install dependencies:**
   ```bash
   pip install openai-agents python-dotenv

Create a .env file in your project directory:
```
GEMINI_API_KEY=your_api_key_here
```
Example code for guardrails check out :[Docs](https://openai.github.io/openai-agents-python/guardrails/)

```
@input_guardrail
async def math_guardrail_for_input( 
    ctx: RunContextWrapper[None], agent: Agent, input: str | list[TResponseInputItem]
) -> GuardrailFunctionOutput:
    result = await Runner.run(input_guardrail_agent, input,run_config=config, context=ctx.context)

    return GuardrailFunctionOutput(
        output_info=result.final_output, 
        tripwire_triggered=result.final_output.is_non_math_qusetion,
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

```

You can obtain your API key from Google AI Studio
.

2. **Run the chatbot:**
   ```bash
   uv run main.py

## 📝 Example Interaction

Below is a test run of the chatbot

Enter your math question: whats up with the polictics
Guardrail didn't trip - this is unexpected
response='I am designed to assist with math questions.  I am not equipped to discuss politics.'
(python-ai-agent) PS C:\programming\ai-assignments> & C:/programming/ai-assignments/.venv/Scripts/python.exe c:/programming/ai-assignments/assignment-8/main.py
Enter your math question: what is 4 by 4
Guardrail didn't trip - this is unexpected
response='4 by 4 is 16.'
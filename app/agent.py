import json
import sys

from app.tools import TOOLS, execute_tool


def run(client, prompt):
    messages = [{"role": "user", "content": prompt}]

    while True:
        response = client.chat.completions.create(
            model="anthropic/claude-haiku-4.5",
            messages=messages,
            tools=TOOLS,
        )

        if not response.choices:
            raise RuntimeError("no choices in response")

        msg = response.choices[0].message
        messages.append(msg.model_dump(exclude_none=True))

        if not msg.tool_calls:
            return msg.content

        for tool_call in msg.tool_calls:
            name = tool_call.function.name
            args = json.loads(tool_call.function.arguments)

            print(f"Tool call: {name}({args})", file=sys.stderr)
            result = execute_tool(name, args)

            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": result,
                }
            )


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "Read",
            "description": "Read and return the contents of a file",
            "parameters": {
                "type": "object",
                "properties": {
                    "file_path": {
                        "type": "string",
                        "description": "The path to the file to read",
                    }
                },
                "required": ["file_path"],
            },
        },
    }
]


def _read(file_path):
    with open(file_path, "r") as f:
        return f.read()


TOOL_HANDLERS = {
    "Read": lambda args: _read(args["file_path"]),
}


def execute_tool(name, args):
    handler = TOOL_HANDLERS.get(name)
    if handler:
        return handler(args)
    return f"Unknown tool: {name}"


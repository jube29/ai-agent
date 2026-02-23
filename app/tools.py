import subprocess

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
    },
    {
        "type": "function",
        "function": {
            "name": "Write",
            "description": "Write content to a file",
            "parameters": {
                "type": "object",
                "required": ["file_path", "content"],
                "properties": {
                    "file_path": {
                        "type": "string",
                        "description": "The path of the file to write to",
                    },
                    "content": {
                        "type": "string",
                        "description": "The content to write to the file",
                    },
                },
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "Bash",
            "description": "Execute a shell command",
            "parameters": {
                "type": "object",
                "required": ["command"],
                "properties": {
                    "command": {
                        "type": "string",
                        "description": "The command to execute",
                    }
                },
            },
        },
    },
]


def _read(file_path):
    with open(file_path, "r") as f:
        return f.read()


def _write(file_path, content):
    with open(file_path, "w") as f:
        f.write(content)
    return f"Written to {file_path}"


def _bash(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    output = result.stdout
    if result.stderr:
        output += result.stderr
    return output


TOOL_HANDLERS = {
    "Read": lambda args: _read(args["file_path"]),
    "Write": lambda args: _write(args["file_path"], args["content"]),
    "Bash": lambda args: _bash(args["command"]),
}


def execute_tool(name, args):
    handler = TOOL_HANDLERS.get(name)
    if handler:
        return handler(args)
    return f"Unknown tool: {name}"


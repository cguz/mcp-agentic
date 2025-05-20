from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
import json
import asyncio

client = MultiServerMCPClient(
    {
        "knowledge_retrieval": {
            "command": "python",
            # Replace with absolute path to your math_server.py file
            "args": ["./server/server_knowledge_retrieval.py"],
            "transport": "stdio",
        },
        "draft_procedures": {
            # Ensure your start your weather server on port 8000
            "url": "http://localhost:8000/mcp",
            "transport": "streamable_http",
        }
    }
)

async def main():
    tools = await client.get_tools()

    # Convert StructuredTool objects to JSON-friendly dictionaries
    tools_json_friendly = []
    for tool in tools:
        tool_dict = {
            "name": tool.name,
            "description": tool.description,
            "parameters": tool.args_schema, # For StructuredTool, the schema is in args_schema
        }
        tools_json_friendly.append(tool_dict)

    # Print as human-readable JSON
    print(json.dumps(tools_json_friendly, indent=4))

    # You can add more async code here

asyncio.run(main())
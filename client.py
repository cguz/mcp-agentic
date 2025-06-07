from langchain_mcp_adapters.client import MultiServerMCPClient
from server.server_knowledge_retrieval import MCP_SERVER_KNOWLEDGE_RETRIEVAL
from server.server_draft_procedure import MCP_TOOL_DRAFT_PROCEDURE
from langgraph.prebuilt import create_react_agent
import json
import asyncio

client = MultiServerMCPClient(
    {
        "knowledge_retrieval": MCP_SERVER_KNOWLEDGE_RETRIEVAL,
        "draft_procedures": MCP_TOOL_DRAFT_PROCEDURE,  
    }
)

def print_friendly(tools):
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

async def main():
    tools = await client.get_tools()

    print_friendly(tools)

    

asyncio.run(main())
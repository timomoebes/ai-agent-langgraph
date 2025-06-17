from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

model = ChatOpenAI(
    model_name="gpt-4o-mini", 
    temperature=0,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

server_params = StdioServerParameters(
    command="npx",
    env={
        "FIRECRAWL_API_KEY": os.getenv("FIRECRAWL_API_KEY"),
        "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY"),
        "OPENAI_MODEL_NAME": "gpt-4o-mini",
        },
        args=["firecrawl-mcp"]
)

async def main():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            
            await session.initialize()
            # Load all tools first
            all_tools = await load_mcp_tools(session)
            
            # Filter to only keep the essential tools we need
            essential_tools = [
                tool for tool in all_tools 
                if tool.name in ["firecrawl_search", "firecrawl_scrape"]
            ]
            
            agent = create_react_agent(model, essential_tools)

            messages = [
                {
                    "role": "system", 
                    "content": "You are a helpful assistant that can scrape websites and extract information."
                }
            ]
            
            print("Available tools -", *[tool.name for tool in essential_tools])
            print("-" * 60)

            while True:
                user_input = input("\nYou: ")
                if user_input == "quit":
                    print("\nGoodbye!")
                    break

                messages.append({"role": "user", "content": user_input[:175000]})
                
                try:
                    agent_response = await agent.ainvoke({"messages": messages})

                    ai_message = agent_response["messages"][-1].content
                    print("\nAgent: ", ai_message)
                except Exception as e:
                    print("\nError: ", e)
                
if __name__ == "__main__":
    asyncio.run(main())
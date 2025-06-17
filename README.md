# AI Web Scraping Assistant with LangGraph & Firecrawl

An interactive AI agent that can scrape and extract information from websites using LangGraph, OpenAI, and Firecrawl. The agent provides a command-line interface for natural language interaction with web content.

## Features

- Interactive command-line interface for natural language queries
- Web scraping capabilities powered by Firecrawl
- Utilizes OpenAI's GPT-4o-mini model for intelligent responses
- Built with LangGraph for agent orchestration
- Environment variable based configuration

## Project Structure

```
ai-agent-langgraph/
├── simple-agent/
│   ├── main.py          # Main application code
│   ├── pyproject.toml   # Project dependencies
│   ├── README.md        # Project-specific documentation
│   └── .env.example     # Example environment variables
└── README.md            # Main project documentation
```

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- OpenAI API key
- Firecrawl API key (optional, for web scraping functionality)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/timomoebes/ai-agent-langgraph.git
   cd ai-agent-langgraph/simple-agent
   ```

2. Set up a virtual environment (recommended):
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On macOS/Linux:
   # source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -e .
   ```

4. Configure environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```
   Required environment variables:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   # Optional:
   FIRECRAWL_API_KEY=your_firecrawl_api_key_here
   ```

### Usage

Run the agent:
```bash
python main.py
```

Interact with the agent in the command line. Type your questions or commands, and the agent will respond. Type 'quit' to exit.

Example commands:
- "What's the latest news on AI?"
- "Scrape the Wikipedia page for Python and summarize it"
- "Find information about machine learning trends in 2023"

## 🔧 Configuration

The agent can be configured using the following environment variables:

- `OPENAI_API_KEY`: Your OpenAI API key (required)
- `FIRECRAWL_API_KEY`: Your Firecrawl API key (required for web scraping)
- `OPENAI_MODEL_NAME`: The OpenAI model to use (default: "gpt-4o-mini")

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [LangGraph](https://langchain-ai.github.io/langgraph/)
- [OpenAI](https://openai.com/)
- [Firecrawl](https://firecrawl.dev/)

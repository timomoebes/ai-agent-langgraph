# Simple AI Agent

This is a simple AI agent implementation that uses LangGraph for orchestration, OpenAI's language models for natural language understanding, and Firecrawl for web scraping capabilities.

## 🛠️ Features

- **Interactive CLI**: Chat with the agent directly from your terminal
- **Web Scraping**: Extract and process information from websites
- **LangGraph Integration**: Uses LangGraph for agent orchestration and tool management
- **OpenAI Integration**: Leverages GPT-4o-mini for natural language understanding
- **Environment-Based Configuration**: Easy setup with environment variables

## 🚀 Quick Start

1. **Clone the repository**:
   ```bash
   git clone https://github.com/timomoebes/ai-research-agent-langgraph.git
   cd ai-research-agent-langgraph/simple-agent
   ```

2. **Install dependencies**:
   ```bash
   pip install -e .
   ```

3. **Set up environment variables**:
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

4. **Run the agent**:
   ```bash
   python main.py
   ```

## 🛠️ Available Tools

The agent has access to the following tools:

- **Web Scraping**: Extract content from websites
- **Information Retrieval**: Process and summarize web content
- **General Knowledge**: Answer questions using the underlying language model

## 🧩 Architecture

The agent is built using:

- **LangGraph**: For agent orchestration and tool management
- **OpenAI API**: For natural language understanding and generation
- **Firecrawl**: For web scraping capabilities
- **Python-dotenv**: For environment variable management

## 🔄 Development

### Prerequisites

- Python 3.10+
- pip (Python package manager)
- OpenAI API key
- Firecrawl API key (for web scraping)

### Installing Dependencies

```bash
pip install -e .
```

### Environment Variables

Create a `.env` file in the project root with the following variables:

```
OPENAI_API_KEY=your_openai_api_key_here
FIRECRAWL_API_KEY=your_firecrawl_api_key_here
```

## 📝 Usage Examples

1. **Basic Interaction**:
   ```
   You: What can you do?
   Agent: I can help you with web scraping, information retrieval, and answering questions...
   ```

2. **Web Scraping**:
   ```
   You: Scrape the Wikipedia page for Python and summarize it
   Agent: [Scrapes the page and provides a summary]
   ```

3. **Information Lookup**:
   ```
   You: What's the latest news on AI?
   Agent: [Searches and summarizes recent AI news]
   ```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

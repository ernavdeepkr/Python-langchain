# Python-LangChain

A comprehensive repository for learning and implementing LangChain projects in Python.

## What is LangChain?

LangChain is a framework for developing applications powered by language models. It enables developers to build sophisticated applications that can:

- **Chain multiple LLM calls together** - Combine multiple language model operations in a sequence
- **Interact with external data sources** - Integrate with databases, APIs, and knowledge bases
- **Create intelligent agents** - Build autonomous systems that can reason and take actions
- **Memory management** - Maintain context across conversations and interactions
- **Vector databases integration** - Work with embeddings for semantic search and retrieval

## Key Features

- **LLM Integration**: Easy integration with various language models (OpenAI, Hugging Face, etc.)
- **Chains**: Combine multiple components into a single, coherent workflow
- **Agents**: Create intelligent agents that can use tools and make decisions
- **Memory**: Built-in memory systems for maintaining conversation history
- **Document Processing**: Load, split, and process documents efficiently
- **Retrieval Augmented Generation (RAG)**: Combine language models with external knowledge sources
- **Prompt Management**: Templates and optimization for prompts

## Installation

```bash
pip install langchain langchain-openai
```

## Getting Started

To get started with LangChain, you'll need:

1. **Python 3.8+**
2. **An API key** for your chosen LLM provider (e.g., OpenAI)
3. **LangChain library** installed via pip

## Running the Demo

### `langchain_basics.py`

A simple program that demonstrates core LangChain concepts:
- Initializing a ChatOpenAI model
- Creating a prompt template with variables
- Building a chain (`prompt | llm | output parser`)
- Running the chain and printing the result

**Steps to run:**

1. Install dependencies:
   ```bash
   pip install langchain langchain-openai
   ```

2. Set your OpenAI API key:
   ```bash
   # Windows
   set OPENAI_API_KEY=your-api-key-here

   # Linux/Mac
   export OPENAI_API_KEY=your-api-key-here
   ```

3. Run the program:
   ```bash
   python langchain_basics.py
   ```

## Project Structure

This repository contains simple LangChain projects demonstrating:

- Basic LLM interactions
- Creating chains
- Building agents
- Working with memory
- Document processing
- And more

## Documentation

- [LangChain Official Documentation](https://python.langchain.com/)
- [LangChain GitHub Repository](https://github.com/langchain-ai/langchain)

## Contributing

Feel free to contribute improvements, bug fixes, or new project examples!

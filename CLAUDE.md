# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Rules

**IMPORTANT**: The following rules must be followed when working in this repository:

1. **Language**: All responses and communication must be in Japanese (日本語)
2. **Documentation Lookup**: When retrieving information about libraries, frameworks, or tools, you MUST use the Context7 MCP tools (`mcp__context7__resolve-library-id` and `mcp__context7__get-library-docs`) to ensure up-to-date and accurate documentation

## Repository Overview

This is a seminar/tutorial repository focused on intermediate generative AI topics, specifically:
- **MCP (Model Context Protocol) basics** - Located in `mcp-basics/`
- **Dify basics** - Located in `dify-basics/`

The repository is structured as educational content with sections organized sequentially (e.g., `section-01-introduction`).

## Project Configuration

- **Python Version**: 3.13 (specified in `.python-version`)
- **Project Manager**: uv (based on `pyproject.toml` structure)
- **Package Name**: `generative-ai-intermediate`
- **Python Requirement**: >=3.10

## Repository Structure

```
generative-ai-intermediate/
├── mcp-basics/           # Model Context Protocol tutorials
│   └── section-*/        # Sequential tutorial sections
└── dify-basics/          # Dify platform tutorials
    └── section-*/        # Sequential tutorial sections
```

## Development Setup

Since this project uses uv for Python package management:

```bash
# Install dependencies (when they exist)
uv pip install -e .

# Or sync dependencies
uv sync
```

## Content Organization

- Each topic area (`mcp-basics`, `dify-basics`) contains its own README.md
- Tutorial sections are numbered sequentially: `section-01-introduction`, `section-02-*`, etc.
- Each section has its own README.md with content
- README files are the primary content delivery mechanism

## Working with Tutorial Content

When creating or editing tutorial sections:
- Maintain the `section-##-description` naming pattern
- Each section should have a descriptive README.md
- Keep content focused and progressive (each section builds on previous ones)
- Consider both MCP and Dify content may be developed in parallel

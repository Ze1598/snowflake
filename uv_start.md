# Initialize new project with pyproject.toml
uv init

# Add dependencies (creates/updates pyproject.toml and uv.lock)
uv add pandas snowflake-connector-python streamlit snowflake-snowpark-python snowflake.core

# Sync environment (install everything from lock file)
uv sync

# Run scripts with uv (no venv activation needed)
uv run streamlit run main.py

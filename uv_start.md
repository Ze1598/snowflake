# Initialize new project with pyproject.toml
uv init

# Add dependencies (creates/updates pyproject.toml and uv.lock)
uv add llvmlite;
uv add numba;
uv add snowflake-ml-python;
uv add pandas streamlit snowflake-snowpark-python;

# Sync environment (install everything from lock file)
uv sync

# Run scripts with uv (no venv activation needed)
uv run streamlit run main.py

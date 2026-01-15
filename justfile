# Copy secrets file
setup-secrets DAY_NUMBER:
    mkdir day{{DAY_NUMBER}}/.streamlit
    cp day1/.streamlit/secrets.toml day{{DAY_NUMBER}}/.streamlit

# Create python env
setup-env DAY_NUMBER:
    #!/usr/bin/env bash
    set -euo pipefail
    cd day{{DAY_NUMBER}}
    uv init
    uv add llvmlite
    uv add numba
    uv add snowflake-ml-python
    uv add pandas streamlit snowflake-snowpark-python
    uv sync

# Orchestrate local env creation
create-new DAY_NUMBER:
    mkdir day{{DAY_NUMBER}}
    just setup-secrets {{DAY_NUMBER}}
    just setup-env {{DAY_NUMBER}}

# Run the app
run DAY_NUMBER:
    #!/usr/bin/env bash
    set -euo pipefail
    cd day{{DAY_NUMBER}}
    uv run streamlit run main.py
import streamlit as st

st.title(":material/vpn_key: Day 1: Connect to Snowflake")

# Connect to Snowflake
try:
    # Works in Streamlit in Snowflake
    from snowflake.snowpark.context import get_active_session
    session = get_active_session()
except:
    from snowflake.snowpark import Session

    session = Session.builder.configs({
        # Owner account
        "account": st.secrets["snowflake"]["account"],
        # Service user name
        "user": st.secrets["snowflake"]["user"],
        # PAT
        "password": st.secrets["snowflake"]["token"],
        # Target warehouse
        "warehouse": st.secrets["snowflake"]["warehouse"],
        # Target database
        "database": st.secrets["snowflake"]["database"],
        # Target schema
        "schema": st.secrets["snowflake"]["schema"]
    }).create()

# Query Snowflake version
version = session.sql("SELECT CURRENT_VERSION()").collect()[0][0]

# Display results
st.success(f"Successfully connected! Snowflake Version: {version}")
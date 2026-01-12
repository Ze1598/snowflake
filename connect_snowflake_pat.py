import streamlit as st
# snowflake-snowpark-python
from snowflake.snowpark import Session

# Read from .streamlit secrets file
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
st.success(f"Successfully connected! Snowflake Version: {version}")
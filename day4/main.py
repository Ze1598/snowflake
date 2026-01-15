import streamlit as st
import time
import json
from snowflake.snowpark.functions import ai_complete

st.title(":material/cached: Caching your App")
# Connect to Snowflake
try:
    # Works in Streamlit in Snowflake
    from snowflake.snowpark.context import get_active_session
    session = get_active_session()
except:
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

@st.cache_data
def call_cortex_llm(prompt_text):
    model = "claude-3-5-sonnet"
    df = session.range(1).select(
        ai_complete(model=model, prompt=prompt_text).alias("response")
    )
    
    # Get and parse response
    response_raw = df.collect()[0][0]
    response_json = json.loads(response_raw)
    return response_json

prompt = st.text_input("Enter your prompt", "Why is the sky blue?")

if st.button("Submit"):
    start_time = time.time()
    response = call_cortex_llm(prompt)
    end_time = time.time()
    
    st.success(f"*Call took {end_time - start_time:.2f} seconds*")
    st.write(response)

# Footer
st.divider()
st.caption("Day 4: Caching your App | 30 Days of AI")
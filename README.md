1. Create a folder named `.streamlit`then inside the folder create a `secerts.toml` file and add the the required key inside
    ```toml
    openai_api_key="add key here"
    anthropic_api_key="add key here"
    ```
2. after that run pip to install the requirements as follows:
    ````bash
    pip install -r requirements.txt
    ````

3. now you can start the app using streamlit 
    ```bash
    streamlit run app.py
    ```

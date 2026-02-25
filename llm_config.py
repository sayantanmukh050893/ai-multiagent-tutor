from langchain_community.llms import HuggingFaceHub

llm = HuggingFaceHub(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    model_kwargs={"temperature": 0.5, "max_new_tokens": 2048}
)

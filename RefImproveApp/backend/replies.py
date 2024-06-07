# This file will call a reply function to send a reply to the user
from transformers import pipeline
from llama_cpp import Llama
from huggingface_hub import hf_hub_download

"""This will send a reply back to the user"""
def reply(comment):
    pipe = pipeline("text2text-generation", model="ilsilfverskiold/tech-keywords-extractor")

    query = f"Using the words in this list {pipe} create a response that is politely thanking the user for informing about the referee"

    prompt = "You will respond as a politely like a customer service rep"

    model_path = hf_hub_download("TheBloke/Llama-2-7B-Chat-GGUF", filename="llama-2-7b-chat.Q4_K_M.gguf")

    llm = Llama(model_path=model_path)

    output = llm(f"User:{query}\n"
                 f"Assistant: {prompt}.",max_tokens=200)
    
    return output["choices"][0]["text"]

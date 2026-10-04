from langchain_aws import ChatBedrockConverse


def build_chat_model(provider: str, model_id: str, region_name: str = "us-east-1"):
    """Crea el chat model utilizado por chains, RAG y agents de M06."""
    if provider != "bedrock":
        raise ValueError(f"MODEL_PROVIDER no soportado en M06: {provider}")

    return ChatBedrockConverse(
        model=model_id,
        region_name=region_name,
        temperature=0,
    )

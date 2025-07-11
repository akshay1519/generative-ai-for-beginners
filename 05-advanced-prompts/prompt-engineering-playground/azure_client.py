import os
from openai import AzureOpenAI
from dotenv import load_dotenv


def get_azure_openai_client():
    """
    Initialize and return Azure OpenAI client with error handling.
    Returns tuple of (client, deployment_name)
    """
    # Load environment variables
    load_dotenv()
    
    try:
        client = AzureOpenAI(
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
        )
        deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")
        
        # Test the connection with a simple request
        test_response = client.chat.completions.create(
            model=deployment,
            messages=[{"role": "user", "content": "Hello"}],
            max_tokens=10
        )
        print("Connection successful. Test response:", test_response.choices[0].message.content)
        
        return client, deployment
        
    except Exception as e:
        print(f"Error connecting to Azure OpenAI: {e}")
        raise


def create_chat_completion(client, deployment, messages, temperature=0.7, max_tokens=None):
    """
    Helper function to create chat completions with consistent parameters.
    """
    kwargs = {
        "model": deployment,
        "messages": messages,
        "temperature": temperature
    }
    
    if max_tokens:
        kwargs["max_tokens"] = max_tokens
        
    return client.chat.completions.create(**kwargs)
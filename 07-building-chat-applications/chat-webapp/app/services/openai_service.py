import logging
from typing import List, Dict, Optional
from openai import AzureOpenAI
from azure.identity import  DefaultAzureCredential, ManagedIdentityCredential,get_bearer_token_provider
from app.config import settings

logger = logging.getLogger(__name__)

class ChatService:
    """Service for handling chat operations with Azure OpenAI with azure authentication."""

    def __init__(self):
        self.client = self._initialize_client()
        self.deployment = settings.azure_openai_deployment

    def _initialize_client(self) -> AzureOpenAI:
        """Initialize the Azure OpenAI client with appropriate credentials."""
        try:
            if settings.environment == 'local':
                # Use DefaultAzureCredential for local development
                credential = DefaultAzureCredential()
                logger.info("Using DefaultAzureCredential for local development")
            else:
                # Use ManagedIdentityCredential for Azure App Service
                if settings.managed_identity_client_id:
                    credential = ManagedIdentityCredential(client_id=settings.managed_identity_client_id)
                    logger.info(f"Using ManagedIdentityCredential with client ID")
                else:
                    credential = ManagedIdentityCredential()
                    logger.info("Using ManagedIdentityCredential without client ID")
            
            token_provider = get_bearer_token_provider(
                credential,
                "https://cognitiveservices.azure.com/.default"
            )

            print("=== Azure OpenAI Client Initialization ===")
            client = AzureOpenAI(
                azure_endpoint=settings.azure_openai_endpoint,
                azure_ad_token_provider=token_provider,
                api_version=settings.azure_openai_api_version
            )
            
            logger.info("Azure OpenAI client initialized successfully")
            return client
        
        except Exception as e:
            logger.error("Failed to initialize Azure OpenAI client: %s", e)
            raise

    def get_chat_response(
        self, 
        messages: List[Dict[str, str]], 
        temperature: float = 0.7,
        max_tokens: int = 1000
    ) -> str:
        """Get chat response from Azure OpenAI."""
        try:
            response = self.client.chat.completions.create(
                model=self.deployment,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens
            )
            return response.choices[0].message.content.strip()
        
        except Exception as e:
            logger.error("Error getting chat response: %s", e)
            raise
    
    def create_system_message(self) -> dict:
        """Create a system message for the chat."""
        return {
            "role": "system",
            "content": """You are a helpful technical assistant specializing in:
            - Cloud computing (Azure, AWS, GCP)
            - Software development and debugging
            - System administration and DevOps
            - Database management
            - Network troubleshooting
            
            Provide clear, concise, and accurate technical guidance.
            Include code examples when relevant.
            Always consider security best practices."""
        }

#create singleton instance of ChatService
chat_service = ChatService()
logger.info("ChatService initialized with deployment: %s", settings.azure_openai_deployment)
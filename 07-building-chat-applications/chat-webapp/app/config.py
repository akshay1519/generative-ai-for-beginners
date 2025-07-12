import os
from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from azure.identity import DefaultAzureCredential,ManagedIdentityCredential

class Settings(BaseSettings):
    """ Application settings for the chat web application. """

    app_name: str = Field(default="Chat Web App", description="Name of the application")
    environment: str = Field(default="production", alias="ENVIRONMENT")
    debug: bool = Field(default=False, alias="DEBUG")

    # Azure OpenAI settings
    azure_openai_endpoint: str = Field(..., alias="AZURE_OPENAI_ENDPOINT")
    azure_openai_deployment: str = Field(..., alias="AZURE_OPENAI_DEPLOYMENT")
    azure_openai_api_version: str = Field(..., alias="AZURE_OPENAI_API_VERSION")

    # Azure authentication settings
    use_managed_identity: bool = Field(default=True, alias="USE_MANAGED_IDENTITY")
    managed_identity_client_id: Optional[str] = Field(None, alias="MANAGED_IDENTITY_CLIENT_ID")

    # Flask settings
    secret_key: str = Field(..., alias="FLASK_SECRET_KEY", description="Secret key for Flask sessions")

    #logging settings
    log_level: str = Field(default="INFO", alias="LOG_LEVEL")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore"  # Ignore any extra fields not defined in the model
    )

    def get_azure_credentials(self):
        """Get Azure credential based on environment"""
        if self.use_managed_identity:
            if self.environment == "local":
                # Use DefaultAzureCredential for local development
                # This will try multiple authentication methods including Azure CLI
                return DefaultAzureCredential()
            else:
                # Use ManagedIdentityCredential for Azure App Service
                if self.managed_identity_client_id:
                    return ManagedIdentityCredential(client_id=self.managed_identity_client_id)
                else:
                    return ManagedIdentityCredential()
        else:
            # Fallback to DefaultAzureCredential
            return DefaultAzureCredential()

# Create a global settings instance
settings = Settings()
from google.genai.types import GenerateContentConfig, HttpOptions, HttpRetryOptions

GENERATE_CONTENT_CONFIG = GenerateContentConfig(
    http_options=HttpOptions(
        timeout=120000, # 120 seconds in milliseconds
        retry_options=HttpRetryOptions(
            attempts=3, # 3 retries
        )
    )
)

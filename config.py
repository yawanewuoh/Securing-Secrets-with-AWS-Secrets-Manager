# config.py - TEMPORARY for demonstration only
# WARNING: This is NOT safe for production! We'll fix it with Secrets Manager.

import botocore
import json  
import botocore.session  
from aws_secretsmanager_caching import SecretCache, SecretCacheConfig

def get_secret():

    client = botocore.session.get_session().create_client('secretsmanager')
    cache_config = SecretCacheConfig()
    cache = SecretCache(config=cache_config, client=client)

    secret = cache.get_secret_string('aws-access-key')
    return json.loads(secret)

# Retrieve credentials from Secrets Manager
credentials = get_secret()

# Extract the values; if AWS_REGION isn't in the secret, use the region from the session
AWS_ACCESS_KEY_ID = credentials.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = credentials.get("AWS_SECRET_ACCESS_KEY")
AWS_REGION = credentials.get("AWS_REGION", boto3.session.Session().region_name or "us-east-2")




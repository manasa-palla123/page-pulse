from cachetools import TTLCache

# Maximum 1000 cached URLs
# Cache expires after 600 seconds (10 minutes)

cache = TTLCache(
    maxsize=1000,
    ttl=600
)
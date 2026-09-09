import time
import functools
import random
from typing import Callable, Any

def retry_with_exponential_backoff(max_attempts: int = 5, base_delay: float = 1.0):
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            while attempt < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempt += 1
                    if attempt == max_attempts:
                        raise e
                    sleep_time = (base_delay * (2 ** attempt)) + (random.random() * 0.1)
                    time.sleep(sleep_time)
        return wrapper
    return decorator

class NetworkProcessor:
    @retry_with_exponential_backoff(max_attempts=3, base_delay=0.5)
    def fetch_node_status(self, endpoint: str):
        # Simulate unstable crypto node connection
        if random.random() < 0.7:
            raise ConnectionError(f"Node {endpoint} unreachable")
        return {"status": "synced", "block": 1234567}

if __name__ == '__main__':
    processor = NetworkProcessor()
    try:
        print(processor.fetch_node_status("mainnet.infura.io"))
    except Exception as err:
        print(f"Final failure after retries: {err}")
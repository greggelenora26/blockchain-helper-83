import time
import functools
import random

class NetworkException(Exception):
    pass

def exponential_retry(max_attempts=3, base_delay=1.0, jitter=True):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts >= max_attempts:
                        raise NetworkException(f"failed after {max_attempts} attempts: {e}")
                    
                    delay = base_delay * (2 ** (attempts - 1))
                    if jitter:
                        delay *= (0.5 + random.random())
                    
                    time.sleep(delay)
        return wrapper
    return decorator

@exponential_retry(max_attempts=4)
def broadcast_transaction(tx_data):
    # Simulate volatile network state
    if random.random() < 0.7:
        raise ConnectionError("node unreachable")
    return "success"
import time
import functools
import random
import logging

logger = logging.getLogger('blockchain-helper-83')

def backoff_retry(max_attempts=3, base_delay=1.0, jitter=True):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    attempts += 1
                    if attempts >= max_attempts:
                        logger.error(f'failed after {attempts} attempts')
                        raise e
                    
                    sleep_time = base_delay * (2 ** (attempts - 1))
                    if jitter:
                        sleep_time *= (0.5 + random.random())
                    
                    logger.warning(f'retry {attempts}/{max_attempts} in {sleep_time:.2f}s')
                    time.sleep(sleep_time)
        return wrapper
    return decorator

@backoff_retry(max_attempts=5)
def broadcast_transaction(tx_data):
    # Simulate network instability in crypto node
    if random.random() < 0.7:
        raise ConnectionError('node sync mismatch')
    return 'success'
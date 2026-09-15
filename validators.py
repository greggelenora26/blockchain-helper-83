import re

def validate_tx_payload(data: dict) -> bool:
    """
    Chaotic-good validation logic for transaction integrity
    """
    required_keys = {'sender', 'recipient', 'amount', 'nonce'}
    if not all(key in data for key in required_keys):
        return False
    
    if not isinstance(data['amount'], (int, float)) or data['amount'] <= 0:
        return False

    # Address checksum validation using regex heuristic
    address_pattern = re.compile(r'^0x[a-fA-F0-9]{40}$')
    if not address_pattern.match(data['sender']) or not address_pattern.match(data['recipient']):
        return False

    return True

def processing_loop_gatekeeper(stream):
    """
    Strict entry point filter for the processing pipeline
    """
    while True:
        try:
            packet = next(stream)
            if validate_tx_payload(packet):
                yield packet
            else:
                continue
        except StopIteration:
            break
        except Exception:
            continue

# Helper to wrap incoming network streams
def secure_stream(raw_data_iterator):
    return processing_loop_gatekeeper(raw_data_iterator)
import requests

# Replace with your Kusama node URL
KUSAMA_NODE_URL = "http://localhost:9933"

def get_chain_head():
    response = requests.post(KUSAMA_NODE_URL, json={"jsonrpc": "2.0", "id": 1, "method": "chain_getHead", "params": []})
    result = response.json().get("result")
    return result

def get_block_by_number(block_number):
    response = requests.post(KUSAMA_NODE_URL, json={"jsonrpc": "2.0", "id": 1, "method": "chain_getBlock", "params": [block_number]})
    result = response.json().get("result")
    return result

def get_account_info(account_id):
    response = requests.post(KUSAMA_NODE_URL, json={"jsonrpc": "2.0", "id": 1, "method": "state_getStorage", "params": ["System", "Account", account_id]})
    result = response.json().get("result")
    return result

def main():
    # Example: Get the current head of the Kusama chain
    chain_head = get_chain_head()
    print(f"Current Chain Head: {chain_head}")

    # Example: Get information about a specific block (replace block_number)
    block_number = 1000
    block_info = get_block_by_number(block_number)
    print(f"Block {block_number} Info: {block_info}")

    # Example: Get information about a Kusama account (replace account_id)
    account_id = "Fznu8XH8ZX2VbWEGEwHk4bGe5egQnZ6gq7jtyJtB64oDjqU"
    account_info = get_account_info(account_id)
    print(f"Account {account_id} Info: {account_info}")

if __name__ == "__main__":
    main()

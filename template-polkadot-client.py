from substrateinterface import SubstrateInterface, Keypair

# Connect to the local Polkadot node
substrate = SubstrateInterface(url="http://localhost:9933")

# Replace with your account seed or address
account_seed = "your_account_seed_or_address"
keypair = Keypair.create_from_uri(account_seed)

# Query the account balance
account_info = substrate.get_account_info(keypair.ss58_address)
balance = account_info["data"]["free"]

print(f"Account Balance: {balance} DOT")

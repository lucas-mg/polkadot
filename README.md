
# Polkadot Template

This is a template with the basics to create a polkadot node inside GCP using terraform and a simple pyhton client to interact with the node.



```bash
terraform init
terraform apply
```
## Polkadot Node Setup
Inside the instance, install Polkadot:
```bash
sudo apt-get update
sudo apt-get install -y software-properties-common
sudo add-apt-repository -y ppa:ethereum/ethereum
sudo apt-get update
sudo apt-get install -y polkadot
```

Start the Polkadot node:
```bash
sudo systemctl start polkadot
```

## Python Polkadot Client

Install the substrate-interface Python library:
```bash
pip install substrate-interface
```

Then run the python script:

```bash
python polkadot_client.py
```




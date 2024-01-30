provider "google" {
  credentials = file("<path-to-your-service-account-key.json>")
  project     = "<your-gcp-project>"
  region      = "us-central1"  # Change to your desired GCP region
}

resource "google_compute_instance" "polkadot_node" {
  name         = "polkadot-node"
  machine_type = "e2-medium"  # Change to your desired machine type
  zone         = "us-central1-a"  # Change to your desired GCP zone

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-10"
    }
  }

  network_interface {
    network = "default"
  }

  tags = ["polkadot-node"]
}

output "instance_ip" {
  value = google_compute_instance.polkadot_node.network_interface.0.access_config.0.assigned_nat_ip
}

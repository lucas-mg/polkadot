# Configure the Google Cloud provider
provider "google" {
  credentials = file("<PATH_TO_YOUR_GCP_SERVICE_ACCOUNT_KEY>")
  project     = "<YOUR_GCP_PROJECT_ID>"
  region      = "us-central1"
}

# Define variables
variable "instance_name" {
  default = "kusama-node-instance"
}

variable "machine_type" {
  default = "n1-standard-2"
}

variable "image_family" {
  default = "ubuntu-2004-lts"
}

# Create a VM instance
resource "google_compute_instance" "kusama_node_instance" {
  name         = var.instance_name
  machine_type = var.machine_type

  boot_disk {
    initialize_params {
      image_family = var.image_family
    }
  }

  network_interface {
    network = "default"
  }

  metadata_startup_script = <<-EOF
    #!/bin/bash
    sudo apt-get update -y
    sudo apt-get install -y unzip curl
    curl -s https://getsubstrate.io -sSf | bash -s -- --fast
    EOF
}

# Output the external IP address of the VM
output "external_ip" {
  value = google_compute_instance.kusama_node_instance.network_interface.0.access_config.0.assigned_nat_ip
}

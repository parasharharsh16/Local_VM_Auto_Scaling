# Local_VM_Auto_Scaling# GCP Auto-Scaling with CPU Monitoring

This project implements an automatic scaling mechanism that monitors CPU usage and scales up a Google Cloud Platform (GCP) instance group when the CPU utilization exceeds a specified threshold. It uses Python, `psutil` for CPU monitoring, and the Google Cloud Compute API for scaling operations.

## Prerequisites

Before running this project, ensure the following prerequisites are met:

1. **Python 3.9+**: Make sure Python is installed on your system.
2. **Google Cloud SDK**: Install the Google Cloud SDK and authenticate using `gcloud auth login`.
3. **Google Cloud Compute API**: Ensure the **Compute Engine API** is enabled in your GCP project.
4. **GCP Credentials**: Set up Application Default Credentials by running:
    ```bash
    gcloud auth application-default login
    ```
5. **Instance Group**: You should have a managed instance group set up in your GCP project.

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/parasharharsh16/Local_VM_Auto_Scaling.git
    cd Local_VM_Auto_Scaling
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

Create a `config.json` file in the project directory with the following format:

```json
{
    "PROJECT_ID": "gcp-project-id",
    "ZONE": "gcp-zone",
    "INSTANCE_GROUP_NAME": "instance-group-name",
    "INCREMENT_VM_COUNT": 1,
    "CPU_THRESHOLD": 75.0,
    "COOLDOWN_PERIOD": 60
}

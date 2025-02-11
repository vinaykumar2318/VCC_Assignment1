# Virtualisation and Cloud Computing Assignment 1

## Overview
Create and configure multiple VMs using VirtualBox, establish a network, and deploy a microservice-based application (data sender/receiver).

## Steps
1. **Install VirtualBox and Create VMs**:
   - Download VirtualBox and Ubuntu.
   - Create 2 VMs with 2GB RAM and 20GB VHD each.

2. **Configure Network**:
   - Set Adapter 1 to NAT and Adapter 2 to Host-Only.
   - Get receiver VM IP using `ip a`.

3. **Deploy Microservice**:
   - Sender VM (port 5001) sends data.
   - Receiver VM (port 5002) stores and retrieves data.

## API Endpoints
- **POST /send_data**: Send  data.
- **POST /receive_data**: Fetch data back.

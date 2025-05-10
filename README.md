# mc-server
Public minecraft server in local docker without any port forwarding and white IP's

To start the MC-Server project, you need to follow these steps:

## Prerequisites

1. Docker and Docker Compose installed on your system
2. ngrok account with an authentication token
3. Telegram bot token and chat ID

## Steps to Start the Project

1. **Clone the repository**:  
    First, clone the repository to your local machine.
    
2. **Set up environment variables**:  
    You need to set the following environment variables:
    
    - `NGROK_AUTHTOKEN`: Your ngrok authentication token
    - `TELEGRAM_BOT_TOKEN`: Your Telegram bot token
    - `TELEGRAM_CHAT_ID`: Your Telegram chat ID
    
    These environment variables are required for the ngrok tunnel and notification service to work properly.
    
3. **Start the services using Docker Compose**:  
    Run the following command in the project directory:
    
    ```
    docker-compose up -d
    ```
    
    This will start three services:
    
    - `mc`: The Minecraft server running on port 25565
    - `ngrok`: The tunnel service that makes your Minecraft server accessible from the internet
    - `notifier`: A service that sends the server connection details to your Telegram chat

4. **Wait for the notification**:  
    The notifier service will attempt to retrieve the tunnel URL from ngrok and send it to your Telegram chat.
    
5. **Connect to the server**:  
    Once you receive the notification in Telegram with the server address, you can use that address to connect to your Minecraft server.
    

## Configuration Options

The Minecraft server is configured with specific settings in the docker-compose.yml file:

- Minecraft version: 1.19.4
- Server type: PAPER
- Memory allocation: 1G initial, 4G maximum
- View distance: 6
- Simulation distance: 3
- Command blocks enabled
- Offline mode authentication

You can modify these settings in the docker-compose.yml file according to your preferences.

# Notes

The project uses Docker Compose to orchestrate three services: a Minecraft server, an ngrok tunnel for remote access, and a notification service that sends connection details via Telegram. The system is designed to make a Minecraft server accessible from anywhere without requiring port forwarding or a static IP address.
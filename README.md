
# chatRoom: A Real-Time chatting Application

chatRoom is a **real-time chat application** built with **Django**, **Channels**, and **WebSockets**. It allows users to send and receive messages in real-time, providing an interactive messaging experience. The project also includes user authentication (login/signup) and WebSocket handling for communication.

## Demo

Watch the demo video to see the **chatRoom Application** in action:

<div align="center">
    <a href="https://youtu.be/QaxZLYRwQWU">
        <img src="https://img.youtube.com/vi/QaxZLYRwQWU/0.jpg" alt="Watch the video" style="width:80%; max-width:600px;">
    </a>
</div>


## Features
- **Real-time Messaging**: Messages are sent and received instantly using WebSockets.
- **User Authentication**: Users can sign up and log in to use the chat application.
- **Responsive UI**: The chat interface is built with **Tailwind CSS** for a clean and responsive design.

## Requirements
To run this application locally, you need the following tools installed:
- **Python 3.x** (preferably 3.8+)
- **Django 5.x**
- **Channels** (Django Channels package for WebSockets)
- **Redis** (for the Channels layer)
  
## Installation Instructions

### Step 1: Clone the Repository

Clone this repository to your local machine:
```bash
git clone https://github.com/tarunkeshukumar/roomChat.git
```
Navigate into the project directory:
```bash
cd chat-project
```

### Step 2: Set Up a Virtual Environment

Create and activate a virtual environment:
```bash
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies

Install the required dependencies from `requirements.txt`:
```bash
pip install -r requirements.txt
```

### Step 4: Set Up Redis (For Channels Layer)

The application uses Redis as a channel layer for WebSocket communication. If you don't have Redis installed, you can follow the [Redis installation guide](https://redis.io/download).

After installation, make sure Redis is running:
```bash
# On macOS/Linux
redis-server

# On Windows (use Redis from the Windows Subsystem for Linux or Docker)
redis-server
```

### Step 5: Set Up Database

Run the following command to set up the database and apply migrations:
```bash
python manage.py migrate
```

### Step 6: Create a Superuser (Admin)

To access the Django admin panel and manage users, create a superuser:
```bash
python manage.py createsuperuser
```
Follow the prompts to create your superuser account.

### Step 7: Run the Development Server

Start the Django development server:
```bash
python manage.py runserver
```

Visit the application in your web browser:
```
http://127.0.0.1:8000/chat
```

## Usage

### Registering and Logging In
1. Navigate to the **Sign Up** page to create a new account.
2. After registration, log in with the username and password you just created.
3. Once logged in, you will be redirected to the chat window.
4. Start typing messages in the input field and hit **Enter** to send a message.

### Chat Functionality
- The chat application uses **WebSockets** to allow messages to be sent in real-time.
- Each user can chat with a recipient by navigating to the URL:
  ```
  http://127.0.0.1:8000/chat/chat/<recipient_username>/
  ```
- **Sender's messages** are styled with [recipient's username]: **recipient's messages**.

### Django Admin Panel
- You can log into the **admin panel** at:
  ```
  http://127.0.0.1:8000/admin/
  ```
- Use the superuser credentials you created earlier to manage users, view messages, etc.

## Project Structure

```
chat_project/
├── chat_app/
│   ├── __init__.py
│   ├── consumers.py             # WebSocket consumer for handling real-time messages
│   ├── models.py                # Models for user authentication and chatrooms
│   ├── routing.py               # Routing for WebSocket connections
│   ├── templates/
│   │   ├── chat_app/
│   │   │   ├── base.html        # Base HTML template for all pages
│   │   │   ├── chatroom.html    # Chatroom UI
│   │   │   ├── login.html       # Login page
│   │   │   └── register.html    # Registration page
│   └── views.py                 # Views for handling user login, registration
├── chat_project/
│   ├── __init__.py
│   ├── settings.py              # Django settings
│   ├── urls.py                  # URL routing for the project
│   └── asgi.py                  # ASGI configuration for Channels
├── manage.py                    # Django management command script
└── requirements.txt             # List of dependencies
```

## Troubleshooting

### WebSocket Connection Issues

- Ensure **Redis** is running. WebSocket connections rely on Redis for the channel layer.
- If you're getting WebSocket errors, check the browser's console for more information.


## Contributing

Feel free to fork the repository, make changes, and create a pull request. Ensure that your contributions adhere to the style of the existing code.

---

## Acknowledgements

- **Django**: For building the web framework.
- **Django Channels**: For enabling WebSocket support in Django.
- **Redis**: For handling real-time data and WebSocket connections.


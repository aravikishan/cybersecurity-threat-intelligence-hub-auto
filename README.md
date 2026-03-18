# Cybersecurity Threat Intelligence Hub Auto

## Overview
The Cybersecurity Threat Intelligence Hub Auto is a sophisticated web application that centralizes the management and analysis of cybersecurity threats and incidents. It is designed to provide cybersecurity professionals with a comprehensive platform for monitoring, reporting, and managing threat indicators and incident reports. The application offers a user-friendly interface and a robust backend, addressing the critical need for efficient threat intelligence management.

This platform is particularly beneficial for cybersecurity teams, analysts, and administrators who need a reliable system to track threats and incidents, manage user roles, and maintain a secure environment. With its intuitive dashboard and detailed reporting capabilities, users can quickly access and manage relevant data, enhancing their ability to respond to cybersecurity challenges effectively.

## Features
- **User Management**: An admin panel for managing user roles and profiles, ensuring secure access control.
- **Threat Indicators**: View and manage a comprehensive list of cybersecurity threat indicators, categorized by type and severity.
- **Incident Reporting**: Create, view, and manage detailed incident reports with statuses, enhancing incident response.
- **Dashboard**: A centralized dashboard providing an overview of the system's functionalities and quick access to key features.
- **Static File Serving**: Efficiently serves static files such as CSS for styling, ensuring a seamless user experience.
- **Data Seeding**: Automatically seeds initial data for users, threat indicators, and incident reports for quick setup.
- **RESTful API**: Provides endpoints for accessing and managing users, threat indicators, and incident reports, facilitating integration with other systems.

## Tech Stack
| Technology   | Description                               |
|--------------|-------------------------------------------|
| FastAPI      | Web framework for building APIs           |
| Uvicorn      | ASGI server for running FastAPI apps      |
| SQLAlchemy   | ORM for database interaction              |
| Pydantic     | Data validation and settings management   |
| SQLite       | Lightweight database for data storage     |
| Docker       | Containerization for deployment           |

## Architecture
The project is structured to separate concerns between the frontend and backend, with FastAPI serving as the backend API provider. The application serves static HTML files for the frontend, which interact with the backend via RESTful API endpoints. The database models are defined using SQLAlchemy, and data flows from the database to the frontend through API calls.

```plaintext
+-------------------+
|  Frontend (HTML)  |
+-------------------+
          |
          v
+-------------------+
|  FastAPI Backend  |
+-------------------+
          |
          v
+-------------------+
|     SQLite DB     |
+-------------------+
```

## Getting Started

### Prerequisites
- Python 3.11+
- pip (Python package installer)
- Docker (optional, for container deployment)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/cybersecurity-threat-intelligence-hub-auto.git
   cd cybersecurity-threat-intelligence-hub-auto
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application
1. Start the FastAPI application using Uvicorn:
   ```bash
   uvicorn app:app --reload
   ```
2. Visit the application at `http://127.0.0.1:8000`

## API Endpoints
| Method | Path                       | Description                                  |
|--------|----------------------------|----------------------------------------------|
| GET    | `/`                        | Displays the main dashboard                  |
| GET    | `/threats`                 | Displays the list of threat indicators       |
| GET    | `/incidents`               | Displays the list of incident reports        |
| GET    | `/profile`                 | Displays the user profile page               |
| GET    | `/admin`                   | Displays the admin panel                     |
| GET    | `/api/threat-indicators`   | Retrieves all threat indicators              |
| POST   | `/api/incidents`           | Creates a new incident report                |
| GET    | `/api/incidents`           | Retrieves all incident reports               |
| GET    | `/api/users`               | Retrieves all users                          |
| PUT    | `/api/users/{user_id}`     | Updates a user's information                 |

## Project Structure
```
.
├── Dockerfile                 # Docker configuration file
├── app.py                     # Main application file
├── requirements.txt           # Python dependencies
├── start.sh                   # Script to start the application
├── static
│   └── css
│       └── bootstrap.min.css  # Bootstrap CSS for styling
├── templates
│   ├── admin.html             # Admin panel HTML template
│   ├── incidents.html         # Incident reports HTML template
│   ├── index.html             # Dashboard HTML template
│   ├── profile.html           # User profile HTML template
│   └── threats.html           # Threat indicators HTML template
```

## Screenshots
*Screenshots will be added here to showcase the application interface.*

## Docker Deployment
1. Build the Docker image:
   ```bash
   docker build -t cybersecurity-threat-intelligence-hub-auto .
   ```
2. Run the Docker container:
   ```bash
   docker run -d -p 8000:8000 cybersecurity-threat-intelligence-hub-auto
   ```

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes. Ensure your code adheres to the project's coding standards and includes appropriate tests.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---
Built with Python and FastAPI.
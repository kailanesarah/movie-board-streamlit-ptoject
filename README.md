<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
</head>
<body>

  <h1>🎬 Movie Dashboard App</h1>

  <p>
    <img src="https://img.shields.io/badge/Python-3.11-blue" alt="Python" />
    <img src="https://img.shields.io/badge/Streamlit-1.33.0-orange" alt="Streamlit" />
    <img src="https://img.shields.io/badge/status-in%20development-yellow" alt="Status" />
  </p>

  <p>
    Movie Board app is an interactive dashboard built with <strong>Streamlit</strong> that consumes a <strong>Movie API</strong>. 
    The application allows you to <strong>view charts and tables</strong> with data fetched via <code>GET</code> requests, 
    and also enables <strong>adding new data</strong> via <code>POST</code> requests. 
    The entire system is protected by <strong>token-based authentication</strong>.
  </p>

  <hr />

  <h2>🚀 Demo</h2>

  <p>
    🔗 Access the hosted project on Render:<br />
    <a href="https://movie-board.onrender.com" target="_blank" rel="noopener noreferrer">https://movie-board.onrender.com</a>
  </p>

  <hr />

  <h2>✨ Features</h2>
  <ul>
    <li>📊 Interactive charts (like pie charts) using Plotly</li>
    <li>📋 Display of detailed tables with movie and review data</li>
    <li>🔐 JWT token authentication</li>
    <li>➕ Adding new movies to the database via form (<code>POST</code>)</li>
    <li>🔄 Real-time data updates after requests</li>
  </ul>

  <hr />

  <h2>✅ Requirements</h2>
  <ul>
    <li>Python 3.10 or higher</li>
    <li>API service account (JWT token may be required)</li>
  </ul>

  <hr />

  <h2>🌟 STAR Methodology (Situation, Task, Action, Result)</h2>
  <ul>
    <li><strong>Situation:</strong> Static or less interactive dashboards make real-time data analysis difficult.</li>
    <li><strong>Task:</strong> Create a dynamic and visually attractive dashboard to display and manage movie data from a custom API, with authentication and data input capabilities.</li>
    <li><strong>Action:</strong> Used Streamlit for the UI, Plotly for charts, and integrated API calls for data fetching (GET) and creation (POST), secured by JWT token authentication.</li>
    <li><strong>Result:</strong> A functional, lightweight, and online-accessible dashboard via Render, enabling simple and secure data analysis and management.</li>
  </ul>

  <hr />

  <h2>🔧 Technologies Used</h2>
  <ul>
    <li><a href="https://www.python.org/" target="_blank" rel="noopener noreferrer">Python 3.11</a></li>
    <li><a href="https://streamlit.io/" target="_blank" rel="noopener noreferrer">Streamlit</a></li>
    <li><a href="https://plotly.com/python/" target="_blank" rel="noopener noreferrer">Plotly</a></li>
    <li><a href="https://docs.python-requests.org/" target="_blank" rel="noopener noreferrer">Requests</a></li>
    <li><a href="https://jwt.io/" target="_blank" rel="noopener noreferrer">JWT Token Authentication</a></li>
  </ul>

  <hr />

  <h2>🧪 How to Run Locally</h2>
  <pre><code>
# Clone the repository
git clone https://github.com/kailanesarah/movie-board-app-streamlit.git
cd movie-board-app-streamlit

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Run Streamlit
streamlit run app.py
  </code></pre>

  <hr />

  <h2>✅ Folder Structure</h2>
  <pre>
movie-board-app-streamlit/
│
├── app.py                         &lt;!-- Main app file initializing Streamlit --&gt;
├── requirements.txt               &lt;!-- Main dependencies --&gt;
├── requirements_dev.txt           &lt;!-- Development/test dependencies --&gt;
│
├── movies/                        &lt;!-- Movies module --&gt;
│   ├── __init__.py
│   ├── page.py                    &lt;!-- User interface (Streamlit) --&gt;
│   ├── repository.py              &lt;!-- API communication (GET/POST movies) --&gt;
│   └── service.py                 &lt;!-- Business logic --&gt;
│
├── reviews/                       &lt;!-- Reviews module --&gt;
│   ├── __init__.py
│   ├── page.py
│   ├── repository.py
│   └── service.py
│
├── genres/                        &lt;!-- Genres module --&gt;
│   ├── __init__.py
│   ├── page.py
│   ├── repository.py
│   └── service.py
│
├── actors/                        &lt;!-- Actors module --&gt;
│   ├── __init__.py
│   ├── page.py
│   ├── repository.py
│   └── service.py
│
├── login/                         &lt;!-- User authentication module --&gt;
│   ├── __init__.py
│   ├── page.py                    &lt;!-- Login screen --&gt;
│   ├── repository.py              &lt;!-- Handles login/auth requests --&gt;
│   └── service.py                 &lt;!-- JWT token generation/storage --&gt;
│
├── home/                          &lt;!-- Home page --&gt;
│   ├── __init__.py
│   ├── page.py
│   ├── repository.py
│   └── service.py
│
└── api/                           &lt;!-- Common module for API auth and global configs --&gt;
    ├── __init__.py
    └── authentication.py          &lt;!-- Token handler, headers, JWT auth --&gt;
  </pre>

  <hr />

  <h2>🚀 Project Architecture</h2>

  <p>
    This project uses a modular, layered architecture, splitting the application into separate modules (movies, reviews, genres, etc.). Each module contains:
  </p>

  <ul>
    <li><strong>page.py:</strong> Presentation layer — user interfaces built with Streamlit;</li>
    <li><strong>repository.py:</strong> Responsible for communication with the API, i.e., sending and receiving data (GET, POST, etc.);</li>
    <li><strong>service.py:</strong> Contains business logic, data manipulation, and logic not directly related to UI or external communication;</li>
    <li><strong>__init__.py:</strong> Declares Python packages.</li>
  </ul>

  <p>
    Additionally, there is an <code>api/</code> module that handles authentication and global API configurations, centralizing security functions and tokens.
  </p>

  <p>
    This separation allows for more organized, reusable, and testable code, easing maintenance and project scalability.
  </p>

  <hr />

  <h2>📄 License</h2>
  <p>This project is licensed under the MIT license. See the LICENSE file for details.</p>

</body>
</html>

# ✨ SkillTrax

## 🚀 Your Personalized Learning Companion

SkillTrax is an intelligent, web-based learning assistant that helps students generate personalized learning roadmaps for different subjects based on their current knowledge level, learning style, educational goals, and time commitment.

![SkillTrax Logo](static/images/logo.png)

## ✅ Features

- 🧠 **Personalized Learning Roadmaps**: Automatically generate custom learning paths based on your inputs
- 📚 **Resource Recommendations**: AI-powered selection of high-quality video and text resources
- 📝 **Syllabus Pro Mode**: Upload a syllabus to create a roadmap aligned with specific course topics
- 🧩 **Automated Quizzes**: Test your knowledge with AI-generated quizzes after each topic
- 📊 **Progress Tracking**: Visualize your learning journey with detailed analytics

## 🛠️ Technology Stack

- 🐍 **Backend**: Flask (Python)
- 🗄️ **Database**: SQLite
- 🎨 **Frontend**: HTML, CSS, JavaScript
- 🤖 **AI Integration**: Generative AI for resource recommendations and quiz generation

## ⚙️ Installation

### Prerequisites

- Python 3.8 or higher
- Git

### Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/skilltrax.git
   cd skilltrax
   ```

2. Create and activate a virtual environment:
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Initialize the SQLite database:
   ```bash
   python init_db.py
   ```

5. Set up environment variables (create a `.env` file in the project root):
   ```
   FLASK_APP=app.py
   FLASK_ENV=development
   SECRET_KEY=your_secret_key_here
   API_KEY=your_ai_service_api_key_here
   ```

## 🚀 Running the Application

1. Ensure your virtual environment is activated:
   ```bash
   # On Windows
   venv\Scripts\activate

   # On macOS/Linux
   source venv/bin/activate
   ```

2. Start the Flask server:
   ```bash
   flask run
   ```

3. Access the application at `http://localhost:5000`

## 📁 Project Structure

```
skilltrax/
├── app.py                  # Main Flask application
├── init_db.py              # Database initialization script
├── requirements.txt        # Project dependencies
├── .env                    # Environment variables (create this)
├── static/                 # Static files (CSS, JS, images)
├── templates/              # HTML templates
├── models/                 # Database models
├── services/               # Business logic and services
│   ├── ai_service.py       # AI integration logic
│   ├── roadmap_service.py  # Roadmap generation
│   └── quiz_service.py     # Quiz generation
└── utils/                  # Utility functions
```

## 🔌 API Endpoints

- `/api/roadmap/create` - Generate a new learning roadmap
- `/api/syllabus/parse` - Parse uploaded syllabus
- `/api/quiz/generate` - Generate quizzes for a topic
- `/api/progress/update` - Update user progress

## 👥 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

## 📞 Contact

For questions or support, please open an issue or contact the project maintainer.

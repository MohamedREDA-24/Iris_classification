# Iris Classification Project

This project implements a machine learning solution for classifying Iris flowers using a Streamlit-based web interface and a FastAPI backend.

## Project Structure

```
.
├── api/                 # FastAPI backend service
├── streamlit_ui/       # Streamlit frontend application
├── iris_model.pkl/     # Trained model files
├── docker-compose.yml  # Docker configuration
└── README.md           # Project documentation
```

## Features

- Machine learning model for Iris flower classification
- Interactive web interface built with Streamlit
- RESTful API backend using FastAPI
- Docker containerization for easy deployment

## Prerequisites

- Python 3.8+
- Docker and Docker Compose
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/MohamedREDA-24/llm-chatbot.git
cd Iris_classification
```

2. Create and activate a virtual environment:
```bash
python -m venv xenv
source xenv/bin/activate  # On Windows: xenv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

### Using Docker (Recommended)

1. Build and start the containers:
```bash
docker-compose up --build
```

2. Access the application:
- Frontend: http://localhost:8501
- API: http://localhost:8000

### Manual Setup

1. Start the API server:
```bash
cd api
uvicorn main:app --reload
```

2. Start the Streamlit UI:
```bash
cd streamlit_ui
streamlit run app.py
```

## Usage

1. Open your web browser and navigate to http://localhost:8501
2. Input the Iris flower measurements (sepal length, sepal width, petal length, petal width)
3. Click the "Predict" button to get the classification result

## API Documentation

The API documentation is available at http://localhost:8000/docs when the API server is running.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

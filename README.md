# Smart Taxi API

<br />

<img src="https://raw.githubusercontent.com/Mhadi-1382/smart-taxi-api/refs/heads/main/assets/logo.svg" alt="Smart Taxi API" width="320">

Smart Taxi API is an intelligent web service for estimating taxi fares based on trip distance and traffic conditions. It uses a Machine Learning model to predict estimated fares and provides a Flask-based REST API. With optional integration of Qwen2.5 for natural-language explanations and Text-to-Speech (TTS) for audio output, it delivers clear and accessible results to users.

<br />

## Features

- Taxi fare prediction using Machine Learning.
- REST API built with Flask.
- JSON responses.
- AI-generated explanations using Qwen2.5.
- Text-to-Speech using edge-tts.
- Automated testing with pytest.
- Logging with Loguru.

## Tech Stack

- **Language:** Python
- **Backend:** Flask (REST API)
- **Machine Learning:** scikit-learn
- **Data Processing:** pandas / CSV
- **Model LLM:** Qwen2.5-0.5B-Instruct
- **LLM Library:** llama-cpp-python
- **Text-to-Speech:** edge-tts
- **HTTP Requests:** requests
- **Testing:** pytest
- **Logging:** Loguru
- **Version Control:** Git / GitHub

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Mhadi-1382/smart-taxi-api.git
cd smart-taxi-api
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Download the LLM Model

Download the following model file:

`qwen2.5-0.5b-instruct-q4_k_m.gguf`

Place the downloaded file in the `models/trained/` directory:

```text
smart-taxi-api/
├── models/
│   └── trained/
│       └── qwen2.5-0.5b-instruct-q4_k_m.gguf
├── main.py
├── requirements.txt
└── README.md
```

Make sure the model path in the application matches the location of the downloaded file.

### 4. Run the Application

```bash
python main.py
```

### 5. Run Tests

```bash
pytest
```

## Documentation

- [Project Documentation](https://github.com/Mhadi-1382/smart-taxi-api/blob/main/assets/smart_taxi_documentation.pdf)
- [Business Plan](https://github.com/Mhadi-1382/smart-taxi-api/blob/main/assets/smart_taxi_business_plan.pdf)

## License

This project is licensed under the [MIT License](https://raw.githubusercontent.com/Mhadi-1382/smart-taxi-api/refs/heads/main/LICENSE).

# Smart Taxi API

<br />

<img src="https://raw.githubusercontent.com/Mhadi-1382/smart-taxi-api/refs/heads/main/assets/logo.svg" alt="Smart Taxi API" width="320">

Smart Taxi API is a web service for estimating taxi fares using Machine Learning. It uses Flask to provide a REST API, Qwen2.5 to generate simple explanations, and Text-to-Speech (TTS) to convert text into audio.

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

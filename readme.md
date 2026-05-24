# WattGuard

A modern desktop application built with PyQt6 to control and monitor a TP-Link Tapo smart plug asynchronously using Python.

## Features

* Turn smart plug ON/OFF
* Modern PyQt6 GUI
* Async device communication using `asyncio`
* Persistent smart plug connection
* External QSS styling support
* Responsive UI using `qasync`
* Environment variable configuration with `.env`

---

## Technologies Used

* Python 3.12
* PyQt6
* qasync
* python-kasa
* asyncio
* Qt Style Sheets (QSS)

---

## Project Structure

```text
WattGuard/
│
├── app.py
├── controllers.py
├── style/
│   └── main.qss
│
├── .env
├── requirements.txt
└── README.md
```

---

## Installation

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd WattGuard
```

---

### 2. Create Virtual Environment

```bash
python3 -m venv .venv
```

Activate the environment:

#### Linux/macOS

```bash
source .venv/bin/activate
```

#### Windows

```bash
.venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install pyqt6 qasync python-kasa python-dotenv
```

---

## Environment Variables

Create a `.env` file in the project root.

Example:

```env
TAPO_IP=192.168.0.78
TAPO_EMAIL=your_email@example.com
TAPO_PASSWORD=your_password
TAPO_PORT=80
```

---

## Running the Application

```bash
python3 app.py
```

---

## Screenshots

Add screenshots here later.

---

## Learning Goals

This project explores:

* Async programming with `asyncio`
* Event-driven GUI architecture
* PyQt6 layouts and styling
* Smart device communication
* Persistent async connections
* Separation of UI and controller logic

---

## Future Improvements

* Real-time power monitoring
* Energy usage graphs
* Device auto-discovery
* Multiple plug support
* Scheduling and automation
* System tray integration
* Dark/light theme switching
* Packaging as executable app

---

## License

This project is for educational and personal use.

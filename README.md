# Flask Web Server

This project is a simple web server built using Flask, a lightweight WSGI web application framework in Python. It serves a basic web page with the ability to extend functionality as needed.

## Project Structure

```
flask-webserver
├── app.py                # Main entry point of the Flask application
├── requirements.txt      # Dependencies required for the project
├── README.md             # Documentation for the project
├── static                # Directory for static files (CSS, JS, images)
│   └── style.css         # CSS styles for the web application
├── templates             # Directory for HTML templates
│   └── index.html        # Main HTML template for the web application
└── .gitignore            # Files and directories to be ignored by Git
```

## Getting Started

To set up and run the Flask web server, follow these steps:

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd flask-webserver
   ```

2. **Create a virtual environment (optional but recommended):**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```
   python app.py
   ```

5. **Access the web server:**
   Open your web browser and go to `http://127.0.0.1:5000`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
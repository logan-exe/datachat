# Installation Guide for DataChat

## Prerequisites
- Python 3.7+
- Git

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/logan-exe/datachat.git
   cd datachat
   ```

2. **Set Up Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables**
   - Create a `.env` file in the root directory and add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_openai_api_key_here
     ```

5. **Run the Application**
   ```bash
   uvicorn app.main:app --reload
   ```

6. **Access the Application**
   - Open your browser and go to `http://127.0.0.1:8000` to access the API.
   - Use the interactive API documentation at `http://127.0.0.1:8000/docs`.

## Additional Notes
- Ensure your database is set up and accessible if connecting external databases.
- Follow best practices for securing your API keys and sensitive information.
# ATS Resume Expert

ATS Resume Expert is a web application designed to help job seekers evaluate their resumes against job descriptions using Google's Generative AI. The application converts uploaded PDF resumes into images, processes them, and provides feedback on how well the resume matches the job description.

## Features

- Upload a PDF resume and convert it to an image.
- Evaluate the resume against a job description.
- Get professional feedback on the strengths and weaknesses of the resume.
- Receive a percentage match score and missing keywords for the job description.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/vismay299/customATS.git
    cd customATS
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory and add your Google API key:

    ```env
    GOOGLE_API_KEY=your_google_api_key
    ```

## Usage

1. Run the Streamlit application:

    ```bash
    streamlit run app.py
    ```

2. Open your web browser and go to `http://localhost:8501`.

3. Enter the job description in the text area.

4. Upload your resume in PDF format.

5. Click on "Tell me about the resume" to get professional feedback or "Percentage Match" to get a percentage match score and missing keywords.

## Project Structure

- `app.py`: The main Streamlit application file.
- `requirements.txt`: A list of required Python packages.
- `.env`: Environment file to store your Google API key.

## Dependencies

- `base64`
- `io`
- `dotenv`
- `streamlit`
- `os`
- `PIL`
- `pdf2image`
- `google.generativeai`

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

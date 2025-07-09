# Buddy: User Activity Analyzer & Extractor

Buddy is a cross-platform system for monitoring, extracting, and analyzing user activity on your computer. It combines Python scripts, a VS Code extension, and AI-powered analysis to classify what you're doing (e.g., coding, browsing, messaging) in real time.

## Features

- **Live Activity Capture**: Continuously collects data about your active window, focused text, clipboard, VS Code editor content, and screen OCR.
- **AI-Powered Analysis**: Uses Google Gemini (via LangChain) to classify your current activity with confidence scores and detailed descriptions.
- **Right-Click Text Extraction**: Instantly logs focused text from any window on right-click.
- **Live Activity Popup**: Displays the latest activity prediction in a live-updating popup window.
- **VS Code Extension**: Writes the content of your active VS Code editor to a file for further analysis.

## Components

### Python Scripts

- `gatheruserdata.py`: Captures user activity data (active window, focused text, clipboard, VS Code text, OCR from screenshots) and writes it to JSON files in the `output/` directory.
- `activity_analyzer.py`: Analyzes the captured user data using Google Gemini to classify the user's activity (e.g., coding, browsing, messaging).
- `user_text_extracter.py`: On right-click, extracts focused text from the active window and logs it with a timestamp.
- `output_popup.py`: Displays the latest activity prediction in a live-updating Tkinter popup window.

### VS Code Extension

- `text/src/extension.ts`: Continuously writes the content of the active text editor to a file on your Desktop (`vscode_live_text.txt`).

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/Buddy.git
cd Buddy
```

### 2. Set Up Python Environment
It is recommended to use a virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Set Up Google Gemini API Key
Create a `.env` file in the project root with your Google Gemini API key:
```
GOOGLE_API_KEY=your_google_gemini_api_key
```

### 4. Install Tesseract OCR
- **macOS**: `brew install tesseract`
- **Windows**: Download from [Tesseract at UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki)

### 5. Install the VS Code Extension
- Open the `text/` folder in VS Code.
- Run `npm install` (if needed).
- Press `F5` to launch the extension in a new VS Code window.

## Usage

1. **Start Data Collection**
   - Run `python gatheruserdata.py` to start collecting user activity data.
2. **Analyze Activity**
   - Run `python activity_analyzer.py` to analyze the latest data and classify your activity.
3. **Live Activity Popup**
   - Run `python output_popup.py` to display a live-updating popup with the latest prediction.
4. **Right-Click Text Extraction**
   - Run `python user_text_extracter.py` and right-click on any window to log focused text.
5. **VS Code Live Text**
   - The extension will automatically write the active editor's content to `~/Desktop/vscode_live_text.txt`.

## Output
- All user data and predictions are stored in the `output/` directory.
- Screenshots (if any) are saved temporarily and deleted after OCR.

## Dependencies
See `requirements.txt` for Python dependencies. Key packages:
- `pytesseract`, `Pillow`, `pyperclip`, `langchain`, `langchain_google_genai`, `google-generativeai`, `mss`, `opencv-python`, `numpy`, `python-dotenv`

## Security & Privacy
- All data is stored locally by default.
- Be mindful of sensitive information in captured text, clipboard, and screenshots.
- The Google Gemini API key is required for AI analysis.

## License
MIT License (add your license file if needed)

## Acknowledgments
- [LangChain](https://github.com/langchain-ai/langchain)
- [Google Generative AI](https://ai.google.dev/)
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) 

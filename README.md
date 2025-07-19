# 🎵 Genius Lyrics Decoder

A powerful web application that provides deep analysis and interpretation of song lyrics using AI. The project combines the Genius API for lyrics retrieval with advanced language models to offer meaningful insights into songs.

## 🌟 Features

- **Lyrics Retrieval**: Automatically fetches song lyrics using the Genius API
- **AI-Powered Analysis**: Provides two levels of interpretation:
  - Overall song summary and thematic analysis
  - Detailed line-by-line interpretation of lyrics
- **User-Friendly Interface**: Clean and simple Streamlit-based frontend
- **Modern Architecture**: FastAPI backend with async support

## 🛠️ Technical Stack

### Backend
- **FastAPI**: Modern, fast web framework for building APIs
- **LangChain**: For structured interaction with language models
- **Genius API**: For retrieving song lyrics
- **Python 3.9+**: Async support and modern Python features

### Frontend
- **Streamlit**: For building the interactive web interface

## 🚀 Getting Started

### Prerequisites
- Python 3.9 or higher
- Genius API token
- LLM API access

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/genius-lyrics-decoder.git
cd genius-lyrics-decoder
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file in the root directory with:
```env
GENIUS_API_TOKEN=your_genius_token_here
```

### Running the Application

1. Start the backend server:
```bash
python -m backend.main
```

2. Start the frontend:
```bash
streamlit run frontend/app.py
```
or
```bash
python -m frontend/bot.py
```

## 🎯 Usage

1. Open the web interface (typically at `http://localhost:8501`)
2. Enter the artist name and song title
3. Click "Analyze" to get:
   - A comprehensive summary of the song's themes and motifs
   - Detailed interpretations of paired lyrics

## 🔍 How It Works

1. **Input Processing**: User provides artist and song information
2. **Lyrics Retrieval**: System fetches lyrics using the Genius API
3. **Analysis Pipeline**:
   - Generates an overall summary of the song
   - Processes lyrics in pairs for more contextual interpretation
   - Uses AI to provide meaningful interpretations
4. **Result Presentation**: Displays both summary and line-by-line analysis in a user-friendly format


## 🔮 Future Improvements

- Multi-language support
- More detailed musical context analysis
- Support for comparing multiple songs
- Enhanced error handling and user feedback
- Caching mechanism for frequently requested songs
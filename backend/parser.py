import fitz  # PyMuPDF

def extract_text_from_file(file_path, file_name):
    """Extracts text from a given file (PDF or TXT)."""
    text = ""
    try:
        if file_name.lower().endswith('.pdf'):
            with fitz.open(file_path) as doc:
                for page in doc:
                    text += page.get_text()
        elif file_name.lower().endswith('.txt'):
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read()
        else:
            return None # Unsupported file type
    except Exception as e:
        print(f"Error processing file {file_name}: {e}")
        return None
    return text
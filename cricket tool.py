import pytesseract
from PIL import Image
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

# --- CONFIGURATION ---
# If you are on Windows, uncomment the line below and point to your tesseract.exe
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def get_questions_from_image(image_path):
    """Extracts text from the photo of your OBT questions."""
    if not os.path.exists(image_path):
        print(f"Error: File {image_path} not found.")
        return []
    
    # Open and convert to grayscale for better OCR accuracy
    img = Image.open(image_path).convert('L')
    text = pytesseract.image_to_string(img)
    
    # Split text into individual questions (assuming one per line or separated by ?)
    raw_questions = text.split('\n')
    clean_questions = [q.strip() for q in raw_questions if len(q.strip()) > 15]
    return clean_questions

def rank_importance(obt_questions, past_dbatu_data):
    """Ranks OBT questions based on similarity to University patterns."""
    all_docs = obt_questions + past_dbatu_data
    
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(all_docs)
    
    obt_vectors = tfidf_matrix[:len(obt_questions)]
    past_vectors = tfidf_matrix[len(obt_questions):]
    
    results = []
    for i, vec in enumerate(obt_vectors):
        # Compare current question to the entire history of DBATU exams
        similarity_scores = cosine_similarity(vec, past_vectors)
        # We take the average of top matches to see how "popular" this topic is
        avg_importance = similarity_scores.mean() 
        results.append((obt_questions[i], avg_importance))
    
    # Sort: Highest importance first
    return sorted(results, key=lambda x: x[1], reverse=True)

# --- YOUR DATA ---

# 1. Put the filename of your OBT image here
image_input = "obt_test_paper.jpg" 

# 2. Paste as many DBATU past paper questions here as possible
# The more you add, the smarter the prediction becomes!
dbatu_history_bank = [
    "Define and explain Bernoulli's Theorem with neat sketch.",
    "Explain the working of 4-stroke Diesel engine.",
    "What is the difference between path function and point function?",
    "State and explain Zeroth Law of Thermodynamics.",
    "Derive an expression for air standard efficiency of Otto Cycle.",
    "Explain the concept of internal energy and enthalpy.",
    "What are the various types of thermodynamic systems?"
]

# --- RUN ---
print("Scanning your OBT image...")
current_obt = get_questions_from_image(image_input)

if current_obt:
    print(f"Detected {len(current_obt)} questions from image.")
    ranked = rank_importance(current_obt, dbatu_history_bank)
    
    print("\n--- PREDICTION FOR YOUR 10-MARK TEST ---")
    print("Probability | Question")
    print("-" * 50)
    for q, score in ranked:
        # Scale score for display
        chance = "HIGH" if score > 0.05 else "MEDIUM"
        print(f"[{chance}] - {q}")
else:
    print("Could not read questions. Try a clearer photo!")
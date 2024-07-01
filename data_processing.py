import json
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_course_data(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def preprocess_course_data(courses):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )
    
    processed_data = []
    for course in courses:
        text = f"Title: {course['title']}\n"
        text += f"Overview: {course['course_overview']}\n"
        text += "Course Details:\n"
        for key, value in course['course_info_details'].items():
            text += f"- {key}: {value}\n"
        text += f"Link: {course['link']}"
        
        chunks = text_splitter.split_text(text)
        processed_data.extend(chunks)
    
    return processed_data

def get_processed_data():
    courses = load_course_data('courses.json')
    return preprocess_course_data(courses)
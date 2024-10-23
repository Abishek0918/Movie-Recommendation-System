import os
import pickle

file_path = 'models/movie_list.pkl'

# Check if the file exists
if os.path.exists(file_path):
    try:
        with open(file_path, 'rb') as file:
            movies = pickle.load(file)
            print("File loaded successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
else:
    print("File not found.")

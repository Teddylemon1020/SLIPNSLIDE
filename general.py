import os 

def create_directory(directory):
    """Create a directory if it doesn't exist."""
    try:
        os.makedirs(directory, exist_ok=True)
        print(f"Directory '{directory}' created or already exists.")
    except Exception as e:
        print(f"Error creating directory '{directory}': {e}")



create_directory("example_dir")
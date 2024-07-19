import os
import shutil
import logging

logging.basicConfig(filename="file_organiser.log", level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s")


# DEFINE COMPREHENSIVE FILE EXTENSIONS
images = ['.jpeg', '.jpg', '.png', '.gif', '.bmp', '.tiff', '.svg', '.webp', '.jfif', '.ico', '.heif']
videos = ['.avi', '.mp4', '.mov', '.mkv', '.webm', '.flv', '.wmv', '.mpg', '.mpeg', '.3gp', '.ts']
audios = ['.mp3', '.ogg', '.wav', '.amr', '.flac', '.aac', '.m4a', '.wma', '.opus']
documents = ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.ppt', '.pptx', '.odt', '.ods', '.odp', '.docm', '.dot', '.dotx', '.dotm', '.epub', '.mobi', '.azw', '.xps', '.tex', '.xml', '.rtf', '.html', '.htm', '.csv']
compressed = ['.zip', '.rar', '.7z', '.iso', '.tar', '.gz', '.bz2', '.xz', '.z', '.dmg']
programs = ['.exe', '.msi', '.app', '.bat', '.sh', '.jar']

# LISTS TO TRACK MOVED FILES
images_folder = []
videos_folder = []
audios_folder = []
documents_folder = []
compressed_folder = []
programs_folder = []
others_folder = []



def get_input():
    print("THIS IS A FILE ORGANISER APPLICATION.\nThe files will be organised based on their extensions in their respective folders.")
    start_dir=input(r"Enter the start directory(PATH TO WHERE THE FILES CURRENTLY ARE e.g C:\Users\PC\Downloads): ")

    while True:
        if not os.path.exists(start_dir):
            print("The directory you entered does not exist.")
            start_dir = input(r"Enter the start directory(PATH TO WHERE THE FILES CURRENTLY ARE e.g C:\Users\PC\Downloads): ")
        else:
            print(f"\n THE BASE DIRECTORY IS: {start_dir}")
            break
    return start_dir

START_DIR=get_input()
IMAGE_DIR = os.path.join(START_DIR, "Images")
VIDEO_DIR = os.path.join(START_DIR, "Video")
AUDIO_DIR = os.path.join(START_DIR, "Audios")
DOCUMENTS_DIR = os.path.join(START_DIR, "Documents")
ZIPFILES_DIR = os.path.join(START_DIR, "Compressed")
PROGRAMS_DIR = os.path.join(START_DIR, "Programs")
OTHERS_DIR = os.path.join(START_DIR, "Others")

def create_directories():
    for folder in [IMAGE_DIR, VIDEO_DIR, AUDIO_DIR, DOCUMENTS_DIR, ZIPFILES_DIR, PROGRAMS_DIR, OTHERS_DIR]:
        if not os.path.exists(folder):
            os.makedirs(folder)
            logging.info(f"Directory {folder} created successfully!")

def move_files():
    with os.scandir(START_DIR) as files:
        for file in files:
            if file.is_file():
                file_extension = os.path.splitext(file.name)[1].lower()
                file_source = os.path.join(START_DIR, file.name)
                
                if file_extension in images:
                    destination = os.path.join(IMAGE_DIR, file.name)
                    images_folder.append(file)
                elif file_extension in videos:
                    destination = os.path.join(VIDEO_DIR, file.name)
                    videos_folder.append(file)
                elif file_extension in audios:
                    destination = os.path.join(AUDIO_DIR, file.name)
                    audios_folder.append(file)
                elif file_extension in documents:
                    destination = os.path.join(DOCUMENTS_DIR, file.name)
                    documents_folder.append(file)
                elif file_extension in compressed:
                    destination = os.path.join(ZIPFILES_DIR, file.name)
                    compressed_folder.append(file)
                elif file_extension in programs:
                    destination = os.path.join(PROGRAMS_DIR, file.name)
                    programs_folder.append(file)
                else:
                    destination = os.path.join(OTHERS_DIR, file.name)
                    others_folder.append(file)
                
                try:
                    shutil.move(file_source, destination)
                    logging.info(f"{file.name} moved to {destination}")
                except Exception as e:
                    print(f"ERROR MOVING {file_source} TO {destination}: {e}")
                    logging.error(f"ERROR MOVING {file_source} TO {destination}: {e}")

def print_summary():
    any_files_moved = False

    if images_folder:
        print(f"\n{len(images_folder)} IMAGE FILES MOVED TO {IMAGE_DIR}\n")
        any_files_moved = True
    if videos_folder:
        print(f"{len(videos_folder)} VIDEO FILES MOVED TO {VIDEO_DIR}\n")
        any_files_moved = True
    if audios_folder:
        print(f"{len(audios_folder)} AUDIO FILES MOVED TO {AUDIO_DIR}\n")
        any_files_moved = True
    if documents_folder:
        print(f"{len(documents_folder)} DOCUMENT FILES MOVED TO {DOCUMENTS_DIR}\n")
        any_files_moved = True
    if compressed_folder:
        print(f"{len(compressed_folder)} COMPRESSED FILES MOVED TO {ZIPFILES_DIR}\n")
        any_files_moved = True
    if programs_folder:
        print(f"{len(programs_folder)} PROGRAM FILES MOVED TO {PROGRAMS_DIR}\n")
        any_files_moved = True
    if others_folder:
        print(f"{len(others_folder)} OTHER FILES MOVED TO {OTHERS_DIR}\n")
        any_files_moved = True

    if not any_files_moved:
        print("\nNO FILES FOUND TO MOVE.\n")

def main():
    print("\n STARTING THE FILE ORGANISER APPLICATION...\n")
    print("1. Images will be saved in: ", IMAGE_DIR)
    print("2. Videos will be saved in: ", VIDEO_DIR)
    print("3. Audios will be saved in: ", AUDIO_DIR)
    print("4. Documents will be saved in: ", DOCUMENTS_DIR)
    print("5. Compressed files will be saved in: ", ZIPFILES_DIR)
    print("6. Programs will be saved in: ", PROGRAMS_DIR)
    print("7. Others will be saved in: ", OTHERS_DIR)
    create_directories()
    move_files()
    print_summary()
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()


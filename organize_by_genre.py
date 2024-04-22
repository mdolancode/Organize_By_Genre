import os
from mutagen.mp3 import MP3
from mutagen import File

def get_genre(file_path):
    _, file_extension = os.path.splitext(file_path.lower())

    if file_extension == '.mp3':
        audio = MP3(file_path)
        return audio.tags.get('TCON', ['Unknown'])[0]
    elif file_extension == '.aiff':
        audio = File(file_path)
        return audio.tags.get('genre', ['Unknown'])[0]
    else:
        return 'Unknown'
    
def organize_by_genre(root_dir, output_dir):
    unknown_genre_dir = os.path.join(output_dir, 'Unknown')
    if not os.path.exists(unknown_genre_dir):
        os.makedirs(unknown_genre_dir)

    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            genre = get_genre(file_path)

            if genre == 'Unknown':
                     output_file_path = os.path.join(unknown_genre_dir, filename)
            else:
                genre_dir = os.path.join(output_dir, genre)
                if not os.path.exists(genre_dir):
                    os.makedirs(genre_dir)
                    output_file_path = os.path.join(genre_dir, filename)

            os.rename(file_path, output_file_path)

if __name__ == "__main__":
    root_dir = input("Enter the directory where your music files are located: ")
    output_dir = input("Enter the directory where you want to organize the music by genre: ")

    organize_by_genre(root_dir, output_dir)
    print("Music files have been organized by genre.")



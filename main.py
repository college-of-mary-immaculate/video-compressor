import tkinter as tk
from tkinter import messagebox
import os
from PIL import Image
from moviepy.editor import VideoFileClip

def compress_video(input_path, output_path, bitrate='500k'):
    try:
        clip = VideoFileClip(input_path)
        clip.write_videofile(output_path, bitrate=bitrate)
        messagebox.showinfo("Success", f"Video saved to {output_path} with bitrate={bitrate}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to compress video.\n{str(e)}")

def find_first_video_meeting_size(directory, size_limit):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.mp4', '.avi', '.mov', '.mkv')):
                file_path = os.path.join(root, file)
                file_size = os.path.getsize(file_path)

                if file_size >= size_limit:
                    return file_path, file_size

    return None, 0  

def main():
    root = tk.Tk()
    root.withdraw()  

    search_directory = "C:/Users/Izyne/Videos/Captures"  

    size_limit = 1024 * 1024 * 1024  

    first_video, first_video_size = find_first_video_meeting_size(search_directory, size_limit)

    if first_video_size >= size_limit:
        file_type = 'video'
        largest_file = first_video
        largest_size = first_video_size

        choice = messagebox.askyesno(f"Largest {file_type.capitalize()} Found",
                                     f"The largest {file_type} found is:\n{largest_file}\n"
                                     f"Size: {largest_size / (1024 * 1024):.2f} MB\nDo you want to compress it?")

        if choice:
            output_path = f"{os.path.splitext(largest_file)[0]}_compressed{os.path.splitext(largest_file)[1]}"
            compress_video(largest_file, output_path, bitrate='500k')
    else:
        messagebox.showinfo("No Large Files Found", "No video files larger than 1024 MB were found.")

if __name__ == "__main__":
    main()
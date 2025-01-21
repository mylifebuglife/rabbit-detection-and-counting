from batch_processing import process_all_videos  # Import the batch processing function
import tkinter as tk
from tkinter import filedialog, messagebox
import os


class RabbitDetectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rabbit Detector")
        self.root.geometry("400x200")
        self.input_folder = None
        self.output_folder = None

        # Create GUI elements
        tk.Label(root, text="Rabbit Detector", font=("Helvetica", 16, "bold")).pack(pady=10)

        tk.Button(root, text="Select Input Folder", command=self.select_input_folder).pack(pady=5)
        tk.Button(root, text="Select Output Folder", command=self.select_output_folder).pack(pady=5)
        tk.Button(root, text="Start Processing", command=self.start_processing).pack(pady=20)

    def select_input_folder(self):
        """Prompt user to select the input folder."""
        folder = filedialog.askdirectory(title="Select the folder containing videos")
        if folder:
            self.input_folder = folder
            messagebox.showinfo("Input Folder Selected", f"Selected folder:\n{folder}")

    def select_output_folder(self):
        """Prompt user to select the output folder."""
        folder = filedialog.askdirectory(title="Select the output folder for the CSV file")
        if folder:
            self.output_folder = folder
            messagebox.showinfo("Output Folder Selected", f"Selected folder:\n{folder}")

    def start_processing(self):
        """Start the video processing."""
        if not self.input_folder or not self.output_folder:
            messagebox.showwarning("Missing Folders", "Please select both input and output folders!")
            return

        output_csv = os.path.join(self.output_folder, "rabbit_count_results.csv")

        try:
            # Process videos
            process_all_videos(self.input_folder, output_csv)

            # Notify user of success
            messagebox.showinfo("Success", f"Processing complete. Results saved to:\n{output_csv}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")


def main():
    root = tk.Tk()
    app = RabbitDetectorApp(root)
    root.mainloop()


if __name__ == "__main__":
    import multiprocessing
    multiprocessing.freeze_support()  # Fix for PyInstaller and multiprocessing
    main()


#2nd right attempt
# from batch_processing import process_all_videos  # Import the batch processing function
# import tkinter as tk
# from tkinter import filedialog, messagebox
# import os

# def select_folder(prompt):
#     """Helper function to select a folder."""
#     root = tk.Tk()
#     root.withdraw()  # Hide the root window
#     folder_path = filedialog.askdirectory(title=prompt)
#     root.destroy()
#     return folder_path

# def main():
#     try:
#         # Select input folder
#         input_folder = select_folder("Select the folder containing videos")
#         if not input_folder:
#             messagebox.showinfo("Cancelled", "No input folder selected. Exiting.")
#             return

#         # Select output folder
#         output_folder = select_folder("Select the output folder for the CSV file")
#         if not output_folder:
#             messagebox.showinfo("Cancelled", "No output folder selected. Exiting.")
#             return

#         # Output CSV path
#         output_csv = os.path.join(output_folder, "rabbit_count_results.csv")

#         # Process videos
#         process_all_videos(input_folder, output_csv)

#         # Notify user of success
#         messagebox.showinfo("Success", f"Processing complete. Results saved to:\n{output_csv}")

#     except Exception as e:
#         messagebox.showerror("Error", f"An error occurred: {e}")

# if __name__ == "__main__":
#     import multiprocessing
#     multiprocessing.freeze_support()  # Fix for PyInstaller and multiprocessing
#     main()


#first right attempt
# import tkinter as tk
# from tkinter import filedialog, messagebox
# import os
# from batch_processing import process_all_videos


# def run_app():
#     """Run the Rabbit Detector app."""
#     app = tk.Tk()
#     app.title("Rabbit Detector")
#     app.geometry("400x200")

#     input_folder = tk.StringVar()
#     output_folder = tk.StringVar()

#     def browse_input():
#         folder = filedialog.askdirectory(title="Select Input Folder")
#         input_folder.set(folder)

#     def browse_output():
#         folder = filedialog.askdirectory(title="Select Output Folder")
#         output_folder.set(folder)

#     def start_processing():
#         if not input_folder.get() or not output_folder.get():
#             messagebox.showerror("Error", "Please select both input and output folders.")
#             return
#         try:
#             input_path = input_folder.get()
#             output_path = os.path.join(output_folder.get(), "aggregated_rabbit_counts.csv")
#             process_all_videos(input_path, output_path)
#             messagebox.showinfo("Success", f"Processing complete. Results saved to:\n{output_path}")
#         except Exception as e:
#             messagebox.showerror("Error", f"An error occurred: {str(e)}")

#     tk.Label(app, text="Select Input Folder:").pack(pady=5)
#     tk.Entry(app, textvariable=input_folder, width=40).pack(pady=5)
#     tk.Button(app, text="Browse", command=browse_input).pack(pady=5)

#     tk.Label(app, text="Select Output Folder:").pack(pady=5)
#     tk.Entry(app, textvariable=output_folder, width=40).pack(pady=5)
#     tk.Button(app, text="Browse", command=browse_output).pack(pady=5)

#     tk.Button(app, text="Start Processing", command=start_processing).pack(pady=10)

#     app.mainloop()


# if __name__ == "__main__":
#     run_app()



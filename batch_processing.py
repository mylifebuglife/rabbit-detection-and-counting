import os
from multiprocessing import Pool
from single_video_processing import process_single_video

def process_all_videos(video_folder, output_csv):
    """Process all videos in the folder using multiprocessing."""
    video_files = [os.path.join(video_folder, f) for f in os.listdir(video_folder) if f.endswith(".mp4")]

    # Use multiprocessing to process videos in parallel
    with Pool(processes=os.cpu_count()) as pool:
        results = pool.map(process_single_video, video_files)

    # Write aggregated results to CSV
    with open(output_csv, "w") as f:
        f.write("Video Name,Total Frames,Total Rabbits Detected\n")
        for video_name, frame_count, total_rabbits in results:
            f.write(f"{video_name},{frame_count},{total_rabbits}\n")

    print(f"Processing complete. Results saved to {output_csv}")


if __name__ == "__main__":
    VIDEO_FOLDER = "/Users/debtanu/Desktop/HiWi/final/testappvideos"  # Input video folder
    OUTPUT_CSV = "/Users/debtanu/Desktop/HiWi/final/testappoutput/aggregated_rabbit_counts.csv"  # Output CSV file

    process_all_videos(VIDEO_FOLDER, OUTPUT_CSV)


# import os
# import sys
# import argparse
# from multiprocessing import Pool
# from single_video_processing import process_single_video


# def process_all_videos(input_folder, output_folder):
#     """Process all videos in the folder using multiprocessing."""
#     video_files = [os.path.join(input_folder, f) for f in os.listdir(input_folder) if f.endswith(".mp4")]

#     # Use multiprocessing to process videos in parallel
#     with Pool(processes=os.cpu_count()) as pool:  # Use all available CPU cores
#         results = pool.map(process_single_video, video_files)

#     # Write aggregated results to CSV
#     output_csv = os.path.join(output_folder, "aggregated_rabbit_counts.csv")
#     with open(output_csv, "w") as f:
#         f.write("Video Name,Total Frames,Total Rabbits Detected\n")
#         for video_name, frame_count, total_rabbits in results:
#             f.write(f"{video_name},{frame_count},{total_rabbits}\n")

#     print(f"Processing complete. Results saved to {output_csv}")


# if __name__ == "__main__":
#     parser = argparse.ArgumentParser()
#     parser.add_argument("--input_folder", required=True, help="/Users/debtanu/Desktop/HiWi/final/testappvideos")
#     parser.add_argument("--output_folder", required=True, help="Path to the folder to save the output CSV")
#     args = parser.parse_args()

#     process_all_videos(args.input_folder, args.output_folder)

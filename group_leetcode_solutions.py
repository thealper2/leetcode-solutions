import os
import re
import shutil

def create_folders(base_dir, max_question=4000):
    for lower_bound in range(0, max_question, 100):
        upper_bound = lower_bound + 99
        folder_name = f"{lower_bound:04d}-{upper_bound:04d}"
        folder_path = os.path.join(base_dir, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        print(f"Created folder: {folder_name}")

def move_files(source_dir):
    files = [f for f in os.listdir(source_dir) if (f.endswith('.py') or f.endswith('.js')) and os.path.isfile(os.path.join(source_dir, f))]
    
    for filename in files:
        match = re.match(r'^(\d{1,4})', filename)
        if match:
            question_num = int(match.group(1))
            lower_bound = (question_num // 100) * 100
            upper_bound = lower_bound + 99
            
            folder_name = f"{lower_bound:04d}-{upper_bound:04d}"
            src_path = os.path.join(source_dir, filename)
            dest_path = os.path.join(source_dir, folder_name, filename)
            
            try:
                shutil.move(src_path, dest_path)
                print(f"Moved: {filename} → {folder_name}/")
            except Exception as e:
                print(f"Error moving {filename}: {e}")

if __name__ == "__main__":
    leetcode_dir = "."
    
    print("Creating folders...")
    create_folders(leetcode_dir)
    
    print("\nMoving files...")
    move_files(leetcode_dir)
    
    print("\nDone!")
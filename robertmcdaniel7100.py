from mega import Mega
import threading
import time

successful_renames = 0

def rename_files(mega, files_to_rename):
    global successful_renames
    for file_name in files_to_rename:
        if "@nsfwpack0" not in file_name:
            new_name = f"@nsfwpack0 Telegram {file_name}"
            file = mega.find(file_name)
            try:
                mega.rename(file, new_name)
                print(f"{file_name} --> {new_name}")
                successful_renames += 1
            except Exception as e:
                print(f"Failed to rename {file_name}: {e}")  

def main():
    mega = Mega()
    m = mega.login("elizabethsmith4269@fexpost.com", "Bot@7051")

    files = m.get_files()
    extracted = []

    for x in files:
        if files[x]:
            try:
                extracted.append(files[x]['a']['n'])
            except:
                pass
    extracted = extracted[(len(extracted)//2):]
    print(f"Total :- {len(extracted)}")
    time.sleep(1)
    num_threads = 50
    files_per_thread = len(extracted) // num_threads
    threads = []

    for i in range(num_threads):
        start_idx = i * files_per_thread
        end_idx = start_idx + files_per_thread if i < num_threads - 1 else len(extracted)
        thread_files = extracted[start_idx:end_idx]
        thread = threading.Thread(target=rename_files, args=(m, thread_files))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Print the total number of successful renames
    print(f"Successful Renames: {successful_renames}/{len(extracted)}")

if __name__ == "__main__":
    main()

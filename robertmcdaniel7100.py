from mega import Mega
import threading
import time

# Define a counter for successful renames
successful_renames = 0

def rename_files(mega, files_to_rename):
    global successful_renames  # Declare the global counter variable
    for file_name in files_to_rename:
        new_name = file_name
        
        patterns_to_replace = {
            "Telegram @OnlyShare0 - - ": "",
            "Telegram @OnlyShare0 - -": "",
            "Telegram @OnlyShare0 -- ": "",
            "Telegram @OnlyShare0 --": "",
            "Telegram @OnlyShare0 - ": "",
            "Telegram @OnlyShare0 -": "",
            "Telegram @OnlyShare0 ": "",
            "Telegram @OnlyShare0": "",
            "@Newsociety70 Telegram Join Channel ": "",
            "@Newsociety70 Telegram Join Channel": "",
            "_@newsociety0 telegram Fsociety_TG Reddit_ ": "",
            "_@newsociety0 telegram Fsociety_TG Reddit_": "",
            "@Nud3Cloud Telegram ": "",
            "@Nud3Cloud Telegram": "",
            "Fsociety_TG SubReddit Download Join ": "",
            "Fsociety_TG SubReddit Download Join": "",
        }
        
        if any(pattern in file_name for pattern in patterns_to_replace):
            for pattern, replacement in patterns_to_replace.items():
                new_name = new_name.replace(pattern, replacement)

            file = mega.find(file_name)
            try:
                mega.rename(file, new_name)
                print(f"{file_name} --> {new_name}")

                successful_renames += 1
            except:
                try:
                    mega.rename(file, new_name)
                    print(f"{file_name} --> {new_name}")

                    successful_renames += 1
                except:
                    print(f"Failed to rename {file_name}")   

def main():
    mega = Mega()
    m = mega.login("robertmcdaniel7100@fexpost.com", "Bot@7051")

    files = m.get_files()
    extracted = []

    for x in files:
        if files[x]:
            try:
                extracted.append(files[x]['a']['n'])
            except:
                pass
        
    dump_txt = ["Telegram @OnlyShare0 - - ", "Telegram @OnlyShare0 - -", "Telegram @OnlyShare0 --", "Telegram @OnlyShare0 -", "Telegram @OnlyShare0", "@Newsociety70 Telegram Join Channel", "_@newsociety0 telegram Fsociety_TG Reddit_", "Fsociety_TG SubReddit Download Join", "@Nud3Cloud Telegram"]
    matches = [txt for txt in extracted if any(keyword in txt for keyword in dump_txt)]
    print(f"Total :- {len(matches)}")
    time.sleep(1)
    num_threads = 100
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
    print(f"Successful Renames: {successful_renames}/{len(matches)}")

if __name__ == "__main__":
    main()

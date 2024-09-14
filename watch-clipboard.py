import pyperclip
import time

def main():
    # File to append clipboard content
    file_path = 'clipboard_log.txt'
    
    # Get the initial clipboard content
    last_clipboard_content = pyperclip.paste()
    
    while True:
        # Get the current clipboard content
        current_clipboard_content = pyperclip.paste()
        
        # Check if the clipboard content has changed
        if current_clipboard_content != last_clipboard_content:
            # Append the new content to the file
            with open(file_path, 'a', encoding='utf-8') as file:
                file.write(current_clipboard_content + '\n')
            
            # Update the last clipboard content
            last_clipboard_content = current_clipboard_content
        
        # Sleep for a short duration before checking again
        time.sleep(1)

if __name__ == "__main__":
    main()
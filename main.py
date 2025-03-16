import sys, platform, tkinter as tk

# input optimizer (only linux)
if platform.system() == 'Linux':
    import readline

import uuid

from func.send_greeting import *
from func.converts import *
from func.file_management import *
from func.read_options import *
from func.count_chars import *
from func.count_words import *
from options_main_menu import *

version = '1.3.0'

# Generate report
def generate_report(file_path, window_mode = False):
    # Permission and existence check
    try:
        get_file(file_path)
    except PermissionError:
        if window_mode:
            return "Error when processing file: no permission!\nTry changing the file permissions or run Bookbot as administrator."
        print("Error when processing file: no permission!")
    except UnicodeDecodeError:
        if window_mode:
            return "Error when processing file: failed to decode Unicode!\nBookbot can't process files that use non-standard text, such as .xlsx, .pdf, .docx, etc."
        print("Error when processing file: failed to decode Unicode!\nBookbot can't process files that use non-standard text, such as .xlsx, .pdf, .docx, etc.")

    # Import options
    current_options = read_options()

    option_save_to_file = int(current_options[1])
    option_report_more_chars = int(current_options[3])

    # Sometimes a substring crash occurs, account for that
    try:
        text_to_print = f'======== REPORT for {file_path[file_path.rindex("/") + 1:]} ========\n'
    except ValueError:
        text_to_print = f'======== REPORT for {file_path} ========\n'
    
    text_to_print += '\n'
    text_to_print += f'    * Word count: {count_words(get_file(file_path))}\n'
    text_to_print += '\n'
    text_to_print += '    * Character counts:\n'

    # Charcount and check for options
    processed_stats = convert_to_sorted_list(count_chars(get_file(file_path)))

    if option_report_more_chars:
        for dict in processed_stats:
            if dict['char'] == '\n':
                pass
            elif dict['char'] == ' ':
                text_to_print += (f'       > [space] was found {dict["count"]} times\n')
            else:
                text_to_print += (f'       > {dict["char"]} was found {dict["count"]} times\n')
    else:
        for dict in processed_stats:
            if dict['char'].isalpha():
                text_to_print += (f'       > {dict["char"]} was found {dict["count"]} times\n')
            elif dict['char'] == ' ':
                pass # Exclude spaces

    # Get vowel/consonant counts
    text_vowel_or_consonant_stats = count_vowels_and_consonants(get_file(file_path))

    text_to_print += '\n'
    text_to_print += f'    * Vowel count: {text_vowel_or_consonant_stats[0]}\n'
    text_to_print += f'    * Consonant count: {text_vowel_or_consonant_stats[1]}'
    text_to_print += '\n'
    text_to_print += '=================================='

    if option_save_to_file:
        # Sometimes a substring crash occurs, account for that  
        try:
            create_report_file(f'{uuid.uuid4()}-{file_path[file_path.rindex("/") + 1:]}', text_to_print)
        except ValueError:
            create_report_file(f'{uuid.uuid4()}-{file_path}.txt', text_to_print)
        # File format: (random uuid)-(filename).txt
    
    if window_mode:
        return text_to_print
    else:
        clear_prompt_screen()
        print(text_to_print)
        sleep(2)
        send_greeting('start', False)

# Console run mode
def console_mode():
    while True:
        try:
            inp = input('    ║ File path: ')

            if inp == 'exit' or inp == 'quit' or inp == 'x' or inp == 'q':
                send_greeting('quickexit')
                sys.exit()

            elif inp == 'help' or inp == 'h':
                send_greeting('help')

            elif inp == 'options' or inp == 'opt':
                options_main_menu()

            else:
                try:
                    generate_report(inp)
                except FileNotFoundError:
                    print('    ║ File not found! Example usage: file.txt or folder/file.txt')

        except KeyboardInterrupt:
            send_greeting('quickexit')
            sys.exit()

def window_mode():
    main_window = tk.Tk()

    main_window.title('Bookbot')

    def open_file_dialog(): 
        from tkinter import filedialog
        file_path = tk.filedialog.askopenfilename()

        if file_path:
            report_text = generate_report(file_path, True)

            file_name_indicator.config(text = f'Selected: {file_path}')
            report_output.delete(1.0, tk.END)
            report_output.insert(1.0, report_text)

    open_button = tk.Button(main_window, text="Open File", command=open_file_dialog)
    open_button.pack(pady=10)

    file_name_indicator = tk.Label(main_window, text='Waiting for file...')
    file_name_indicator.pack(pady=10)

    report_output = tk.Text(main_window, height=30)
    report_output.pack()

    tk.Button(main_window, text='Quit', command=sys.exit).pack(pady=10)

    tk.Label(text=f'Bookbot version {version}').pack(pady=10)

    main_window.mainloop()
    
# Main
def main():
    send_greeting("select-modal")
    while True:
        try:
            try:
                option = get_file('default_run_mode')

                if option == '1':
                    send_greeting('start')
                    console_mode()
                elif option == '2':
                    send_greeting('window-running') 
                    window_mode()
                    sys.exit()
            except FileNotFoundError:
                create_file_write('default_run_mode')

            inp = input('    ║ ')
            if inp == '1':
                send_greeting('start')
                console_mode()
            elif inp == '2':
                send_greeting('window-running') 
                window_mode()
                sys.exit()
            elif inp == 'exit' or inp == 'quit' or inp == 'x' or inp == 'q':
                send_greeting('quickexit')
                sys.exit()
        except KeyboardInterrupt:
            send_greeting('quickexit')
            sys.exit()
    
if __name__ == '__main__':
    main()
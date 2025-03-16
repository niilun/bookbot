import platform, os

def clear_prompt_screen():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def send_greeting(type, clear_screen = True):
    if clear_screen:
        clear_prompt_screen()

    # start
    if type == "start":
        from main import version
        print(f"""
    ╔═══════════════════════╗
    ║    Bookbot! v{version}    ║
    ║                       ║
    ║ Please provide a path ║
    ║ or use 'exit' to exit ║
    ╠═══════════════════════╝
    ║""")

    # exit
    elif type == 'quickexit':
        print("""
    ╔═══════════════════════╗
    ║        Bookbot!       ║
    ║                       ║
    ║        Goodbye!       ║
    ╚═══════════════════════╝""")
    
    elif type == 'select-modal':
        print("""    
    ╔══════════════════════════════════╗
    ║             Bookbot              ║
    ║      Select operation mode       ║
    ║                                  ║
    ║ The default_run_mode file also   ║
    ║   works to choose this option!   ║
    ║   1 - Console   ║   2 - Window   ║
    ╠══════════════════════════════════╝""")
    
    elif type == 'window-running':
        print("""    
    ╔══════════════════════════════════╗
    ║             Bookbot              ║
    ║    Is running in window mode     ║
    ║ Swap to the new window to use it ║
    ╚══════════════════════════════════╝""")
    
    elif type == 'help':
         print("""    
    ╔══════════════════════════════════╗
    ║                Help              ║
    ║                                  ║
    ║ command(shortcuts) - use         ║
    ║                                  ║
    ║ help(h) - displays this menu     ║
    ║ quit(exit, q, x) - quit Bookbot  ║
    ║ options(opt) - display options   ║
    ║                                  ║
    ║    Use return(rt) to go back     ║
    ╚══════════════════════════════════╝
""")
         while True:
                inp = input()
                if inp == 'return' or inp == 'rt' or inp == 'q' or inp == 'x':
                    send_greeting('start')
                    break
                else:
                     send_greeting('help')

    # options
    elif type == 'options':
            print(
"""    ║
    ║                       Options                       
    ║
    ║ Changes are saved after exiting! (use rt/return)
    ║ If options are missing or not working correctly
    ║ try using 'reset' to reset options to default.
    ║
    ║ Type option name to toggle:
    ║                                                     """)
    
    # else it's an error
    else:
        raise TypeError
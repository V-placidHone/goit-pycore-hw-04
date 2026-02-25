import sys
from pathlib import Path
from colorama import init, Fore, Style

colorama.init( autoreset=True)


def show(path_obj: Path):
    if not path_obj.is_dir():
        print("передано не правильний шлях до директорії")
        return
    
    output = ""

    #printing first directory name
    output += f"|{Fore.BLUE} FOLDER:  {path_obj.name}\n{Style.RESET_ALL}"
    

    for item in path_obj.iterdir():
        output += "__"
        if item.is_dir():
            output += f"|{Fore.BLUE} FOLDER:  {item.name}\n{Style.RESET_ALL}"
            show(item)
            
        elif item.is_file():
            output += f"|{Fore.MAGENTA} FILE: {item.name}\n{Style.RESET_ALL}"
            
            
    print(output)
    


if __name__ == "__main__":
    """try:
        path_obj = sys.argv[1]
    except IndexError:
        print("передано не правильний шлях до директорії")
"""

    #WHEN Adding Path object to work only absolute path does work
    path_obj = Path("/Users/WorkVH/Documents/Study")
    show(path_obj)
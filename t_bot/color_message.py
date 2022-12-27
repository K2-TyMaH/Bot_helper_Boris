
def color_message(message: str, color: str) -> str:

    # general message - blue
    # error messages - red
    # neutral message - yellow
    # successful messages - green
    # chossing messages - purple
    # hello and good buy message - blie bold
    

    color_code = {
        "blue_bold": "\033[1m\033[34m{}\033[0m",
        "green": "\033[32m{}\033[0m",
        "yellow": "\033[33m{}\033[0m",
        "red": "\033[31m{}\033[0m",
        "blue": "\033[34m{}\033[0m",
        "purple": "\033[35m{}\033[0m",
        "turquoise": "\033[36m{}\033[0m"
        }
    return color_code[color].format(message)  
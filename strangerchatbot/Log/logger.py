from datetime import datetime

def log(msg):
    f = open("logs.txt", "a+")
    f.write(f'{datetime.now()} -- {msg}\n')
    f.close()


def all_exception_handler():
    import traceback
    log(traceback.format_exc() + "\n######")

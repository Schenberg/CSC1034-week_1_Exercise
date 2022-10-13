def error_prone():
    return(10/0)

def handle_error():
    try:
        error_prone()
    except(ZeroDivisionError):
       print("something was wrong.")
def not_handle_error():
    return error_prone()

if True:
    handle_error()
else:
    not_handle_error()
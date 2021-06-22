from functools import wraps

def logit(logfile='out.log'):
    def logging_decorator(func):

        def wrapped_function(*args, **kwargs):
            __name__=func.__name__
            log_string=func.__name__+" was called"
            print(log_string)
            # 打开logfile，并写入内容
            with open(logfile, 'a') as opened_file:
                # 现在将日志打到指定的logfile
                opened_file.write(log_string+'\n')
            return func(*args, **kwargs)

        return wrapped_function

    return logging_decorator

@logit()
def a(b:int):
    return b
    pass




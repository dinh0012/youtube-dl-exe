class MyLogger(object):
    def debug(self, msg):
        print("debug,", msg)

    def warning(self, msg):
        print("warning,",msg)

    def error(self, msg):
        print("error,",msg)
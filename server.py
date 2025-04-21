# release: nuitka server.py --onefile


if __name__ == '__main__':
    import os
    os.system("python -m http.server --bind 127.0.0.1 --directory ./web")
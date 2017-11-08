import subprocess, time


if(__name__ == "__main__"):
    subprocess.call(["jekyll", "serve"])
    time.sleep(2)
    subprocess.call(["firefox", "http://127.0.0.1:4000"])


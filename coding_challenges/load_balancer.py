import threading

class LoadBalancer:
    def __init__(self):
        self.storage = dict()
        self.lock = threading.Lock()
        self.current_index = 0

    def add_server(self, server_id: str, address: str, port: int) -> None:
        with self.lock:
            if server_id not in self.storage:
                self.storage[server_id] = (address, port)

    def remove_server(self, server_id: str) -> None:
        with self.lock:
            if server_id not in self.storage:
                raise RuntimeError(f"No such server: {server_id}")
            else:
                del self.storage[server_id]
                if self.current_index >= len(self.storage):
                    self.current_index = 0

    def get_server(self) -> (str, int):
        with self.lock:
            if len(self.storage) == 0:
                return '', 0

            servers = list(self.storage.values())
            selected_server = servers[self.current_index]

            self.current_index = (self.current_index + 1) % len(servers)
            return selected_server

    def list_servers(self) -> list:
        with self.lock:
            return list(self.storage.keys())

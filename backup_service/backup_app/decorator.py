#Decorator Pattern

class StorageDecorator(StorageService):
    def __init__(self, wrapped_service):
        self._wrapped_service = wrapped_service

    def store_file(self, file_path):
        # Lógica adicional antes de almacenar el archivo
        self._wrapped_service.store_file(file_path)
        # Lógica adicional después de almacenar el archivo

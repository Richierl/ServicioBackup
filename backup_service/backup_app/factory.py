#Factory Method Pattern

from abc import ABC, abstractmethod

class StorageService(ABC):
    @abstractmethod
    def store_file(self, file_path):
        pass

class GoogleDriveService(StorageService):
    def store_file(self, file_path):
        # Lógica para almacenar el archivo en Google Drive
        pass

class AmazonS3Service(StorageService):
    def store_file(self, file_path):
        # Lógica para almacenar el archivo en Amazon S3
        pass

def create_storage_service(service_name):
    if service_name == 'google_drive':
        return GoogleDriveService()
    elif service_name == 'amazon_s3':
        return AmazonS3Service()
    else:
        raise ValueError('Servicio de almacenamiento no válido')

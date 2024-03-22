#Strategy Pattern

class BackupStrategy(ABC):
    @abstractmethod
    def backup(self):
        pass

class FullBackupStrategy(BackupStrategy):
    def backup(self):
        # Lógica para respaldo completo
        pass

class IncrementalBackupStrategy(BackupStrategy):
    def backup(self):
        # Lógica para respaldo incremental
        pass

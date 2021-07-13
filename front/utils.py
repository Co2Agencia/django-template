from django.core.files.storage import FileSystemStorage

class OverwriteStorage(FileSystemStorage):
    # Devuelve el mismo nombre para los archivos que ya existen
    # y elimina los archivos existententes al guardarlos.
    def _save(self, name, content):
        if self.exists(name):
            self.delete(name)
        return super(OverwriteStorage, self)._save(name, content)

    def get_available_name(self, name, max_length=None):
        
        return name
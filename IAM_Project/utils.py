import hashlib

admin_password_hash = hashlib.sha256('admin123'.encode()).hexdigest()
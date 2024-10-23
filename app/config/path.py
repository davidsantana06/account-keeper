from pathlib import Path


_ROOT_DIR = Path(__file__).resolve().parent.parent.parent
''' / '''

STORAGE_DIR = _ROOT_DIR / 'storage'
''' /storage '''

DATABASE_FILE = STORAGE_DIR / 'database.sqlite3'
''' /storage/database.sqlite3 '''

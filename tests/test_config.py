import os
import unittest
from config.config import Config
  # Importujemy główną klasę konfiguracji

class TestConfig(unittest.TestCase):
    def test_env_variables_loaded(self):
        # Sprawdzamy, czy zmienne środowiskowe są poprawnie załadowane z pliku .env
        self.assertIsNotNone(os.getenv('DATABASE_URL'), "DATABASE_URL nie jest ustawiona")
        self.assertIsNotNone(os.getenv('DEBUG'), "DEBUG nie jest ustawione")
        self.assertIsNotNone(os.getenv('SECRET_KEY'), "SECRET_KEY nie jest ustawiony")

    def test_config_database_url(self):
        # Sprawdzamy, czy DATABASE_URL w konfiguracji jest zgodny z oczekiwaną wartością
        config_value = Config.DATABASE_URL
        expected_value = os.getenv('DATABASE_URL')
        self.assertEqual(config_value, expected_value, "DATABASE_URL nie jest poprawna")

    def test_config_debug(self):
        # Sprawdzamy, czy DEBUG w konfiguracji jest zgodne z wartością z .env
        config_value = Config.DEBUG
        expected_value = os.getenv('DEBUG') == 'True'
        self.assertEqual(config_value, expected_value, "DEBUG nie jest poprawne")

    def test_config_secret_key(self):
        # Sprawdzamy, czy SECRET_KEY w konfiguracji jest zgodny z oczekiwaną wartością
        config_value = Config.SECRET_KEY
        expected_value = os.getenv('SECRET_KEY')
        self.assertEqual(config_value, expected_value, "SECRET_KEY nie jest poprawny")

if __name__ == '__main__':
    unittest.main()

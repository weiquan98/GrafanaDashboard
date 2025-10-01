# test_grafanadashboard.py
"""
Tests for GrafanaDashboard module.
"""

import unittest
from grafanadashboard import GrafanaDashboard

class TestGrafanaDashboard(unittest.TestCase):
    """Test cases for GrafanaDashboard class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = GrafanaDashboard()
        self.assertIsInstance(instance, GrafanaDashboard)
        
    def test_run_method(self):
        """Test the run method."""
        instance = GrafanaDashboard()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

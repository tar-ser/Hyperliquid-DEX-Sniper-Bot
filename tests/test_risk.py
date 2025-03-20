import unittest

class TestRiskManager(unittest.TestCase):
    def setUp(self):
        self.rm = RiskManager(100_000)
        
    def test_position_size(self):
        self.assertTrue(self.rm.can_open_position(2000, 50))  # 2% of 100k
        self.assertFalse(self.rm.can_open_position(3000, 50)) # 3% > limit
        
    def test_daily_loss(self):
        self.rm.update_after_trade(-4500)
        self.assertAlmostEqual(self.rm.daily_loss, 4500)
        self.assertFalse(self.rm.can_open_position(1000, 100))

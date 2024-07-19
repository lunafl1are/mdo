import unittest
import aerodynamics

class TestAerodynamicsSolver(unittest.TestCase):
  
  def test_wing_area(self):
    result = aerodynamics.mixed_wing_area(2,2,4,5)
    self.assertEqual(result, 18)

  def test_wing_area_with_equal_taper(self):
    result = aerodynamics.mixed_wing_area(1,1,1,0)
    self.assertEqual(result, 1)
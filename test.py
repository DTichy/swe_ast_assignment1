import unittest
from moon import Moon

class TestMoon(unittest.TestCase):

    def test_phobos_rise_and_set_before_deimos(self):
        """
        Phobos  |---------|
        Deimos               |---------|
        Overlap X
        """
        phobos, deimos = Moon(1,0,2,0,'Phobos'), Moon(3,0,4,0,'Deimos')
        self.assertEqual(phobos.calculate_overlap_time(deimos),0)

    def test_phobos_rise_before_deimos_deimos_set_after_phobos(self):
        """
        Phobos  |---------|
        Deimos      |---------|
        Overlap     |-----|
        """
        phobos, deimos = Moon(1,0,4,0,'Phobos'), Moon(3,0,5,0,'Deimos')
        self.assertEqual(phobos.calculate_overlap_time(deimos),100)    



    def test_phobos_rise_before_deimos_phobos_set_after_deimos(self):
        """
        Phobos   |---------|
        Deimos      |---|
        Overlap     |---|
        """
        phobos, deimos  = Moon(1,0,4,0,'Phobos'), Moon(2,0,3,0,'Deimos')
        self.assertEqual(phobos.calculate_overlap_time(deimos),100) 


    def test_phobos_rise_before_deimos_phobos_set_after_deimos_phobos_set_after_midnight(self):
        """
        Zero               |
        Phobos  |------------|
        Deimos    |------|
        Overlap   |------|
        """
        phobos, deimos = Moon(22,0,1,0,'Phobos'), Moon(23,0,24,0,'Deimos')
        self.assertEqual(phobos.calculate_overlap_time(deimos),100) 

    def test_phobos_rise_before_phobos_deimos_set_after_phobos_deimos_rise_and_set_after_midnight(self):
        """
        Zero          |
        Phobos  |----------|
        Deimos         |-----|
        Overlap        |---|
        """
        phobos, deimos = Moon(22,0,2,0,'Phobos'), Moon(0,0,1,0,'Deimos')
        self.assertEqual(phobos.calculate_overlap_time(deimos),100)

    def test_phobos_rise_after_deimos_deimos_set_after_phobos_deimos_and_phobos_set_after_midnight(self):
        """
        Zero          |
        Phobos     |----|
        Deimos   |---------|
        Overlap    |----|
        """
        phobos, deimos = Moon(22,0,2,0,'Phobos'), Moon(23,0,1,0,'Deimos')
        self.assertEqual(phobos.calculate_overlap_time(deimos),300)


    def test_deimos_set_at_same_time_as_phobos_rise(self):
        """
        Phobos   |----| 
        Deimos        |----|
        Overlap       |
        """
        phobos, deimos = Moon(11,0,12,0,'Phobos'), Moon(12,0,13,0,'Deimos')
        self.assertEqual(phobos.calculate_overlap_time(deimos),1)
    
    def test_phobos_set_at_same_time_as_deimos_rise_midnight(self):
        """
        Zero          |
        Phobos   |----| 
        Deimos        |----|   
        Overlap       |
        """
        deimos, phobos = Moon(24,0,0,0,'Phobos'), Moon(0,0,1,0,'Deimos')
        self.assertEqual(phobos.calculate_overlap_time(deimos),1)

    def test_deimos_set_at_same_time_as_phobos_rise_midnight(self):
        """
        Zero          |
        Phobos        |----|
        Deimos   |----|   
        Overlap       |
        """
        phobos, deimos = Moon(24,0,0,0,'Phobos'), Moon(0,0,1,0,'Deimos')
        self.assertEqual(phobos.calculate_overlap_time(deimos),1)


    def test_both_moons_up_the_whole_day(self):
        phobos, deimos = Moon(0,0,24,99,'Phobos'), Moon(0,0,24,99,'Deimos')
        self.assertEqual(phobos.calculate_overlap_time(deimos),2499)

    def test_deimos_and_phobos_overlap_two_times(self):
        """
        Zero            |
        Phobos   ------|     |------- 
        Deimos      |-----------|   
        Overlap     |--|  +  |--|
        """
        phobos, deimos = Moon(15,0,7,0,'Phobos'), Moon(4,0,16,0,'Deimos')
        self.assertEqual(phobos.calculate_overlap_time(deimos),400)
        
    def test_phobos_set_at_same_time_as_deimos_rise(self):
        """
        Phobos        |----| 
        Deimos   |----|
        Overlap       |
        """
        deimos, phobos = Moon(11,0,12,0,'Phobos'), Moon(12,0,13,0,'Deimos')
        self.assertEqual(phobos.calculate_overlap_time(deimos),1)


    def test_deimos_rise_and_set_before_phobos(self):
        """
        Phobos               |---------|
        Deimos   |---------|
        Overlap X
        """
        deimos, phobos = Moon(1,0,2,0,'Phobos'), Moon(3,0,4,0,'Deimos')
        self.assertEqual(phobos.calculate_overlap_time(deimos),0)


    def test_deimos_rise_before_phobos_phobos_set_after_deimos(self):
        """
        Phobos       |---------|
        Deimos  |---------|
        Overlap     |-----|
        """
        deimos, phobos = Moon(1,0,4,0,'Phobos'), Moon(3,0,5,0,'Deimos')
        self.assertEqual(phobos.calculate_overlap_time(deimos),100)  


    def test_deimos_rise_before_phobos_deimos_set_after_phobos(self):
        """
        Phobos      |---|
        Deimos    |-------|
        Overlap     |---|
        """
        deimos, phobos  = Moon(1,0,4,0,'Phobos'), Moon(2,0,3,0,'Deimos')
        self.assertEqual(phobos.calculate_overlap_time(deimos),100) 

if __name__ == '__main__':
    unittest.main()
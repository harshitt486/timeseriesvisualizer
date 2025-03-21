import unittest
from time_series_visualizer import draw_line_plot, draw_bar_plot, draw_box_plot

class TestVisualizer(unittest.TestCase):
    def test_line_plot(self):
        self.assertTrue(draw_line_plot())

    def test_bar_plot(self):
        self.assertTrue(draw_bar_plot())

    def test_box_plot(self):
        self.assertTrue(draw_box_plot())

if __name__ == "__main__":
    unittest.main()

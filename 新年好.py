from manimlib import *
from os import system
# from numpy import *


class FunctionGraphSin(Scene):
    @staticmethod
    def func(x):
        y = 0.64*np.sqrt(abs(x)) #- 0.8 + 1.2^abs(x) * np.cos(200*x)) * np.sqrt(np.cos(x))
        return np.array([x,y])
    def construct(self):
        axes = Axes(
            x_range=[-1, 7, 1],
            y_range=[-2, 2, 1],
            width=8,
            height=4,
            axis_config={
                "include_tip": True,
            }
        )

        graph = ParametricCurve(
            t_func= self.func,
            x_range = [-np.pi / 2, np.pi / 2, 1])
        graph.move_to(axes.get_origin(), aligned_edge=LEFT)

        self.play(Write(axes), run_time=1)
        self.play(Write(graph), run_time=1)
        self.wait()

from manim import *


SCALE_FACTOR =0.7
tmp_pixel_height = config.pixel_height
config.pixel_height= config.pixel_width
config.pixel_width= tmp_pixel_height
# Change coord system dimensions
config.frame_height = config.frame_height/SCALE_FACTOR
config.frame_width = config.frame_height* 9/16
FRAME_HEIGHT = config.frame_height
FRAME_WTDTH = config.frame_width

class IntegralExponencial(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width=FRAME_WTDTH,
                height=FRAME_HEIGHT,
                color=BLACK)
            self.add(self.border)

    def construct(self):
        self.camera.background_color = BLACK
        texto0 = Text("Solve Doubts", color=YELLOW).move_to(np.array([-2.2, 5.3, 0])).scale(0.46)
        eqn000 = MathTex(r"\text{Calcular}\,\displaystyle\int 3^{x}e^{x}\,dx", color=YELLOW).move_to(np.array([-1,4,0])).scale(1)
        eqn00 = MathTex(r"\displaystyle\int 3^{x}e^{x}\,dx", color=YELLOW).move_to(np.array([0,4,0])).scale(1)
        eqn0 = MathTex(r"\displaystyle\int 3^{x}e^{x}\,dx").move_to(np.array([-2, 2.5, 0])).scale(1)
        eqn1 = MathTex(r"\displaystyle=\int (3e)^{x}\,dx").move_to(np.array([0.5, 2.5, 0])).scale(1)
        eqn2 = MathTex(r"\displaystyle =\frac{(3e)^{x}}{\ln(3e)}+C").move_to(np.array([0.5,1, 0])).scale(1)
        eqn3 = MathTex(r"\displaystyle=\frac{3^{x}e^{x}}{\ln(3e)}+C").move_to(np.array([0.4, -0.5, 0])).scale(1)
        eqn4 = MathTex(r"\displaystyle=\frac{3^{x}e^{x}}{\ln(3)+\ln(e)}+C").move_to(np.array([0.95, -2, 0])).scale(1)
        eqn5 = MathTex(r"\displaystyle=\frac{3^{x}e^{x}}{\ln(3)+1}+C").move_to(np.array([0.6, -3.5, 0])).scale(1)
        
        self.play(GrowFromCenter(texto0))
        self.wait(0.2)
        self.play(Write(eqn000))
        self.wait(1)
        self.play(Write(eqn00))
        self.wait(0.001)
        self.play(Transform(eqn00, eqn0))
        self.wait(0.3)
        self.play(Write(eqn0))
        self.wait(0.3)
        self.play(Transform(eqn00, eqn1))
        self.wait(0.3)
        self.play(Write(eqn1))
        self.wait(0.3)
        self.play(Transform(eqn00, eqn2))
        self.wait(0.3)
        self.play(Write(eqn2))
        self.wait(0.3)
        self.play(Transform(eqn00,eqn3))
        self.wait(0.3)
        self.play(Write(eqn3))
        self.wait(0.3)
        self.play(Transform(eqn00,eqn4))
        self.wait(0.3)
        self.play(Write(eqn4))
        self.wait(0.3)
        self.play(Transform(eqn00,eqn5))
        self.wait(2)


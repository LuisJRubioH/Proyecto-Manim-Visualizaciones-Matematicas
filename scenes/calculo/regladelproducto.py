from manim import*

SCALE_FACTOR =0.6
tmp_pixel_height = config.pixel_height
config.pixel_height= config.pixel_width
config.pixel_width= tmp_pixel_height
# Change coord system dimensions
config.frame_height = config.frame_height/SCALE_FACTOR
config.frame_width = config.frame_height* 9/16
FRAME_HEIGHT = config.frame_height
FRAME_WTDTH = config.frame_width

class ReglaDelProducto(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width=FRAME_WTDTH,
                height=FRAME_HEIGHT,
                color=BLACK)
            self.add(self.border)
    def construct(self):
        #sonido del video
        self.add_sound("derivada1.mp3")
        
        cielo = "#C4DDFF"
        azul = "#33FFFF"
        verde = "#00FF00"
        rojo = "#B20600"
        color1 = "#66FF00"
        color2 = "#CD1818"
        color3 = "#F3950D"
        color4 = "#F4E185"
        color5 = "#873600"
        color6 = "#33FFFF"
        
        
        self.camera.background_color = BLACK
        texto0 = MathTex(r"Solv\epsilon-\delta oubts").set_color_by_gradient(color3, color5, color2, color3,color4).move_to(np.array([-2, 6, 0])).scale(0.8)
        texto01 = MathTex(r"Solv\epsilon-\delta oubts").set_color_by_gradient(color3, color5, color2, color3, color4).move_to(np.array([0, -5.7, 0])).scale(1)
        texto00 = MathTex(r"\text{Derivación: Regla del producto}}", color=YELLOW).move_to(np.array([0, 5, 0])).scale(0.6)
        text=MathTex( "\\frac{d}{dx}[f(x)g(x)]=","\\frac{d}{dx}[f(x)]g(x)","+","f(x)\\frac{d}{dx}[g(x)]", color=verde).move_to(np.array([0, 2.7, 0])).scale(0.6)
        texto1 = MathTex(r"\text{La derivada del producto de dos funciones es igual a}").move_to(np.array([0, 4.5, 0])).scale(0.6)
        texto2 = MathTex(r"\text{la derivada de la primera por la segunda función}").move_to(np.array([0, 4.1, 0])).scale(0.6)
        texto3 = MathTex(r"\text{mas la primera función por la derivada de la segunda}").move_to(np.array([0, 3.7, 0])).scale(0.6)
        
        self.add(texto0)
        self.add(texto01)
        self.play(Write(texto00))
        
        framebox1 = SurroundingRectangle(text[0], buff = .1)
        framebox2 = SurroundingRectangle(text[1], buff = .1)
        framebox3 = SurroundingRectangle(text[3], buff=.1)
        framebox = SurroundingRectangle(text, buff=.1)
        
        self.add((texto1),(texto2),(texto3))
        self.play(Write(text))
        self.wait(0.001)
        self.play(Create(framebox1))
        self.wait(0.001)
        self.play(Transform(framebox1, framebox2))
        self.wait(0.001)
        self.play(Transform(framebox1, framebox3))
        self.wait(0.001)
        self.remove(framebox1)
        self.wait(0.001)
        self.play(Create(framebox))
        self.wait(0.001)
        
        ejemplo1 = MathTex(r"\text{Ejemplo: Calcular }\displaystyle \frac{d}{dx}[5x^3\sqrt{x}]",color=YELLOW).move_to(np.array([-1, 1.7, 0])).scale(0.6)
        self.add(ejemplo1)
        self.wait(0.001)
        sol= MathTex(r"\text{Solución}").move_to(np.array([-2.5, 1.2, 0])).scale(0.6)
        self.add(sol)
        self.wait(0.001)
        
        sol1 = MathTex(r"\displaystyle\frac{d}{dx}[5x^3\sqrt{x}]",r"=",r"\displaystyle\frac{d}{dx}[5x^3]",r"\sqrt{x}", r"+",r"5x^3", r"\displaystyle\frac{d}{dx}[\sqrt{x}]").move_to(np.array([0.5,0.5, 0])).scale(0.6)
        sol1[0].set_color(color=WHITE)
        sol1[1].set_color(color=WHITE)
        sol1[2].set_color(color=color6)
        sol1[3].set_color(color=WHITE)
        sol1[4].set_color(color=RED)
        sol1[5].set_color(color=WHITE)
        sol1[6].set_color(color=color6)
        
        self.add(sol1[0])
        self.wait(0.001)
        self.play(Write(sol1[1]))
        self.wait(0.001)
        self.play(Write(sol1[2]))
        self.wait(0.001)
        self.play(Write(sol1[3]))
        self.wait(0.001)
        self.play(Write(sol1[4]))
        self.wait(0.001)
        self.play(Write(sol1[5]))
        self.wait(0.001)
        self.play(Write(sol1[6]))
        self.wait(0.001)
        
        sol1_1 = MathTex(r"\displaystyle\frac{d}{dx}[5x^3\sqrt{x}]", r"=", r"\displaystyle\frac{d}{dx}[5x^3]", r"\sqrt{x}", r"+", r"5x^3",r"\frac{d}{dx}[\sqrt{x}]").move_to(np.array([0.5, 0.5, 0])).scale(0.6)
        sol1_1[0].set_color(color=WHITE)
        sol1_1[1].set_color(color=WHITE)
        sol1_1[2].set_color(color=color6)
        sol1_1[3].set_color(color=WHITE)
        sol1_1[4].set_color(color=RED)
        sol1_1[5].set_color(color=WHITE)
        sol1_1[6].set_color(color=color6)
        
        self.add((sol1_1[0]),(sol1_1[1]),(sol1_1[2]),(sol1_1[3]),(sol1_1[4]),(sol1_1[5]),(sol1_1[6]))
        
        sol2 = MathTex(r"\displaystyle\frac{d}{dx}[5x^3\sqrt{x}]",r"=",r"(15x^2)",r"\sqrt{x}",r"+",r"5x^3",r"\left(\frac{1}{2\sqrt{x}}\right)").move_to(np.array([0.5, -0.7, 0])).scale(0.6)
        sol2[0].set_color(color=WHITE)
        sol2[1].set_color(color=WHITE)
        sol2[2].set_color(color=color6)
        sol2[3].set_color(color=WHITE)
        sol2[4].set_color(color=RED)
        sol2[5].set_color(color=WHITE)
        sol2[6].set_color(color=color6)
        
        self.wait(0.001)
        self.add(sol2[0])
        self.wait(0.001)
        self.play(Write(sol2[1]))
        self.wait(0.001)
        self.play(Write(sol1[2]))
        self.wait(0.001)
        self.play(Transform(sol1[2],sol2[2]))
        self.wait(0.001)
        self.play(Write(sol2[3]))
        self.wait(0.001)
        self.play(Write(sol2[4]))
        self.wait(0.001)
        self.play(Write(sol2[5]))
        self.wait(0.001)
        self.play(Write(sol1[6]))
        self.wait(0.001)
        self.play(Transform(sol1[6], sol2[6]))
        self.wait(0.001)
        
        sol2_2 = MathTex(r"\displaystyle\frac{d}{dx}[5x^3\sqrt{x}]", r"=", r"(15x^2)", r"\sqrt{x}", r"+", r"5x^3",r"\left(\frac{1}{2\sqrt{x}}\right)").move_to(np.array([0.5, -0.7, 0])).scale(0.6)
        sol2_2[0].set_color(color=WHITE)
        sol2_2[1].set_color(color=WHITE)
        sol2_2[2].set_color(color=color6)
        sol2_2[3].set_color(color=WHITE)
        sol2_2[4].set_color(color=RED)
        sol2_2[5].set_color(color=WHITE)
        sol2_2[6].set_color(color=color6)
        
        self.add((sol2_2[0]),(sol2_2[1]),(sol2_2[2]),(sol2_2[3]),(sol2_2[4]),(sol2_2[5]),(sol2_2[6]))
        self.wait(0.001)
        
        sol3 = MathTex(r"\displaystyle\frac{d}{dx}[5x^3\sqrt{x}]", r"=", r"(15x^2)", r"x^{1/2}", r"+","{{5x^3}","\\over","{2x^{1/2}}}").move_to(np.array([0.1, -1.7, 0])).scale(0.6)
        sol3[0].set_color(color=WHITE)
        sol3[1].set_color(color=WHITE)
        sol3[2].set_color(color=WHITE)
        sol3[3].set_color(color=WHITE)
        sol3[4].set_color(color=RED)
        sol3[5].set_color(color=WHITE)
        sol3[6].set_color(color=WHITE)
        sol3[7].set_color(color=WHITE)
        
        self.wait(0.001)
        self.add(sol3[0])
        self.wait(0.001)
        self.play(Write(sol3[1]))
        self.wait(0.001)
        self.play(Write(sol3[2]))
        self.wait(0.001)
        self.play(Write(sol2[3]))
        self.wait(0.001)
        self.play(Transform(sol2[3], sol3[3]))
        self.wait(0.001)
        self.play(Write(sol3[4]))
        self.wait(0.001)
        self.play(Write(sol2[5]))
        self.wait(0.001)
        self.play(Write(sol3[5]))
        self.wait(0.001)
        self.play(Transform(sol2[5],sol3[6]))
        self.wait(0.001)
        self.play(Write(sol2[6]))
        self.wait(0.001)
        self.play(Transform(sol2[6],sol3[7]))
        self.wait(0.001)
        
        sol4 = MathTex(r"\displaystyle\frac{d}{dx}[5x^3\sqrt{x}]", r"=", r"15x^{5/2}", r"+", r"\frac{5}{2}x^{5/2}").move_to(np.array([-0.15, -2.7, 0])).scale(0.6)
        sol4[0].set_color(color=WHITE)
        sol4[1].set_color(color=WHITE)
        sol4[2].set_color(color=WHITE)
        sol4[3].set_color(color=WHITE)
        sol4[4].set_color(color=WHITE)
        
        self.add(sol4[0])
        self.wait(0.001)
        self.play(Write(sol4[1]))
        self.wait(0.001)
        self.play(Write(sol4[2]))
        self.wait(0.001)
        self.play(Write(sol4[3]))
        self.wait(0.001)
        self.play(Write(sol4[4]))
        self.wait(0.001)
        
        sol5 = MathTex(r"\displaystyle\frac{d}{dx}[5x^3\sqrt{x}]", r"=",r"\frac{35}{2}x^{5/2}").move_to(np.array([-0.65, -3.7, 0])).scale(0.6)
        sol5[0].set_color(color=WHITE)
        sol5[1].set_color(color=WHITE)
        sol5[2].set_color(color=WHITE)
        
        self.add(sol5[0])
        self.wait(0.001)
        self.play(Write(sol5[1]))
        self.wait(0.001)
        self.play(Write(sol5[2]))
        self.wait(5)



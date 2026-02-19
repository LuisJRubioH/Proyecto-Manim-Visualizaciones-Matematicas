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
class superficies(ThreeDScene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width=FRAME_WTDTH,
                height=FRAME_HEIGHT,
                color=BLACK)
            self.add(self.border)

    def construct(self):
        cielo="#C4DDFF"
        azul= "#33FFFF"
        verde = "#00FF00"
        rojo= "#B20600"
        color1 = "#66FF00"
        color2 = "#CD1818"
        color3 = "#F3950D"
        color4 = "#F4E185"
        color5 = "#873600"
        self.camera.background_color=BLACK
        texto0 = MathTex(r"Solv\epsilon-\delta oubts").set_color_by_gradient(color3, color5, color2, color3,color4).move_to(np.array([0,-5.5, 0])).scale(0.8)
        texto00 = MathTex(r"\text{Superficies:Graficas en 3D}}",color=YELLOW).move_to(np.array([0, 5, 0])).scale(1)
        axes=ThreeDAxes().scale(0.75)
        x=MathTex(r"x").move_to(np.array([2,0.5,0]))
        y=MathTex(r"y").move_to(np.array([0.5, 2, 0]))
        self.set_camera_orientation(phi=65*DEGREES, theta=30*DEGREES)
        s6 = MathTex(r"\displaystyle{\frac{x^2}{a^2}+\frac{y^2}{b^2}-\frac{z^2}{c^2}}=1").move_to(
            np.array([0, -4, 0]))
        texto6 = MathTex(r"\text{Hiperboloide de dos hojas}", color=YELLOW).move_to(np.array([0, 4, 0]))
        doshojas = Surface(lambda u, v: np.array([
            0.6*(u**2-1)*np.cos(v),
            0.6*(u**2-1)*np.sin(v),
            u]),
                        u_range=[-1,1],
                        v_range=[0,2*PI],
                        resolution=(15,3))
        doshojas.set_fill_by_checkerboard(color1,color1 , opacity=0.75)
        self.add_fixed_in_frame_mobjects(texto0)
        self.wait(1)
        self.add_fixed_in_frame_mobjects(texto00)
        self.wait(1)
        self.add_fixed_in_frame_mobjects(texto6,s6)
        self.wait(1)
        self.play(Write(axes))
        self.wait(1)
        self.play(Write(doshojas))
        self.wait(1)


class superficies1(ThreeDScene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width=FRAME_WTDTH,
                height=FRAME_HEIGHT,
                color=BLACK)
            self.add(self.border)
    def construct(self):
        cielo="#C4DDFF"
        azul= "#33FFFF"
        verde = "#00FF00"
        rojo= "#B20600"
        color1 = "#66FF00"
        color2 = "#CD1818"
        color3 = "#F3950D"
        color4 = "#F4E185"
        color5 = "#873600"
        self.camera.background_color=BLACK
        texto0 = MathTex(r"Solv\epsilon-\delta oubts").set_color_by_gradient(color3, color5, color2, color3,color4).move_to(np.array([-2,6, 0])).scale(0.7)
        texto01 = MathTex(r"Solv\epsilon-\delta oubts").set_color_by_gradient(color3, color5, color2, color3,color4).move_to(np.array([0, -5.5, 0])).scale(1)
        texto00 = MathTex(r"\text{Superficies: Graficas en 3D}}",color=YELLOW).move_to(np.array([0, 5, 0])).scale(1)
        axes=ThreeDAxes().scale(0.75)
        x=MathTex(r"x").move_to(np.array([2,0.5,0]))
        y=MathTex(r"y").move_to(np.array([0.5, 2, 0]))
        self.set_camera_orientation(phi=65*DEGREES, theta=30*DEGREES)
        s1=MathTex(r"x^2+y^2+z^2=\rho^2").move_to(np.array([0,-4,0]))
        texto1 = MathTex(r"\text{Esfera}", color=YELLOW).move_to(np.array([0, 4, 0]))
        esfera=Surface(lambda u,v:np.array([
        1.3*np.cos(v)*np.sin(u),
        1.3*np.sin(v)*np.sin(u),
        1.3*np.cos(u)]),
        u_range=[-PI,PI],
        v_range=[0, 2*PI],
        resolution=(5,32))
        esfera.set_fill_by_checkerboard(azul,azul,opacity=0.75)
        s2 = MathTex(r"x^2+y^2=r^2").move_to(np.array([0, -4, 0]))
        texto2 = MathTex(r"\text{Cilíndro}", color = YELLOW ).move_to(np.array([0, 4, 0])).scale(1)
        cilindro = Surface(lambda u, v: np.array([
            1.3 * np.cos(v),
            1.3 * np.sin(v),
            1.3* np.cos(u)]),
            u_range=[-PI, PI],
            v_range=[0, 2 * PI],
            resolution=(5, 32))
        cilindro.set_fill_by_checkerboard(verde,verde, opacity=0.75)
        s3 = MathTex(r"\displaystyle{\frac{x^2}{a^2}+\frac{y^2}{b^2}+\frac{z^2}{c^2}}=1").move_to(np.array([0, -4, 0]))
        texto3 = MathTex(r"\text{Elipsoide}", color=YELLOW).move_to(np.array([0, 4, 0]))
        elipsoide = Surface(lambda u, v: np.array([
            2 * np.cos(v) * np.sin(u),
            1.3 * np.sin(v) * np.sin(u),
            1.2 * np.cos(u)]),
                         u_range=[-PI, PI],
                         v_range=[0, 2 * PI],
                         resolution=(5, 32))
        elipsoide.set_fill_by_checkerboard(color1,color1, opacity=0.75)
        s4 = MathTex(r"z=x^2+y^2").move_to(np.array([0, -4, 0]))
        texto4 = MathTex(r"\text{Paraboloide}", color=YELLOW).move_to(np.array([0, 4, 0]))
        paraboloide = Surface(lambda u, v: np.array([
            1.3 * np.cos(v) * np.sin(u),
            1.3 * np.sin(v) * np.sin(u),
            1.69 * np.sin(u)**2]),
                         u_range=[-PI, PI],
                         v_range=[0, 2 * PI],
                         resolution=(5, 32))
        paraboloide.set_fill_by_checkerboard(color3, color3, opacity=0.75)
        s5 = MathTex(r"z=x^2-y^2").move_to(np.array([0, -4, 0]))
        texto5 = MathTex(r"\text{Hiperboloide o silla de montar}", color=YELLOW).move_to(np.array([0, 4, 0]))
        hiperboloide = Surface(lambda u, v: np.array([
            1.3 * np.cos(v) * np.sin(u),
            1.3 * np.sin(v) * np.sin(u),
            1.69 * ((np.cos(v) * np.sin(u))**2-(np.sin(v) * np.sin(u))**2)]),
                         u_range=[-PI, PI],
                         v_range=[0, 2 * PI],
                         resolution=(5, 32))
        hiperboloide.set_fill_by_checkerboard(color4, color4, opacity=0.75)
        s6 = MathTex(r"\displaystyle{\frac{x^2}{a^2}+\frac{y^2}{b^2}-\frac{z^2}{c^2}}=0").move_to(
            np.array([0, -4, 0]))
        texto6 = MathTex(r"\text{Cono eliptico}", color=YELLOW).move_to(np.array([0, 4, 0]))
        conoelip = Surface(lambda u, v: np.array([
            1.5 * np.cos(v) * np.sinh(u),
            1.2 * np.sin(v) * np.sinh(u),
            1.2 * u]),
                           u_range=[-1, 1],
                           v_range=[0, 2 * PI],
                           resolution=(5, 32))
        conoelip.set_fill_by_checkerboard(color2, color2, opacity=0.75)
        s7 = MathTex(r"\displaystyle{\frac{x^2}{a^2}+\frac{y^2}{b^2}-\frac{z^2}{c^2}}=1").move_to(
            np.array([0, -4, 0]))
        texto7 = MathTex(r"\text{Hiperboloide de una hojas}", color=YELLOW).move_to(np.array([0, 4, 0]))
        hiper1h = Surface(lambda u, v: np.array([
            0.6 * np.cos(v) * np.cosh(u / 0.6),
            0.6 * np.sin(v) * np.cosh(u / 0.6),
            u]),
                           u_range=[-1, 1],
                           v_range=[0, 2 * PI],
                           resolution=(5, 32))
        hiper1h.set_fill_by_checkerboard(color1, color1, opacity=0.75)
        self.begin_ambient_camera_rotation(rate=0.5)
        self.add_fixed_in_frame_mobjects(texto0,texto01)
        self.wait(0.1)
        self.add_fixed_in_frame_mobjects(texto00)
        self.wait(0.1)
        self.add_fixed_in_frame_mobjects(texto1)
        self.wait(0.1)
        self.play(Write(axes))
        self.wait(1)
        self.add_fixed_in_frame_mobjects(s1)
        self.wait(1)
        self.play(Write(esfera))
        self.wait(1)
        self.play(FadeOut(texto1),FadeOut(s1))
        self.wait(0.1)
        self.add_fixed_in_frame_mobjects(texto2,s2)
        self.play(Transform(esfera,cilindro))
        self.wait(1)
        self.play(FadeOut(texto2), FadeOut(s2))
        self.wait(0.1)
        self.add_fixed_in_frame_mobjects(texto3, s3)
        self.play(Transform(esfera, elipsoide))
        self.wait(1)
        self.play(FadeOut(texto3), FadeOut(s3))
        self.wait(0.1)
        self.add_fixed_in_frame_mobjects(texto4, s4)
        self.play(Transform(esfera, paraboloide))
        self.wait(1)
        self.play(FadeOut(texto4), FadeOut(s4))
        self.wait(0.1)
        self.add_fixed_in_frame_mobjects(texto5, s5)
        self.play(Transform(esfera, hiperboloide))
        self.wait(1)
        self.play(FadeOut(texto5), FadeOut(s5))
        self.wait(0.1)
        self.add_fixed_in_frame_mobjects(texto6, s6)
        self.play(Transform(esfera, conoelip))
        self.wait(1)
        self.play(FadeOut(texto6), FadeOut(s6))
        self.wait(0.1)
        self.add_fixed_in_frame_mobjects(texto7, s7)
        self.play(Transform(esfera,hiper1h))
        self.wait(2)

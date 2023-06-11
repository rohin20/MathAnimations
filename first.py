from manim import *

class Calc(Scene):
    def construct(self):
        title = Tex("The derivative of $e^{(x)}$")
        basel = MathTex("f(x)={e}^{x}", color=RED)
        
        plane = NumberPlane(
            x_range=[-5,5],
            y_range=[-4,10],
            x_length=6,
            y_length=7,
        
        ).add_coordinates()

        graph1 = plane.plot(
            lambda x: np.e ** x, x_range=[-5,5], color=RED
        )
        graph2 = plane.plot(
            lambda x: np.e ** x, x_range=[-5,5], color=GREEN
        )
        
        k = ValueTracker(-5) #derivative val
        dot1 = always_redraw(
            lambda: Dot().move_to(
                plane.coords_to_point(
                    k.get_value(), graph1.underlying_function(k.get_value()) #x,f(x)

            
                )
            )
        )

        slope1 = always_redraw(
            lambda: plane.get_secant_slope_group(
                x=k.get_value(),
                graph = graph1,
                dx=0.0001,
                secant_line_length=3,
                
                
            )
        )
        
        slope1.set_color(RED)
        VGroup(basel, title).arrange(DOWN)

        self.play(
            FadeIn(title, shift=DOWN),
            run_time = 2
        )
        self.wait()

        self.play(
            FadeOut(title, shift=UP),
            FadeIn(basel, shift=DOWN),
            
        )
        self.wait()
        transform_basel= MathTex("f(x)={e}^{x}", color=RED)
        transform_basel.to_corner(UP+LEFT)

        self.play(
            Transform(basel,transform_basel),
            run_time = 1
        )

     
        

        self.play(
            LaggedStart(DrawBorderThenFill(plane), Create(graph1)),
            run_time = 1.5,
            lag_ratio=1,

        )

        

        self.add(slope1,dot1)
        self.play(
            k.animate.set_value(3), run_time=5, rate_func=linear 

        )
        

        self.wait()

        equation = MathTex("f(x) = f'(x) = e^x", color=GREEN)
        equation.to_corner(UP + LEFT)
        
        

        self.play(
            FadeOut(basel,transform_basel,graph1),
            
            
        )

       
        

        self.play(
            FadeIn(graph2,run_time=1),
            Write(equation),
             
            run_time=3,
        )
        
        self.wait(2)

     

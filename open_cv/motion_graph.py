from video_Capturing import df 

from bokeh.plotting import figure,show,output_file


p = figure(x_axis_type = 'datetime', height = 100, width = 500, reponsive = True, title = "Motion Graph")
p.yaxis.minor_tick_color = None
p.ygrid[0].ticker.desired_num_ticks = 1

q = p.quad(left = df["Start"], right = df["End"], bottom=0, top= 1, color= "green")
output_file("Motion_graph.html")
show(p)
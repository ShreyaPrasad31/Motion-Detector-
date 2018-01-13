from video_Capturing import df 

from bokeh.plotting import figure,show,output_file
from bokeh.models import HoverTool , ColumnDataSource

df["Start_string"] = df["Start"].dt.str.strftime("%Y-%m-%d %H:%M:%S")
df["End_string"] = df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")
cds = ColumnDataSource(df)


p = figure(x_axis_type = 'datetime', height = 100, width = 500, reponsive = True, title = "Motion Graph")
p.yaxis.minor_tick_line_color = None
p.ygrid[0].ticker.desired_num_ticks = 1

hover = HoverTool(tooltipe = [("Start_string ","@"), ("End_string", "@End")])
p.add_tools(hover)
q = p.quad(left = "Start", right = "End", bottom=0, top= 1, color= "green", souce = cds)
output_file("Motion_graph.html")
show(p)
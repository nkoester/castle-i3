#!/usr/bin/python3
from i3pystatus import Status
from i3pystatus.mail import imap
from i3pystatus.weather import weathercom

status = Status(standalone=True)

status.register("clock",
    color="#93A8D8",
    format="⏲%a %-d %b %H:%M",
)

status.register("weather",
    format='{icon} {current_temp}{temp_unit}',
    colorize=True,
    backend=weathercom.Weathercom(
        location_code="GMXX6175",
        units="metric",
    ),
    on_leftclick= ["chromium http://www.weather.com/de-DE/wetter/heute/l/GMXX6175"]
)

status.register("battery",
    format="{status} {percentage:.2f}% {remaining:%E%hh:%Mm}",
    alert=True,
    alert_percentage=10,
    status={
        "DIS": "🔋",
        "CHR": "🔌",
        "FULL": "🗸",
    },)

status.register("mem",
    color="#E0DA37",
    format="🗐 {used_mem} MiB",)

status.register("load")

status.register("cpu_usage",
    hints = {"markup": "pango"},
    interval=1,
    format="{usage:02}%",)

status.register("cpu_usage_graph",
    cpu="usage_cpu",
    graph_style="blocks",
    direction="right-to-left",
    graph_width=7,
    format="⚙🖳 {cpu_graph}",
)

# Shows your CPU temperature, if you have a Intel CPU
status.register("temp",
    format="{temp:.0f}°C",)

#status.register("temp",
#    color="#F1AF5F",
#    file="/sys/devices/platform/it87.656/temp1_input",
#    format="{temp:.0f}°C",)

#status.register("disk",
#    color="#FFA500",
#    path="/home",
#    format="🖬/home {avail}G",
#    #format="{used}/{total}G [{avail}G]",
#)

status.register("disk",
    color="#FFA500",
    path="/",
    format="🖬/ {avail}G",)

status.register("network",
    interface="enp0s31f6",
    #format_up="〰{v4cidr}",
    format_up="🖧 {v4cidr} ⮉{bytes_recv:5.0f} KB/s ⮋{bytes_sent:5.0f} KB/s",
)

# Note: requires both netifaces and basiciw (for essid and quality)
status.register("network",
    interface="wlp1s0",
    format_up="📶 {essid} {quality:02.0f}% ⮋{bytes_recv:5.0f} KB/s ⮉{bytes_sent:5.0f} KB/s",)


status.run()

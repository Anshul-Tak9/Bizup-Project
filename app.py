from flask import Flask,jsonify,request,render_template
from urllib.request import urlopen
from colormap import rgb2hex
import io
import extcolors

app = Flask(__name__)

@app.route('/')
def index():
    if (request.query_string):
        img = request.query_string[4:]
        imglink = img.decode("utf-8")  # image url link extracted from query string
        fd = urlopen(imglink)
        f = io.BytesIO(fd.read())
        colors, pixel_count = extcolors.extract_from_path(f)
        rgb=colors[0][0]
        if(len(colors)<2):
            rgb1 =rgb
        else:
            rgb1 = colors[1][0]
        result = {
            "logo_border": rgb2hex(rgb[0], rgb[1], rgb[2]),
            "dominant_color": rgb2hex(rgb1[0], rgb1[1], rgb1[2]), #converting (r,g,b) color to hex
        }
        return jsonify(result)
    else:
        return render_template("display.html")

#https://storage.googleapis.com/bizupimg/profile_photo/WhatsApp%20Image%202020-08-23%20at%203.11.46%20PM%20-%20Himanshu%20Kohli.jpeg
#https://storage.googleapis.com/bizupimg/profile_photo/918527129869%20instagram-logo-png-2451.png
#https://storage.googleapis.com/bizupimg/profile_photo/bhawya_logo.jpeg
#https://storage.googleapis.com/bizupimg/profile_photo/kppl_logo.png


if __name__=="__main__":
    app.run(debug=True)
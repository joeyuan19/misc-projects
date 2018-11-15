from PIL import Image, ImageFont, ImageDraw


img = Image.open('chart.png')
w,h = img.size

# put pixels into 2D array for ease of use
data = list(img.getdata())
xy_data = []
for y in xrange(h):
    temp = []
    for x in xrange(w):
        temp.append(data[y*w + x])
    xy_data.append(temp)

# get the title
title = raw_input("Title:")

# load the font
font_size = 20
font_path = "C:/Windows/winsxs/amd64_microsoft-windows-font-truetype-arial_31bf3856ad364e35_6.1.7601.17621_none_d09ba6bac4056b40/arialbd.ttf"
font = ImageFont.truetype(font_path,font_size)

#  Get the required height for you images
height_needed = font.getsize(title)[1] + 2  # 2 px for padding

# get the upperleft pixel to match color
bg = xy_data[0][0]

# add rows to the data to prepare for the text
xy_data += [[bg]*w for i in range(height_needed+5)]  # +5 for more padding

# resize image
img = img.resize((w,h+height_needed+5))

# get the ImageDraw item for this image
draw = ImageDraw.Draw(img)

# draw the text
draw.text((5,0),title,font=font,fill=(0,0,0))  # fill is black

img.save('titled_plot.png')

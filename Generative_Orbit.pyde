# Created by Eric Davidson
w, h = 1500, 1400

# Generation Settings
planets = 10
distance = 110
sun = 200
star_count = 15000

# Empty lists for stars / planets
stars = []
p = []

# Difference between stars mostly
def dist(x1, y1, x2, y2):
    return sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))

def setup():
    size(w, h)
    pixelDensity(2)
    
    # Changing color mode to stay at a low saturation
    colorMode(HSB, 360, 100, 100)
    
    # Black background
    background(0, 0, 0)
    
    # Start the random colors with the sun
    c = int(random(360))
    sun_color = c
    
    # Generate new stars and validate packing within orbit
    for s in range(star_count):
        ran_x = random(w)
        ran_y = random(h)
        valid = True
        if (dist(ran_x, ran_y, w/2, h/2) > (sun + (planets - 1) * distance)/2):
            valid = False
            
        for s in stars:
            if (dist(ran_x, ran_y, s[0], s[1]) < 3):
                valid = False
                
        if (valid is True):
            stars.append([ran_x, ran_y])
            
    
    # Generate the position, size, rotation of each planet
    for i in range(1, planets):
        c = c%360
        p.append([sun + i * distance, random(20, 60), int(random(360)), c, False])
        c += 70
    
    # Draw every star
    noStroke()
    for j in stars:
        fill(120, 0, 70 + random(-20, 20))
        circle(j[0], j[1], 2)
        
    translate(w/2, h/2)
    
    # Draw the Sun
    fill(sun_color, 30, 80)
    circle(0, 0, sun)
    
    # Draw each planet
    for j in p:
        c = j[3]
        push()
        
        # Take away part of the orbit trail
        noFill()
        stroke(c, 30, 100)
        strokeWeight(2)
        circle(0, 0, j[0])
        
        noStroke()
        
        # Draw the planet sphere itself
        rotate(radians(j[2]))
        translate(0, -j[0]/2)
        fill(0, 0, 0)
        circle(0, 0, j[1] + 20)
        fill(c, 30, 100)
        circle(0, 0, j[1])
        
        pop()
        
    
    save("Examples/" +str(int(random(1000))) + ".png")
    
               
        
        

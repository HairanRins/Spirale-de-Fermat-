
import turtle
import math

# Configuration de la fenêtre turtle
screen = turtle.Screen()
screen.bgcolor("white")

# Création d'une turtle pour dessiner
pen = turtle.Turtle()
pen.speed(10)  # Ajuster la vitesse

# Fonction pour dessiner la spirale de Fermat
def fermat_spiral(n_points, angle_increment):
    for i in range(n_points):
        # Calcul des coordonnées polaires
        r = math.sqrt(i) * 10  # La distance croît en fonction de l'indice
        theta = i * angle_increment
        
        # Conversion en coordonnées cartésiennes
        x = r * math.cos(math.radians(theta))
        y = r * math.sin(math.radians(theta))
        
        # Déplacement de la turtle à la position calculée
        pen.goto(x, y)
        pen.dot(5, "blue")  # Ajouter un point

# Dessin du spirale de Fermat avec 200 points
pen.penup()
pen.goto(0, 0)
pen.pendown()
fermat_spiral(200, 137.5)

turtle.done()

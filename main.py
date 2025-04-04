import figure

def main():
    square = figure.Square(7, 'grey', 2, True)
    square.info()
    square.draw()
    quadrilateral = figure.Quadrilateral(8, 7, 6, 8, 'purple', 3, True)
    quadrilateral.info()
    quadrilateral.draw()

if __name__ == "__main__":
    main()
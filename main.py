import algo
import keyboard

def main():
    print("\t---------------------ASCII Maze Generating Algorithm---------------------\n")
    try:
        size = int(input("\nThe size of the maze should be strictly superior to 0.\nEnter the size of the maze : "))
        assert size>0

    except :
        print("Enter a correct value !!")
    
    else:
        algo.draw_maze(size)

    print("\nPress Space to exit...\n")
    keyboard.wait('space')

if __name__ == '__main__':
    main()

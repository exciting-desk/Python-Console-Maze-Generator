import dfs
import kruskal
from keyboard import wait
from os import system

def main():
    vis = False
    while True:
        system('cls')
        print("\t---------------------ASCII Maze Generating Algorithm---------------------\n")
        choice = input("1. Generate with Kruskal\n2. Generate with DFS\n3. Exit\n\n")
        if choice.lower() == 'kruskal' or choice.lower() == 'dfs' or choice.lower() == '2' or choice.lower() == '1':

            vis_input = input("Do you wanna visualize the algorithm ? (y/n)\n")
            if vis_input.lower() == 'y' or vis_input.lower() == 'yes':
                vis = True
            else: 
                vis = False
                
            try:
                size = int(input("\nThe size of the maze should be strictly superior to 0.\nEnter the size of the maze : "))
                assert size>0

            except :
                print("Enter a correct value !!")
            
            else:
                if choice.lower() == 'dfs' or choice.lower() == '2':
                    dfs.draw_maze(size, vis)
                elif choice.lower() == 'kruskal' or choice.lower() == '1':
                    kruskal.draw_maze(size, vis)

        elif choice.lower() == 'exit' or choice.lower() == '3':
            pass
        
        else:
            print("Enter a correct choice\n")

        break

    print("\nPress Space to exit...\n")
    wait('space')

if __name__ == '__main__':
    main()
class Util:
    # Clears screen by printing new lines
    def clearScreen():
        for i in range(100):
            print()
            
             
    # Plots the nth hangman by reading the appropriate file
    def drawMan(n):
        men = ['men/a0.txt', 'men/a1.txt', 'men/a2.txt',
               'men/a3.txt', 'men/a4.txt', 'men/a5.txt', 
               'men/a6.txt']
        f = open( men[n], 'r')
        print( f.read() )

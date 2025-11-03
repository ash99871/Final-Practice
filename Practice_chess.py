import re
import tkinter as tk

#Process
print("Hello!")
print("Welcome to my chess plotter.")
print("")
print("")
print("---------------------------------------------------------")

print("")
print("You're going to write a FEN string.")
print("")
print("These string has to content:")
print("1. The info of each row is separated by \\")
print("2. There must be 8 rows")
print("3. For each row, capital letters are used for white pieces (P, N, B, R, Q, K) and lowercase letters for black pieces (p, n, b, r, q, k).\n Empty spaces are indicated by a number representing the number of consecutive unoccupied squares; for example, 1 is one empty square,\n 3 is three empty squares in a row. ")
print("")
print("Enter your string:")


chess = input()
rg_chess= re.fullmatch(r'([kqrbnpKQRBNP1-8]+/){7}[kqrbnpKQRBNP1-8]+', chess)

print (rg_chess)
parts = chess.split("/")

def calc_Sum(chess):

    if len(parts) != 8:
        print("WRONG: There must be 8 rows")
        return None

    letters_v = 'kqrbnpKQRBNP'
    numbers_v = '12345678'
    error = False
    s = []


    for i, part in enumerate(parts, 1):
        li = []
        ni = []

        for c in part:
            if c.isalpha() and c not in letters_v:
                li.append(c)
            elif c.isdigit() and c not in numbers_v:
                ni.append(c)


        if li:
            print(f"This letters are wrong: {', '.join(set(li))}")
            error = True

        if ni:
            print(f"This numbers are bigger than the possibles in the row: {', '.join(set(ni))}")
            error = True


        if li or ni:
            s.append(0)
            continue


        summa = 0

        exceed = None
        complete = None

        for j, c in enumerate(part):
            if c.lower() in 'kqrbnp':
                value = 1
                summa += value

            elif c in numbers_v:
                value = int(c)
                summa += value



            if summa > 8 and exceed is None:
                exceed = (j, c, summa)


            if summa == 8 and complete is None:
                complete = (j, c)


        print("Row correct")


        if summa > 8:
            if exceed:
                pos, char, sum_at_the_point = exceed
                if char.isdigit():
                    print(
                        f"The number'{char}' exceeds the available spaces in the board")
                else:
                    print(
                        f"The letter '{char}' exceeds the available spaces in the board")
            error = True
        elif summa < 8:
            print("There are not information enough about the board")
            error = True
        elif summa == 8:
            print("Correct row")
        else:
            print("Blank space")
            error = True

        s.append(summa)

    if error:
        print("Cannot pursue, bad data")
        return None
    else:
        print("Well")
        return "Ok"

Atempt=calc_Sum(chess)

#Board
root = tk.Tk()
root.title("Chess Board")

cell_size=70
canvas = tk.Canvas(root, width=cell_size*8, height=cell_size*8)
canvas.pack()

for row in range(8):
    for col in range(8):
        color = "#ffffff" if (row + col) % 2 == 0 else "#b58863"
        x1 = col * cell_size
        y1 = row * cell_size
        x2 = x1 + cell_size
        y2 = y1 + cell_size
        canvas.create_rectangle(x1, y1, x2, y2, fill=color)

conversion_unicode = {
    'p': '♟', 'r': '♜', 'n': '♞', 'b': '♝', 'q': '♛', 'k': '♚',
    'P': '♙', 'R': '♖', 'N': '♘', 'B': '♗', 'Q': '♕', 'K': '♔'
}

def fen(chess):
    for r_index, row in enumerate(parts):
        c_index=0
        for t in row:
            if t.isdigit():
                c_index += int(t)
            elif t in conversion_unicode:
                x= c_index*cell_size+cell_size/2
                y= r_index*cell_size+cell_size/2
                canvas.create_text(x, y, text=conversion_unicode[t], font=("Segoe UI Symbol", 40), tags="piece")
                c_index+=1

entry = tk.Entry(root, width=60, font=("Consolas", 12))
entry.insert(0, fen)
entry.pack(pady=10)

def update():
    new_fen = entry.get()
    try:
        fen(new_fen)
    except Exception:
        print("Error: FEN inválida")

btn = tk.Button(root, text="Refresh", command=update)
btn.pack()


root.mainloop()








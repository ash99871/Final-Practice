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

if not rg_chess:
    print('Invalid format')
    print("Invalid letter or digit(0,9) written")
    print("Expected format: 8 rows separated by '/' with only letters (kqrbnpKQRBNP) and numbers (1-8)")
    exit()

print("Valid input")

parts = chess.split("/")


def calc_Sum(parts):
    if len(parts) != 8:
        print("WRONG: There must be 8 rows")
        return None

    numbers_v = '12345678'
    error = False
    s = []

    for i, part in enumerate(parts, 1):

        summa = 0
        exceed = None

        for j, c in enumerate(part):
            if c.lower() in 'kqrbnp':
                value = 1
                summa += value
            elif c in numbers_v:
                value = int(c)
                summa += value

            if summa > 8 and exceed is None:
                exceed = (j, c, summa)

        if summa > 8:
            if exceed:
                pos, char, sum_at_the_point = exceed
                if char.isdigit():
                    print(f"The number '{char}' exceeds 8 spaces")
                else:
                    print(f"The letter '{char}' exceeds 8 spaces")
            error = True
        elif summa < 8:
            print("There are not information enough about the board")
            error = True
        elif summa == 8:
            print(" Correct")

        s.append(summa)

    if error:
        print("VALIDATION FAILED")
        return None
    else:
        print("ALL ROWS VALID")
        return "Ok"


attempt = calc_Sum(parts)

if attempt:
    print("Correct")
else:
    print("Validation failed")


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













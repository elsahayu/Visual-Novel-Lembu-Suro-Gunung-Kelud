init python:
    import random

    class Puzzle:
        def __init__(self):
            self.size = 3
            self.tiles = list(range(1, 9)) + [0]
            self.shuffle()

        def shuffle(self):
            while True:
                random.shuffle(self.tiles)
                if self.is_solvable():
                    break

        def is_solvable(self):
            inv = 0
            for i in range(len(self.tiles)):
                for j in range(i + 1, len(self.tiles)):
                    if self.tiles[i] and self.tiles[j] and self.tiles[i] > self.tiles[j]:
                        inv += 1
            return inv % 2 == 0

        def get(self, row, col):
            return self.tiles[row * self.size + col]

        def move(self, row, col):
            index = row * self.size + col
            empty = self.tiles.index(0)
            erow, ecol = divmod(empty, self.size)
            if abs(erow - row) + abs(ecol - col) == 1:
                self.tiles[empty], self.tiles[index] = self.tiles[index], self.tiles[empty]

        def is_completed(self):
            return self.tiles == list(range(1, 9)) + [0]

default puzzle_1 = Puzzle()
default puzzle_2 = Puzzle()
default puzzle_timer = 180
default puzzle_timeout = False

init:
    style puzzle_timer_text:
        size 30
        color "#FFFF00"
        outlines [(2, "#FFFF00")]

    style puzzle_menu_frame:
        background "#00000080"
        padding (20, 20)

    style puzzle_menu_button:
        size 30
        color "#FFFFFF"
        outlines [(1, "#000000")]
        xminimum 200
        background "#33333380"
        padding (10, 5)

screen puzzle_game(folder="puzzle", puzzle=puzzle_1):
    tag menu

    timer 1.0 repeat True action If(puzzle_timer > 0 and not puzzle.is_completed(),
        SetVariable("puzzle_timer", puzzle_timer - 1))

    if puzzle_timer == 0 and not puzzle.is_completed():
        $ puzzle_timeout = True

    frame:
        align (0.5, 0.5)
        has vbox spacing 5
        for row in range(3):
            hbox:
                spacing 5
                for col in range(3):
                    $ val = puzzle.get(row, col)
                    if val == 0:
                        imagebutton:
                            idle "images/%s/empty.png" % folder
                            xysize (300, 300)
                            action NullAction()
                    else:
                        imagebutton:
                            idle "images/%s/puzzle%d.png" % (folder, val)
                            xysize (300, 300)
                            action Function(puzzle.move, row, col), Show("puzzle_game", folder=folder, puzzle=puzzle)

    text "Waktu: [puzzle_timer] detik" style "puzzle_timer_text" xalign 0.1 yalign 0.5

    if puzzle.is_completed():
        $ puzzle_timer = 0
        text "Selamat!" size 50 color "#FF3333" outlines [(2, "#000000")] xalign 0.5
        textbutton "✔ Selesai! Klik untuk lanjut." style "puzzle_menu_button" xalign 0.5 yalign 0.9:
            action [Hide("puzzle_game"), Return()]

    if puzzle_timeout:
        frame style "puzzle_menu_frame" xalign 0.5 yalign 0.8:
            vbox:
                spacing 15
                text "⌛ Waktu Habis!" size 50 color "#FF3333" outlines [(2, "#000000")] xalign 0.5
                textbutton "🔄 Ulang" style "puzzle_menu_button":
                    action [
                        SetVariable("puzzle_timer", 180),
                        SetVariable("puzzle_timeout", False),
                        Function(puzzle.shuffle),
                        Show("puzzle_game", folder=folder, puzzle=puzzle)
                    ]

                textbutton "⏭ Lewati Puzzle" style "puzzle_menu_button":
                    action [Hide("puzzle_game"), Jump ("setelah_puzzle")]

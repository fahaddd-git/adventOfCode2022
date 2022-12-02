from pathlib import Path

"""
col1        col2
opponent    player
A=Rock      X=Rock
B=Paper     Y=Paper
C=Scissors  Z=Scissors

Score = shape score + outcome score per turn

Outcome score per turn:
0 lose
3 draw
6 win

Selected shape score:
Rock = 1
Paper = 2
Scissors = 3
"""
"""
B Z 
C Z
B X
A Y
B X
"""

INPUT_FILE = Path(__file__).parent.resolve() / "input.txt"
remapping = {"A": "X", "B" : "Y", "C" : "Z"} # remaps column 2 to be like column 1
scores={
    "A": 1,  # Rock
    "X" : 1,
    "B": 2,  # Paper
    "Y" : 2,
    "C" : 3, # Scissors
    "Z" : 3
}
# rock beats scissors
# paper beats rock
# scissors beats paper

def part_one():
    p1_score=0
    p2_score=0
    def score_shape(p1_shape, p2_shape):
        """
        Add selected shape score.  We are p2.
        """
        nonlocal p1_score
        nonlocal p2_score
        p2_score += scores[p2_shape]
    
    def outcome_score(p1_shape, p2_shape):
        nonlocal p2_score
        remapped_p1 = remapping[p1_shape]
        # shapes same no winner
        if remapped_p1 == p2_shape:
            p2_score += 3
        # rock beats scissors
        elif p2_shape == "X" and remapped_p1 == "Z":
            p2_score += 6
        # paper beats rock
        elif p2_shape == "Y" and remapped_p1 == "X":
            p2_score += 6
        # scissors beats paper
        elif p2_shape == "Z" and remapped_p1 == "Y":
            p2_score += 6


    with open(INPUT_FILE, "r") as inputfile:
        for line in inputfile.readlines():
            player_shapes = line.rstrip("\n").split(" ")
            # shape score
            score_shape(*player_shapes)
            # outcome score
            outcome_score(*player_shapes)
    return p2_score

# X= lose   find losing shape points
# Y= draw   take p1 shape + 3
# Z= win    take p2 shape + 6

# rock beats scissors
# paper beats rock
# scissors beats paper
losing_shapes= {
    "A" : "Z", "B" : "X" , "C" : "Y"
}
winning_shapes = {v: k for k,v in losing_shapes.items()}

def part_two():
    p1_score=0
    p2_score=0
    def score_shape(shape):
        """
        Add selected shape score.  We are p2.
        """
        nonlocal p1_score
        nonlocal p2_score
        p2_score += scores[shape]

    with open(INPUT_FILE, "r") as inputfile:
        for line in inputfile.readlines():
            p1, p2 = line.rstrip("\n").split(" ")
            # draw. p1's shape score +3
            if p2 == "Y":
                score_shape(p1)
                p2_score += 3
            # win. determine p2 winning shape + 6
            elif p2 == "Z":
                winning = winning_shapes[remapping[p1]]
                score_shape(winning)
                p2_score += 6
            # find losing shape points
            else:
                p2_losing_shape = losing_shapes[p1]
                p2_losing_shape_score = scores[p2_losing_shape]
                p2_score += p2_losing_shape_score
    
    return p2_score




if __name__ == "__main__":
    print(part_one())
    print(part_two())
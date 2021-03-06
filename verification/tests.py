"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": (('X....XXX', 'X....XXX', 'X....XXX', 'X....XXX', 'X....XXX', 'X......X', 'X......X', 'X......X',
                       'X......X', 'XXX....X'), 0),
            "answer": 8,
            "explanation": [[['X', '0', '0', '0', '0', 'X', 'X', 'X'],
                             ['X', '*', '*', '*', '*', 'X', 'X', 'X'],
                             ['X', '.', '.', '.', '.', 'X', 'X', 'X'],
                             ['X', '.', '.', '.', '.', 'X', 'X', 'X'],
                             ['X', '.', '.', '.', '.', 'X', 'X', 'X'],
                             ['X', '.', '.', '.', '.', '.', '.', 'X'],
                             ['X', '.', '.', '.', '.', '.', '.', 'X'],
                             ['X', '.', '.', '.', '.', '.', '.', 'X'],
                             ['X', '.', '.', '.', '.', '.', '.', 'X'],
                             ['X', 'X', 'X', '.', '.', '.', '.', 'X']],
                            [['X', '|', '|', '|', '|', 'X', 'X', 'X'],
                             ['X', '|', '|', '|', '|', 'X', 'X', 'X'],
                             ['X', '|', '|', '|', '|', 'X', 'X', 'X'],
                             ['X', '|', '|', '|', '|', 'X', 'X', 'X'],
                             ['X', '|', '|', '|', '|', 'X', 'X', 'X'],
                             ['X', '|', '|', '|', '>', '>', '|', 'X'],
                             ['X', '|', '|', '>', '>', '|', '|', 'X'],
                             ['X', '|', '>', '>', '|', '|', '|', 'X'],
                             ['X', '>', '>', '|', '|', '|', '|', 'X'],
                             ['X', 'X', 'X', '|', '|', '|', '|', 'X']]]
        },

        {
            "input": (('X....XXX', 'X....XXX', 'X....XXX', 'X....XXX', 'X....XXX', 'X......X', 'X......X', 'X......X',
                       'X......X', 'XXX....X'), 7),
            "answer": 18,
            "explanation": [[['X', '.', '.', '.', '.', 'X', 'X', 'X'],
                             ['X', '.', '.', '.', '.', 'X', 'X', 'X'],
                             ['X', '.', '.', '.', '.', 'X', 'X', 'X'],
                             ['X', '.', '.', '.', '.', 'X', 'X', 'X'],
                             ['X', '.', '.', '.', '.', 'X', 'X', 'X'],
                             ['X', '.', '.', '*', '*', '*', '0', 'X'],
                             ['X', '*', '*', '*', '0', '*', '*', 'X'],
                             ['X', '0', '0', '*', '*', '*', '.', 'X'],
                             ['X', '*', '*', '*', '.', '.', '.', 'X'],
                             ['X', 'X', 'X', '.', '.', '.', '.', 'X']],
                            [['X', '|', '|', '|', '|', 'X', 'X', 'X'],
                             ['X', '|', '|', '|', '|', 'X', 'X', 'X'],
                             ['X', '|', '|', '|', '|', 'X', 'X', 'X'],
                             ['X', '|', '|', '|', '|', 'X', 'X', 'X'],
                             ['X', '|', '|', '|', '|', 'X', 'X', 'X'],
                             ['X', '|', '|', '|', '>', '>', '|', 'X'],
                             ['X', '|', '|', '>', '>', '|', '|', 'X'],
                             ['X', '|', '>', '>', '|', '|', '|', 'X'],
                             ['X', '>', '>', '|', '|', '|', '|', 'X'],
                             ['X', 'X', 'X', '|', '|', '|', '|', 'X']]]
        },

        {
            "input": (('X....XXX', 'X....XXX', 'X....XXX', 'X....XXX', 'X....XXX', 'X......X', 'X......X', 'X......X',
                       'X......X', 'XXX....X'), 9),
            "answer": 17,
            "explanation": [[['X', '.', '.', '.', '.', 'X', 'X', 'X'],
                             ['X', '.', '.', '.', '.', 'X', 'X', 'X'],
                             ['X', '.', '.', '.', '.', 'X', 'X', 'X'],
                             ['X', '.', '.', '.', '.', 'X', 'X', 'X'],
                             ['X', '.', '.', '.', '.', 'X', 'X', 'X'],
                             ['X', '.', '.', '.', '.', '.', '.', 'X'],
                             ['X', '.', '.', '*', '*', '*', '*', 'X'],
                             ['X', '*', '*', '*', '0', '0', '0', 'X'],
                             ['X', '*', '0', '*', '*', '*', '*', 'X'],
                             ['X', 'X', 'X', '*', '.', '.', '.', 'X']],
                            [['X', '|', '|', '|', '|', 'X', 'X', 'X'],
                             ['X', '|', '|', '|', '|', 'X', 'X', 'X'],
                             ['X', '|', '|', '|', '|', 'X', 'X', 'X'],
                             ['X', '|', '|', '|', '|', 'X', 'X', 'X'],
                             ['X', '|', '|', '|', '|', 'X', 'X', 'X'],
                             ['X', '|', '|', '|', '>', '>', '|', 'X'],
                             ['X', '|', '|', '>', '>', '|', '|', 'X'],
                             ['X', '|', '>', '>', '|', '|', '|', 'X'],
                             ['X', '>', '>', '|', '|', '|', '|', 'X'],
                             ['X', 'X', 'X', '|', '|', '|', '|', 'X']]]
        },
    ],
    "Extra": [
        {
            "input": (('X..X', 'X..X', 'X..X', 'X..X'), 1),
            "answer": 6,
            "explanation": [[['X', '*', '*', 'X'],
                             ['X', '0', '0', 'X'],
                             ['X', '*', '*', 'X'],
                             ['X', '.', '.', 'X']],
                            [['X', '|', '|', 'X'],
                             ['X', '|', '|', 'X'],
                             ['X', '|', '|', 'X'],
                             ['X', '|', '|', 'X']]]
        },

        {
            "input": (('X.XX', 'X..X', 'XX.X', 'X..X', 'X.XX'), 3),
            "answer": 5,
            "explanation": [[['X', '.', 'X', 'X'],
                             ['X', '*', '*', 'X'],
                             ['X', 'X', '0', 'X'],
                             ['X', '*', '*', 'X'],
                             ['X', '.', 'X', 'X']],
                            [['X', '|', 'X', 'X'],
                             ['X', '>', '|', 'X'],
                             ['X', 'X', '|', 'X'],
                             ['X', '|', '<', 'X'],
                             ['X', '|', 'X', 'X']]]
        },

        {
            "input": (('XXXXX.X', 'X...X.X', 'X.X...X', 'X.XXXXX'), 6),
            "answer": 5,
            "explanation": [[['X', 'X', 'X', 'X', 'X', '.', 'X'],
                             ['X', '*', '0', '*', 'X', '.', 'X'],
                             ['X', '*', 'X', '*', '.', '.', 'X'],
                             ['X', '.', 'X', 'X', 'X', 'X', 'X']],
                            [['X', 'X', 'X', 'X', 'X', '|', 'X'],
                             ['X', '|', '<', '<', 'X', '|', 'X'],
                             ['X', '|', 'X', '^', '<', '<', 'X'],
                             ['X', '|', 'X', 'X', 'X', 'X', 'X']]]
        },
        {
            "input": (('X..XXXXXXX', 'X..X.....X', 'X..X.....X', 'X.....X..X', 'X.....X..X', 'XXXXXXX..X', 'XX.......X',
                       'XX.......X', 'XX..XXXXXX'), 4),
            "answer": 10,
            "explanation": [
                [['X', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                 ['X', '.', '.', 'X', '.', '.', '.', '.', '.', 'X'],
                 ['X', '.', '*', 'X', '*', '.', '.', '.', '.', 'X'],
                 ['X', '*', '*', '0', '*', '.', 'X', '.', '.', 'X'],
                 ['X', '0', '*', '*', '*', '.', 'X', '.', '.', 'X'],
                 ['X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.', 'X'],
                 ['X', 'X', '.', '.', '.', '.', '.', '.', '.', 'X'],
                 ['X', 'X', '.', '.', '.', '.', '.', '.', '.', 'X'],
                 ['X', 'X', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X']],
                [['X', '|', '|', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                 ['X', '|', '|', 'X', '>', '>', '>', '>', '|', 'X'],
                 ['X', '|', '|', 'X', '^', '>', '>', '|', '|', 'X'],
                 ['X', '|', '>', '>', '^', '^', 'X', '|', '|', 'X'],
                 ['X', '>', '>', '>', '>', '^', 'X', '|', '|', 'X'],
                 ['X', 'X', 'X', 'X', 'X', 'X', 'X', '|', '|', 'X'],
                 ['X', 'X', '|', '<', '<', '<', '<', '<', '|', 'X'],
                 ['X', 'X', '|', '|', '<', '<', '<', '<', '<', 'X'],
                 ['X', 'X', '|', '|', 'X', 'X', 'X', 'X', 'X', 'X']]]
        },

        {
            "input": (('X..XXXXXXX', 'X..X.....X', 'X..X.....X', 'X.....X..X', 'X.....X..X', 'XXXXXXX..X', 'XX.......X',
                       'XX.......X', 'XX..XXXXXX'), 12),
            "answer": 8,
            "explanation": [
                [['X', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                 ['X', '.', '.', 'X', '.', '.', '*', '*', '*', 'X'],
                 ['X', '.', '.', 'X', '.', '.', '*', '0', '0', 'X'],
                 ['X', '.', '.', '.', '.', '.', 'X', '*', '*', 'X'],
                 ['X', '.', '.', '.', '.', '.', 'X', '.', '.', 'X'],
                 ['X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.', 'X'],
                 ['X', 'X', '.', '.', '.', '.', '.', '.', '.', 'X'],
                 ['X', 'X', '.', '.', '.', '.', '.', '.', '.', 'X'],
                 ['X', 'X', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X']],
                [['X', '|', '|', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                 ['X', '|', '|', 'X', '>', '>', '>', '>', '|', 'X'],
                 ['X', '|', '|', 'X', '^', '>', '>', '|', '|', 'X'],
                 ['X', '|', '>', '>', '^', '^', 'X', '|', '|', 'X'],
                 ['X', '>', '>', '>', '>', '^', 'X', '|', '|', 'X'],
                 ['X', 'X', 'X', 'X', 'X', 'X', 'X', '|', '|', 'X'],
                 ['X', 'X', '|', '<', '<', '<', '<', '<', '|', 'X'],
                 ['X', 'X', '|', '|', '<', '<', '<', '<', '<', 'X'],
                 ['X', 'X', '|', '|', 'X', 'X', 'X', 'X', 'X', 'X']]]
        },
        {
            "input": (('X..XXXXXXX', 'X..X.....X', 'X..X.....X', 'X.....X..X', 'X.....X..X', 'XXXXXXX..X', 'XX.......X',
                       'XX.......X', 'XX..XXXXXX'), 17),
            "answer": 9,
            "explanation": [
                [['X', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                 ['X', '.', '.', 'X', '.', '.', '.', '.', '.', 'X'],
                 ['X', '.', '.', 'X', '.', '.', '.', '.', '.', 'X'],
                 ['X', '.', '.', '.', '.', '.', 'X', '.', '.', 'X'],
                 ['X', '.', '.', '.', '.', '.', 'X', '.', '.', 'X'],
                 ['X', 'X', 'X', 'X', 'X', 'X', 'X', '*', '.', 'X'],
                 ['X', 'X', '.', '.', '.', '*', '0', '*', '*', 'X'],
                 ['X', 'X', '.', '.', '.', '*', '*', '*', '0', 'X'],
                 ['X', 'X', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X']],
                [['X', '|', '|', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                 ['X', '|', '|', 'X', '>', '>', '>', '>', '|', 'X'],
                 ['X', '|', '|', 'X', '^', '>', '>', '|', '|', 'X'],
                 ['X', '|', '>', '>', '^', '^', 'X', '|', '|', 'X'],
                 ['X', '>', '>', '>', '>', '^', 'X', '|', '|', 'X'],
                 ['X', 'X', 'X', 'X', 'X', 'X', 'X', '|', '|', 'X'],
                 ['X', 'X', '|', '<', '<', '<', '<', '<', '|', 'X'],
                 ['X', 'X', '|', '|', '<', '<', '<', '<', '<', 'X'],
                 ['X', 'X', '|', '|', 'X', 'X', 'X', 'X', 'X', 'X']]]
        },
        {
            "input": ((
                          'XXXXXXXXXXXXXXXXXXXXXXX.....X', 'X...........................X',
                          'X...........................X',
                          'X...........................X', 'X...........................X',
                          'X...........................X',
                          'X.....XXXXXXXXXXXXXXXXXXXXXXX', 'X.....X.....................X',
                          'X.....X.....................X',
                          'X.....X.....................X', 'X.....X.....................X',
                          'X.....X.....................X',
                          'X.....X.....XXXXXXXXXXX.....X', 'X...........XXXXXX..........X',
                          'X...........XXXXXX..........X',
                          'X...........XXXXXX..........X', 'X...........XXXXXX..........X',
                          'X...........XXXXXX..........X',
                          'XXXXXXXXXXXXXXXXXX.....XXXXXX'), 10),
            "answer": 31,
            "explanation": [
                [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
                  'X', 'X', 'X', '.', '.', '.', '.', '.', 'X'],
                 ['X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '*', '0', '*', '*', '*', '.', '.',
                  '.', '.', '.', '.', '.', '.', '.', '.', 'X'],
                 ['X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '*', '*', '*', '0', '*', '*', '*',
                  '.', '.', '.', '.', '.', '.', '.', '.', 'X'],
                 ['X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '*', '*', '*', '0', '*',
                  '*', '*', '.', '.', '.', '.', '.', '.', 'X'],
                 ['X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '*', '*', '*',
                  '0', '*', '*', '*', '.', '.', '.', '.', 'X'],
                 ['X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '*',
                  '*', '*', '0', '*', '.', '.', '.', '.', 'X'],
                 ['X', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
                  'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                 ['X', '.', '.', '.', '.', '.', 'X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                  '.', '.', '.', '.', '.', '.', '.', '.', 'X'],
                 ['X', '.', '.', '.', '.', '.', 'X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                  '.', '.', '.', '.', '.', '.', '.', '.', 'X'],
                 ['X', '.', '.', '.', '.', '.', 'X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                  '.', '.', '.', '.', '.', '.', '.', '.', 'X'],
                 ['X', '.', '.', '.', '.', '.', 'X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                  '.', '.', '.', '.', '.', '.', '.', '.', 'X'],
                 ['X', '.', '.', '.', '.', '.', 'X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                  '.', '.', '.', '.', '.', '.', '.', '.', 'X'],
                 ['X', '.', '.', '.', '.', '.', 'X', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
                  'X', 'X', 'X', '.', '.', '.', '.', '.', 'X'],
                 ['X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.',
                  '.', '.', '.', '.', '.', '.', '.', '.', 'X'],
                 ['X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.',
                  '.', '.', '.', '.', '.', '.', '.', '.', 'X'],
                 ['X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.',
                  '.', '.', '.', '.', '.', '.', '.', '.', 'X'],
                 ['X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.',
                  '.', '.', '.', '.', '.', '.', '.', '.', 'X'],
                 ['X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.',
                  '.', '.', '.', '.', '.', '.', '.', '.', 'X'],
                 ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.',
                  '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X']],
                [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
                  'X', 'X', 'X', '|', '|', '|', '|', '|', 'X'],
                 ['X', '|', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<',
                  '<', '<', '<', '<', '|', '|', '|', '|', 'X'],
                 ['X', '|', '|', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<',
                  '<', '<', '<', '<', '<', '|', '|', '|', 'X'],
                 ['X', '|', '|', '|', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<',
                  '<', '<', '<', '<', '<', '<', '|', '|', 'X'],
                 ['X', '|', '|', '|', '|', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<',
                  '<', '<', '<', '<', '<', '<', '<', '|', 'X'],
                 ['X', '|', '|', '|', '|', '|', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<',
                  '<', '<', '<', '<', '<', '<', '<', '<', 'X'],
                 ['X', '|', '|', '|', '|', '|', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
                  'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                 ['X', '|', '|', '|', '|', '|', 'X', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>',
                  '>', '>', '>', '>', '>', '>', '>', '|', 'X'],
                 ['X', '|', '|', '|', '|', '|', 'X', '^', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>',
                  '>', '>', '>', '>', '>', '>', '|', '|', 'X'],
                 ['X', '|', '|', '|', '|', '|', 'X', '^', '^', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>',
                  '>', '>', '>', '>', '>', '|', '|', '|', 'X'],
                 ['X', '|', '|', '|', '|', '|', 'X', '^', '^', '^', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>',
                  '>', '>', '>', '>', '|', '|', '|', '|', 'X'],
                 ['X', '|', '|', '|', '|', '|', 'X', '^', '^', '^', '^', '>', '>', '>', '>', '>', '>', '>', '>', '>',
                  '>', '>', '>', '|', '|', '|', '|', '|', 'X'],
                 ['X', '|', '|', '|', '|', '|', 'X', '^', '^', '^', '^', '^', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
                  'X', 'X', 'X', '|', '|', '|', '|', '|', 'X'],
                 ['X', '|', '|', '|', '|', '>', '>', '^', '^', '^', '^', '^', 'X', 'X', 'X', 'X', 'X', 'X', '|', '<',
                  '<', '<', '<', '<', '|', '|', '|', '|', 'X'],
                 ['X', '|', '|', '|', '>', '>', '>', '>', '^', '^', '^', '^', 'X', 'X', 'X', 'X', 'X', 'X', '|', '|',
                  '<', '<', '<', '<', '<', '|', '|', '|', 'X'],
                 ['X', '|', '|', '>', '>', '>', '>', '>', '>', '^', '^', '^', 'X', 'X', 'X', 'X', 'X', 'X', '|', '|',
                  '|', '<', '<', '<', '<', '<', '|', '|', 'X'],
                 ['X', '|', '>', '>', '>', '>', '>', '>', '>', '>', '^', '^', 'X', 'X', 'X', 'X', 'X', 'X', '|', '|',
                  '|', '|', '<', '<', '<', '<', '<', '|', 'X'],
                 ['X', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>', '^', 'X', 'X', 'X', 'X', 'X', 'X', '|', '|',
                  '|', '|', '|', '<', '<', '<', '<', '<', 'X'],
                 ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '|', '|',
                  '|', '|', '|', 'X', 'X', 'X', 'X', 'X', 'X']]]
        },
        {
            "input": ((
                          'XXXXXXXXXXXXXXXXXXXXXXX.....X', 'X...........................X',
                          'X...........................X',
                          'X...........................X', 'X...........................X',
                          'X...........................X',
                          'X.....XXXXXXXXXXXXXXXXXXXXXXX', 'X.....X.....................X',
                          'X.....X.....................X',
                          'X.....X.....................X', 'X.....X.....................X',
                          'X.....X.....................X',
                          'X.....X.....XXXXXXXXXXX.....X', 'X...........XXXXXX..........X',
                          'X...........XXXXXX..........X',
                          'X...........XXXXXX..........X', 'X...........XXXXXX..........X',
                          'X...........XXXXXX..........X',
                          'XXXXXXXXXXXXXXXXXX.....XXXXXX'), 62),
            "answer": 31,
            "explanation": [[['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
                              'X', 'X', 'X', 'X', 'X', '.', '.', '.', '.', '.', 'X'],
                             ['X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                              '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X'],
                             ['X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                              '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X'],
                             ['X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                              '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X'],
                             ['X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                              '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X'],
                             ['X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                              '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X'],
                             ['X', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
                              'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                             ['X', '.', '.', '.', '.', '.', 'X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                              '.', '.', '.', '.', '.', '*', '*', '*', '0', '*', 'X'],
                             ['X', '.', '.', '.', '.', '.', 'X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                              '.', '.', '.', '*', '*', '*', '0', '*', '*', '*', 'X'],
                             ['X', '.', '.', '.', '.', '.', 'X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                              '.', '*', '*', '*', '0', '*', '*', '*', '.', '.', 'X'],
                             ['X', '.', '.', '.', '.', '.', 'X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '*',
                              '*', '*', '0', '*', '*', '*', '.', '.', '.', '.', 'X'],
                             ['X', '.', '.', '.', '.', '.', 'X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '*',
                              '0', '*', '*', '*', '.', '.', '.', '.', '.', '.', 'X'],
                             ['X', '.', '.', '.', '.', '.', 'X', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X',
                              'X', 'X', 'X', 'X', 'X', '.', '.', '.', '.', '.', 'X'],
                             ['X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X',
                              '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X'],
                             ['X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X',
                              '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X'],
                             ['X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X',
                              '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X'],
                             ['X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X',
                              '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X'],
                             ['X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X',
                              '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X'],
                             ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
                              '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X']],
                            [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
                              'X', 'X', 'X', 'X', 'X', '|', '|', '|', '|', '|', 'X'],
                             ['X', '|', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<',
                              '<', '<', '<', '<', '<', '<', '|', '|', '|', '|', 'X'],
                             ['X', '|', '|', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<',
                              '<', '<', '<', '<', '<', '<', '<', '|', '|', '|', 'X'],
                             ['X', '|', '|', '|', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<',
                              '<', '<', '<', '<', '<', '<', '<', '<', '|', '|', 'X'],
                             ['X', '|', '|', '|', '|', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<',
                              '<', '<', '<', '<', '<', '<', '<', '<', '<', '|', 'X'],
                             ['X', '|', '|', '|', '|', '|', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<',
                              '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', 'X'],
                             ['X', '|', '|', '|', '|', '|', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
                              'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                             ['X', '|', '|', '|', '|', '|', 'X', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>',
                              '>', '>', '>', '>', '>', '>', '>', '>', '>', '|', 'X'],
                             ['X', '|', '|', '|', '|', '|', 'X', '^', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>',
                              '>', '>', '>', '>', '>', '>', '>', '>', '|', '|', 'X'],
                             ['X', '|', '|', '|', '|', '|', 'X', '^', '^', '>', '>', '>', '>', '>', '>', '>', '>', '>',
                              '>', '>', '>', '>', '>', '>', '>', '|', '|', '|', 'X'],
                             ['X', '|', '|', '|', '|', '|', 'X', '^', '^', '^', '>', '>', '>', '>', '>', '>', '>', '>',
                              '>', '>', '>', '>', '>', '>', '|', '|', '|', '|', 'X'],
                             ['X', '|', '|', '|', '|', '|', 'X', '^', '^', '^', '^', '>', '>', '>', '>', '>', '>', '>',
                              '>', '>', '>', '>', '>', '|', '|', '|', '|', '|', 'X'],
                             ['X', '|', '|', '|', '|', '|', 'X', '^', '^', '^', '^', '^', 'X', 'X', 'X', 'X', 'X', 'X',
                              'X', 'X', 'X', 'X', 'X', '|', '|', '|', '|', '|', 'X'],
                             ['X', '|', '|', '|', '|', '>', '>', '^', '^', '^', '^', '^', 'X', 'X', 'X', 'X', 'X', 'X',
                              '|', '<', '<', '<', '<', '<', '|', '|', '|', '|', 'X'],
                             ['X', '|', '|', '|', '>', '>', '>', '>', '^', '^', '^', '^', 'X', 'X', 'X', 'X', 'X', 'X',
                              '|', '|', '<', '<', '<', '<', '<', '|', '|', '|', 'X'],
                             ['X', '|', '|', '>', '>', '>', '>', '>', '>', '^', '^', '^', 'X', 'X', 'X', 'X', 'X', 'X',
                              '|', '|', '|', '<', '<', '<', '<', '<', '|', '|', 'X'],
                             ['X', '|', '>', '>', '>', '>', '>', '>', '>', '>', '^', '^', 'X', 'X', 'X', 'X', 'X', 'X',
                              '|', '|', '|', '|', '<', '<', '<', '<', '<', '|', 'X'],
                             ['X', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>', '^', 'X', 'X', 'X', 'X', 'X', 'X',
                              '|', '|', '|', '|', '|', '<', '<', '<', '<', '<', 'X'],
                             ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
                              '|', '|', '|', '|', '|', 'X', 'X', 'X', 'X', 'X', 'X']]]
        },
        {
            "input": ((
                      'XXXXXXXXXXXXXXXXXXXXXXX.....X', 'X...........................X', 'X...........................X',
                      'X...........................X', 'X...........................X', 'X...........................X',
                      'X.....XXXXXXXXXXXXXXXXXXXXXXX', 'X.....X.....................X', 'X.....X.....................X',
                      'X.....X.....................X', 'X.....X.....................X', 'X.....X.....................X',
                      'X.....X.....XXXXXXXXXXX.....X', 'X...........XXXXXX..........X', 'X...........XXXXXX..........X',
                      'X...........XXXXXX..........X', 'X...........XXXXXX..........X', 'X...........XXXXXX..........X',
                      'XXXXXXXXXXXXXXXXXX.....XXXXXX'), 70),
            "answer": 20,
            "explanation": [[['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
                              'X', 'X', 'X', 'X', 'X', '.', '.', '.', '.', '.', 'X'],
                             ['X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                              '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X'],
                             ['X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                              '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X'],
                             ['X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                              '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X'],
                             ['X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                              '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X'],
                             ['X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                              '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X'],
                             ['X', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
                              'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                             ['X', '.', '.', '.', '.', '.', 'X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                              '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X'],
                             ['X', '.', '.', '.', '.', '.', 'X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                              '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X'],
                             ['X', '.', '.', '.', '.', '.', 'X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                              '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X'],
                             ['X', '.', '.', '.', '.', '.', 'X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                              '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X'],
                             ['X', '.', '.', '.', '.', '.', 'X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                              '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X'],
                             ['X', '.', '.', '.', '.', '.', 'X', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X',
                              'X', 'X', 'X', 'X', 'X', '*', '.', '.', '.', '.', 'X'],
                             ['X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X',
                              '.', '.', '.', '*', '0', '*', '*', '*', '*', '*', 'X'],
                             ['X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X',
                              '.', '.', '.', '*', '*', '*', '0', '0', '0', '0', 'X'],
                             ['X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X',
                              '.', '.', '.', '.', '.', '*', '*', '*', '*', '*', 'X'],
                             ['X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X',
                              '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X'],
                             ['X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X',
                              '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X'],
                             ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
                              '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X']],
                            [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
                              'X', 'X', 'X', 'X', 'X', '|', '|', '|', '|', '|', 'X'],
                             ['X', '|', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<',
                              '<', '<', '<', '<', '<', '<', '|', '|', '|', '|', 'X'],
                             ['X', '|', '|', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<',
                              '<', '<', '<', '<', '<', '<', '<', '|', '|', '|', 'X'],
                             ['X', '|', '|', '|', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<',
                              '<', '<', '<', '<', '<', '<', '<', '<', '|', '|', 'X'],
                             ['X', '|', '|', '|', '|', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<',
                              '<', '<', '<', '<', '<', '<', '<', '<', '<', '|', 'X'],
                             ['X', '|', '|', '|', '|', '|', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<',
                              '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', 'X'],
                             ['X', '|', '|', '|', '|', '|', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
                              'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                             ['X', '|', '|', '|', '|', '|', 'X', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>',
                              '>', '>', '>', '>', '>', '>', '>', '>', '>', '|', 'X'],
                             ['X', '|', '|', '|', '|', '|', 'X', '^', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>',
                              '>', '>', '>', '>', '>', '>', '>', '>', '|', '|', 'X'],
                             ['X', '|', '|', '|', '|', '|', 'X', '^', '^', '>', '>', '>', '>', '>', '>', '>', '>', '>',
                              '>', '>', '>', '>', '>', '>', '>', '|', '|', '|', 'X'],
                             ['X', '|', '|', '|', '|', '|', 'X', '^', '^', '^', '>', '>', '>', '>', '>', '>', '>', '>',
                              '>', '>', '>', '>', '>', '>', '|', '|', '|', '|', 'X'],
                             ['X', '|', '|', '|', '|', '|', 'X', '^', '^', '^', '^', '>', '>', '>', '>', '>', '>', '>',
                              '>', '>', '>', '>', '>', '|', '|', '|', '|', '|', 'X'],
                             ['X', '|', '|', '|', '|', '|', 'X', '^', '^', '^', '^', '^', 'X', 'X', 'X', 'X', 'X', 'X',
                              'X', 'X', 'X', 'X', 'X', '|', '|', '|', '|', '|', 'X'],
                             ['X', '|', '|', '|', '|', '>', '>', '^', '^', '^', '^', '^', 'X', 'X', 'X', 'X', 'X', 'X',
                              '|', '<', '<', '<', '<', '<', '|', '|', '|', '|', 'X'],
                             ['X', '|', '|', '|', '>', '>', '>', '>', '^', '^', '^', '^', 'X', 'X', 'X', 'X', 'X', 'X',
                              '|', '|', '<', '<', '<', '<', '<', '|', '|', '|', 'X'],
                             ['X', '|', '|', '>', '>', '>', '>', '>', '>', '^', '^', '^', 'X', 'X', 'X', 'X', 'X', 'X',
                              '|', '|', '|', '<', '<', '<', '<', '<', '|', '|', 'X'],
                             ['X', '|', '>', '>', '>', '>', '>', '>', '>', '>', '^', '^', 'X', 'X', 'X', 'X', 'X', 'X',
                              '|', '|', '|', '|', '<', '<', '<', '<', '<', '|', 'X'],
                             ['X', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>', '^', 'X', 'X', 'X', 'X', 'X', 'X',
                              '|', '|', '|', '|', '|', '<', '<', '<', '<', '<', 'X'],
                             ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
                              '|', '|', '|', '|', '|', 'X', 'X', 'X', 'X', 'X', 'X']]]
        },
    ]
}

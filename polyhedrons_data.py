POLYHEDRONS = {
    'tetrahedron': {
        'vertices': [
            (-0.81649658, -0.47140452, 0.33333333),
            (0.81649658, -0.47140452, 0.33333333),
            (0.00000000, 0.00000000, -1.00000000),
            (0.00000000, 0.94280904, 0.33333333)
        ],
        'faces': [(0, 1, 3), (0, 3, 2), (0, 2, 1), (1, 2, 3)],
        'color_pattern': [0, 1, 2, 3]
    },
    'octahedron': {
        'vertices': [
            (-0.70710678, -0.70710678, 0.00000000),
            (-0.70710678, 0.70710678, 0.00000000),
            (0.70710678, 0.70710678, 0.00000000),
            (0.70710678, -0.70710678, 0.00000000),
            (0.00000000, 0.00000000, -1.00000000),
            (0.00000000, 0.00000000, 1.00000000)
        ],
        'faces': [
            (0, 1, 4), (0, 4, 3), (0, 3, 5), (0, 5, 1),
            (1, 2, 4), (1, 5, 2), (2, 3, 4), (2, 5, 3)
        ],
        'color_pattern': [1, 0, 1, 0, 0, 1, 1, 0]
    },
}
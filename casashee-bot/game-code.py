#------------------------------------- Data Definitions -------------------------------------#

# A Terrain is one of:
# - "normal"
# - "hill"
# - "capital"
# and represents one of 3 types of tiles on a casashee board

# A Side is one of:
# - "z"
# - "m"
# and represents which army a piece belongs to

# A Type is one of:
# - "army"
# - "camp"
# - "tower"
# and represents a piece's current type

# A Piece is a Piece(Side,Type)
# - where side is which player controls the piece
# - type is its state (army, camp, or tower)
# and represents a piece on a casashee board
class Piece:

    def __init__(self, side, type="army"):
        self.side = side
        self.type = type

    def __str__(self):
        pass

# A Tile is a Tile(Terrain, [Union None Piece])
# - where terrain signifies the type of tile
# - piece indicates the piece on the tile (or None if it is empty)
# and represents one square of a casashee board
class Tile:

    def __init__(self, terrain="normal", piece=None):
        self.terrain = terrain
        self.piece = piece

    def __str__(self):
        pass


#-------------------------------------- Draw Functions --------------------------------------#

# Explanation of emoji names:
# - each emoji is identified by the tile terrain & color (light or dark), and the piece on it
# - ordering: terrain + color + piece side + piece type
# - terrain and piece type are excluded if default ("normal" and "army," respectively)
# - color is excluded for capitals (which are always dark). piece info is excluded if no piece

# tile_to_emoji_name
# takes a tile and, using naming rules above, returns the matching custom emoji name

# board_to_message
# takes a casashee board state and returns a message made of custom emoji representing the board
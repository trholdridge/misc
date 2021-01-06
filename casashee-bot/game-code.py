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

# A Tile is a Tile(Nat, Nat, Terrain, [Union None Piece])
# - where x is the tile's x-position (left is 0)
# - y is the tile's y-position (top is 0)
# - terrain signifies the type of tile
# - piece represents the piece on the tile (or None if it is empty)
# and represents one square of a casashee board
class Tile:

    def __init__(self, x, y, terrain="normal", piece=None):
        self.terrain = terrain
        self.piece = piece
        self.color = "light" if x%2==y%2 else "dark"

    def __str__(self):
        pass


#-------------------------------------- Draw Functions --------------------------------------#

# Explanation of emoji names:
# - each emoji is identified by the tile terrain & color (light or dark), and the piece on it
# - ordering: terrain + color + piece side + piece type
# - terrain and piece type are excluded if default ("normal" and "army," respectively)
# - color is excluded for capitals (which are always dark). piece info is excluded if no piece

# board_to_message
# takes a casashee board state and returns a message made of custom emoji representing the board,
# using the emoji name->id dictionary to supply emoji ids based on name
def board_to_message(board, id_dict):
    message = ""
    for row in board:
        for tile in row:
            emoji_name = tile_to_emoji_name(tile)
            message += f"<:{emoji_name}:{id_dict[emoji_name]}>"
        message += "\n" # create next row of tiles

    return message

# tile_to_emoji_name
# takes a tile and, using naming rules above, returns the matching custom emoji name
def tile_to_emoji_name(tile):
    # default terrain is normal
    terrain_name = "" if tile.terrain=="normal" else tile.terrain
    color_name = tile.color
    # empty tiles don't need piece description
    piece_name = "" if tile.piece==None else piece_to_emoji_name(tile.piece)

    return terrain_name + color_name + piece_name

def piece_to_emoji_name(piece):
    side_name = piece.side
    # default piece type is army
    type_name = "" if piece.type=="army" else piece.type

    return side_name + type_name
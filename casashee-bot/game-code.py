# ! to do list:
# - make sure message formatting is correct
# - unit tests!!
 
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
        return f"{'mo' if self.side=='m' else 'zaha'} {self.type}"
# Examples
z_army = Piece("z","army")
m_camp = Piece("m","camp")
m_tower = Piece("m","tower")

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
        return f"{self.terrain} tile with {'no' if self.piece==None else str(self.piece)} piece"
# Examples
normal_m_camp = Tile(0,0,piece=m_camp)
capital = Tile(5,2,"capital")
hill_z = Tile(2,4,"hill",z_army)

# A Board is a 2d list of Tiles
# Examples:
initial_board = []
for r in range(6):
    initial_board.append([])
    for c in range(6):
        temp_tile = Tile(r,c)

        if r==0:
            # add pieces to each side's first row
            temp_tile.piece = Piece("m")
            # add the capital to the correct tile
            if c==3: temp_tile.terrain = "capital"
        elif r==5:
            # add pieces to each side's first row
            temp_tile.piece = Piece("z")
            # add the capital to the correct tile
            if c==2: temp_tile.terrain = "capital"
        # add hills to the correct tiles
        elif r==2:
            if c==2 or c==5: temp_tile.terrain = "hill"
        elif r==3:
            if c==0 or c==3: temp_tile.terrain = "hill"

        initial_board[r].append(temp_tile)


#-------------------------------------- Draw Functions --------------------------------------#

# Explanation of emoji names:
# - each emoji is identified by the tile terrain & color (light or dark), and the piece on it
# - ordering: terrain + color + piece side + piece type
# - terrain and piece type are excluded if default ("normal" and "army," respectively)
# - piece info is excluded if no piece

# board_to_message
# takes a casashee board state and returns a message made of custom emoji representing the board,
# using the emoji name->id dictionary to supply emoji ids based on name
def board_to_message(board, id_dict) -> str:
    message = ""
    for row in board:
        for tile in row:
            emoji_name = tile_to_emoji_name(tile)
            message += f"<:{emoji_name}:{id_dict[emoji_name]}>"
        message += "\n" # create next row of tiles

    return message

# tile_to_emoji_name
# takes a tile and, using naming rules above, returns the matching custom emoji name
def tile_to_emoji_name(t: Tile) -> str:
    # default terrain is normal
    terrain_name = "" if t.terrain=="normal" else t.terrain
    color_name = t.color
    # empty tiles don't need piece description
    piece_name = "" if t.piece==None else piece_to_emoji_name(t.piece)

    return terrain_name + color_name + piece_name

# piece_to_emoji_name
# takes a piece and, using naming rules above, returns a string to be used in a tile's custom emoji name
def piece_to_emoji_name(p: Piece) -> str:
    side_name = p.side
    # default piece type is army
    type_name = "" if p.type=="army" else p.type

    return side_name + type_name


#-------------------------------------- Move Functions --------------------------------------#

# move_piece
# move a piece from original Tile to target Tile

# camp_switch
# camp an army or uncamp a camp
# You are going to tile a room whose dimensions are length by width feet. There are
# twelve tiles per box, each 1 foot by 1 foot. How many boxes of tiles do you need? You
# can only buy full boxes, not a partial box.
# You also want to buy 10% more tiles than you need in order to handle chips, breakage,
# and mess-ups. How many total boxes will you buy?

import math

# length_room_byfeet= 13
# width_room_byfeet=10
def tilesneeded(length_room_byfeet,width_room_byfeet):
    boxtiles1by1foot=12
    room_tiles=length_room_byfeet*width_room_byfeet
    alltiles= room_tiles+(room_tiles*0.1)
    box_needed=math.ceil(alltiles/boxtiles1by1foot)

    return box_needed


print(tilesneeded(10,13))
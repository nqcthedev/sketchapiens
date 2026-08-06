# -*- coding: utf-8 -*-
"""V16 Winter — (subject, framing, background, text) cho tung shot.
framing: m=medium w=wide c=close-up d=high-angle u=low-angle f=diagram
bg: white ivory grey snow | navy black cold cave | fire
"""

M = ("the recurring modern guy, the same plain black-outline STICK FIGURE with a plain round "
     "BALD white head and NO hair (just a simple face), a bare thin stick-line body (NO "
     "clothing, NO filled body shape), thin noodle arms and legs, simple rounded mitten hands "
     "and small oval feet,")
A = ("the recurring caveman, the same plain black-outline stickman with a messy scribbly tuft "
     "of short spiky dark doodle hair on top of the head, wearing a simple ragged brown "
     "animal-hide smock as a flat brown shape covering the torso, barefoot with small white "
     "oval feet,")
AF = ("the recurring ancient woman, the same plain black-outline stickman with long dark hair "
      "tied back, wearing a simple brown fibre wrap, barefoot with small white oval feet,")

SHOTS = [
# ── ĐỢT 1 · shot 001-045 — HOOK + ba câu trả lời + mở phần áo quần ───────────
# 001
(M + " standing calmly with one mitten hand reaching up and resting flat on the back of his "
   "own neck, calm neutral face, eyes looking slightly sideways.", "c", "white", ""),
# 002
(M + " with his hand still on the back of his neck, eyes closed in mild contentment, three "
   "tiny curved warm-orange heat lines rising from under his hand.", "c", "white", ""),
# 003
(M + " shrugging with both mitten hands turned up and palms open, thin eyebrows raised, a "
   "blank deadpan straight mouth.", "m", "white", ""),
# 004
("three simple flat icons floating in a neat row with a big bold RED X drawn over each one: a "
 "small orange campfire, a simple grey dumbbell, and an empty white thought bubble. No people "
 "in the frame.", "f", "white", ""),
# 005
(M + " standing on the left with a calm face, and one tall plain flat grey vertical wall slab "
   "running from the top to the bottom of the frame just to his right, three tiny blue "
   "snowflakes drifting on the far side of it.", "w", "grey", ""),
# 006
("one tall plain flat grey vertical wall slab standing in the middle of the frame, and a small "
 "plain black-outline stickman builder with a tiny grey trowel in one mitten hand walking away "
 "from it toward the edge of the frame, seen from behind.", "w", "white", ""),
# 007
("a simple flat brown winter coat hanging by its collar on a small black wall hook, drawn "
 "large and centred, with a simple flat brown door outline behind it. No people in the frame.",
 "m", "white", ""),
# 008
("one big round thermostat dial drawn very large in the centre of the frame, flat white face "
 "with a clean black outline, a short black needle pointing up, and a bold black number on the "
 "dial face. No people in the frame.", "f", "white",
 'a large bold black number "72" printed clearly on the dial face.'),
# 009
("the same big round thermostat dial drawn large and centred, with a small flat yellow sun "
 "doodle floating to its left and a small flat blue snowflake doodle floating to its right, a "
 "thin black arrow curving from the snowflake round to the sun. No people in the frame.", "f",
 "white", ""),
# 010
(M + " standing small at the bottom of the frame looking up at one enormous bold black "
   "percentage figure that fills most of the space above him.", "u", "ivory",
 'one enormous bold black "90%" filling the upper two thirds of the frame.'),
# 011
(M + " standing relaxed with a calm content face and both mitten hands loose at his sides, a "
   "tall plain flat dark wall slab at the very edge of the frame behind him with two tiny blue "
   "snowflakes on its far side.", "m", "fire", ""),
# 012
("three simple flat icons floating in a neat row, each dissolving into a few loose doodle "
 "specks, with one enormous bold RED X drawn straight across all three: a tall grey wall slab, "
 "a brown coat, and a round thermostat dial. No people in the frame.", "f", "white", ""),
# 013
(M + " standing alone in the middle of a completely empty frame, both thin noodle arms wrapped "
   "tightly across his own chest, shoulders hunched high, nervous wavy mouth, inner eyebrows "
   "raised, three short white speed lines slanting past him.", "w", "cold", ""),
# 014
("one big round clock face drawn very large and centred, white face with a clean white "
 "outline, two black hands, and only a few hour marks around the rim. No people in the frame.",
 "f", "cold", ""),
# 015
("a small flat white desk calendar page with a bold RED X drawn across it sitting low in the "
 "frame, and one enormous bold white word printed across the space above it. No people in the "
 "frame.", "f", "navy", 'one enormous bold white ALL-CAPS word "HOURS" filling the upper half.'),
# 016
("one long horizontal black timeline line running the full width of the frame with a row of "
 "many tiny plain black-outline stickmen standing along it, evenly spaced, all identical and "
 "very small.", "w", "ivory", ""),
# 017
("the same long horizontal black timeline line running the full width of the frame with tiny "
 "stickmen along it, and a flat pale blue band shading almost the entire line from the far "
 "left up to a small black mark near the right end.", "w", "ivory", ""),
# 018
(M + " drawn small near the bottom of a large empty frame, arms and legs flung out as if he "
   "has just been dropped from above, surprised wide round eyes and an open O mouth, a few "
   "tiny white snowflakes around him.", "d", "navy", ""),
# 019
(M + " drawn small, sitting hunched on the ground with his knees pulled up and his head "
   "lowered, arms wrapped around his shins, a tiny white snowflake landing on his shoulder.",
 "w", "snow", ""),
# 020
(M + " standing calmly in the centre, with a small flat white pillow doodle floating to his "
   "left under a bold RED X and a small flat brown snail doodle floating to his right under a "
   "second bold RED X.", "m", "white", ""),
# 021
(M + " shivering with his arms wrapped around himself and a nervous wavy mouth, a small flat "
   "YELLOW lightbulb glowing brightly right above his head.", "m", "snow", ""),
# 022
(A + " standing upright and still in the very middle of a large empty frame, small in the "
   "frame, calm steady deadpan face, both mitten hands at his sides.", "w", "snow", ""),
# 023
(M + " standing large on the right side of the frame, and a long receding line of many tiny "
   "plain black-outline stickmen standing shoulder to shoulder stretching away from him to the "
   "far left edge, each one smaller than the last.", "w", "ivory", ""),
# 024
("a long line of many tiny plain black-outline stickmen stretching from the right edge of the "
 "frame to the left, each one smaller and fainter than the last, ending in one large bold "
 "black question mark at the far left. No large character in the frame.", "w", "ivory",
 'one large bold black question mark "?" at the left end of the line.'),
# 025
("one small flat green sprout with two round leaves pushing up out of a short flat brown ground "
 "mark, drawn large and centred, with a small flat yellow sun doodle above it. No people in the "
 "frame.", "m", "white", ""),
# 026
("a neat row of many small flat GREEN check marks filling the middle band of the frame, all "
 "identical and evenly spaced. No people in the frame.", "f", "white", ""),
# 027
(M + " standing large and centred, both mitten hands pointing at his own chest, thin eyebrows "
   "raised, a small confident half smile.", "m", "white",
 'a short bold black ALL-CAPS word "YOU" on a small red tag beside him.'),
# 028
(M + " standing small in a large empty frame with his arms wrapped around himself, and one "
   "enormous bold white question mark rising behind him and filling most of the frame, a few "
   "tiny white snowflakes drifting.", "w", "snow", ""),
# 029
("one enormous bold black numeral drawn in the very centre of an otherwise completely empty "
 "frame. No people in the frame.", "f", "ivory",
 'one enormous bold black numeral "3" filling the middle of the frame.'),
# 030
(A + " standing on the right, and one large flat black numeral in a simple circle badge "
   "floating on the left side of the frame.", "m", "white",
 'a large bold black numeral "1" inside a simple black circle.'),
# 031
(A + " lifting a simple flat brown animal hide up over his own shoulders with both mitten "
   "hands, calm focused face.", "m", "white", ""),
# 032
("one large flat black numeral in a simple circle badge on the left of the frame, and a simple "
 "flat dome-shaped shelter outline with a small dark doorway on the right. No people in the "
 "frame.", "f", "white", 'a large bold black numeral "2" inside a simple black circle.'),
# 033
(A + " standing inside a simple flat dome-shaped shelter outline that arches over him, calm "
   "face, both mitten hands at his sides.", "m", "white", ""),
# 034
("one large flat black numeral in a simple circle badge drawn very large and centred, with one "
 "small flat ORANGE flame doodle burning quietly inside the loop of the numeral. No people in "
 "the frame.", "f", "white", 'a large bold black numeral "3" inside a simple black circle.'),
# 035
(A + " standing upright and still with both mitten hands at his sides and a calm deadpan "
   "face, wearing only the small brown hide smock, with three tiny white snowflakes drifting "
   "past him and no shelter anywhere in the frame.", "w", "cold", ""),
# 036
(A + " standing still and centred, with one small bright flat ORANGE flame doodle drawn "
   "glowing in the middle of his chest and a few short orange glow lines radiating out from it.",
 "m", "navy", ""),
# 037
("one long thin black arrow curving forward from the left of the frame and looping around to "
 "point back at a small flat red bookmark tag on the right. No people in the frame.", "f",
 "white", ""),
# 038
("three simple flat icons floating in a neat row, a brown coat, a dome shelter outline and a "
 "small orange flame, with one bold RED circle drawn around the flame only. No people in the "
 "frame.", "f", "white", ""),
# 039
(M + " standing still and centred with a calm face, one small bright flat ORANGE flame doodle "
   "glowing in the middle of his chest, faint orange glow lines around it.", "m", "navy", ""),
# 040
(M + " with surprised wide round eyes and an open O mouth, both mitten hands raised slightly, "
   "leaning back a little.", "c", "white", ""),
# 041
("a plain black-outline stickman with a round bald white head wearing a simple flat blue "
 "short-sleeved t-shirt, standing relaxed with a calm content half smile, several small flat "
 "white snowflakes drifting around him.", "m", "snow", ""),
# 042
("the same plain black-outline stickman in the simple flat blue short-sleeved t-shirt giving "
 "one cheerful thumbs up with a mitten hand, a small easy smile, snowflakes still drifting "
 "around him.", "m", "snow",
 'a short bold white ALL-CAPS word "FINE" on a small red tag beside him.'),
# 043
(M + " looking sideways with smug half-lidded eyes and a flat straight deadpan mouth, arms "
   "folded across his chest.", "c", "white", ""),
# 044
(A + " standing on the right, and one large flat black numeral in a simple circle badge "
   "floating on the left side of the frame.", "m", "white",
 'a large bold black numeral "1" inside a simple black circle.'),
# 045
("a simple flat side-view diagram drawn large and centred: one horizontal flat pink skin band "
 "at the bottom, one flat brown hide layer resting above it, and open space above that, with "
 "two short thin black arrows pointing up out of the skin and stopping at the hide layer. No "
 "people in the frame.", "f", "white", ""),

# ── ĐỢT 2 · shot 046-110 — chấy/niên đại · áo không sinh nhiệt · xây nhà · lò trong người ──
# 046
(M + " holding up one mitten hand with a single finger raised, one thin eyebrow up, a small "
   "knowing half smile.", "c", "white", ""),
# 047
("three simple flat objects floating in a neat row, each one crumbling away into a few loose "
 "doodle specks at its lower edge: a small patch of brown fur, a flat tan animal hide, and a "
 "small spool of thread. No people in the frame.", "f", "white", ""),
# 048
("one small black wall hook drawn large and centred with nothing hanging on it, and a faint "
 "black DOTTED outline of a coat floating empty beside the hook. No people in the frame.",
 "m", "white", ""),
# 049
("the same faint black DOTTED empty outline of a coat drawn large and centred, with one bold "
 "RED X drawn straight across it. No people in the frame.", "f", "white", ""),
# 050
("one small flat white calendar page on the left of the frame with a large black question mark "
 "above it, and one large flat GREEN check mark on the right. No people in the frame.", "f",
 "white", 'a short bold black ALL-CAPS phrase "WE CAN" on a small red tag under the check mark.'),
# 051
("one cute flat brown louse drawn very large and centred, a simple rounded body in flat solid "
 "brown with six tiny legs and a little friendly face with two big round eyes. No people in "
 "the frame.", "f", "white", ""),
# 052
("two cute flat lice sitting side by side and drawn large, one in flat solid brown and one in "
 "flat solid grey, each a simple rounded body with six tiny legs and a little friendly face. "
 "No people in the frame.", "f", "tan", ""),
# 053
("a large simple round white head with a messy scribbly tuft of dark doodle hair on top seen "
 "from the side, and one cute flat brown louse with a little face sitting among the hair "
 "strands, drawn clearly. No body below the shoulders.", "c", "tan", ""),
# 054
("one cute flat grey louse with a little face drawn large on the left, and a small patch of "
 "messy scribbly dark doodle hair on the right with one bold RED X drawn across the hair "
 "patch, a thin black arrow from the louse toward the hair stopping at the X. No people in the "
 "frame.", "f", "tan", ""),
# 055
("one cute flat grey louse with a little face sitting comfortably inside a soft fold of flat "
 "brown cloth, drawn large and centred. No people in the frame.", "m", "tan", ""),
# 056
("one cute flat grey louse with a little face on a fold of flat brown cloth at the top of the "
 "frame, and a flat pink horizontal skin band at the bottom, with one short thin black arrow "
 "curving from the louse down to the skin band and a second thin arrow curving back up. No "
 "people in the frame.", "f", "tan", ""),
# 057
("one long horizontal black timeline line across the middle of the frame with two small black "
 "tick marks on it: a tiny brown coat icon sitting above the left tick and a tiny grey louse "
 "icon sitting above the right tick, and the whole stretch of line to the left of the coat "
 "shaded out flat grey. No people in the frame.", "w", "tan", ""),
# 058
("one simple black Y-shaped branching line drawn large and centred like a family tree, with "
 "one cute flat brown louse at the tip of the left branch and one cute flat grey louse at the "
 "tip of the right branch, and a small black dot at the fork. No people in the frame.", "f",
 "tan", ""),
# 059
("one long horizontal black timeline line across the frame with a single bold black tick mark "
 "and one large bold black number printed above it. No people in the frame.", "w", "ivory",
 'one large bold black number "80,000" printed above the tick mark.'),
# 060
("the same long horizontal black timeline line with a flat pale blue band shading a wide "
 "stretch of it between two bold black tick marks, and one large bold black number printed "
 "above the far tick. No people in the frame.", "w", "ivory",
 'one large bold black number "170,000" printed above the far tick mark.'),
# 061
("one simple flat brown coat displayed on a small plain grey museum pedestal, drawn large and "
 "centred, with a tiny black rope barrier post beside it. No people in the frame.", "m",
 "white", ""),
# 062
("one simple flat brown coat drawn large on the right, one cute flat grey louse drawn small on "
 "the left, and one thin black arrow running from the louse to a small white date tag hanging "
 "on the coat. No people in the frame.", "f", "white", ""),
# 063
("one simple flat brown coat on the left with a bold RED X drawn across it, and one cute flat "
 "grey louse on the right inside a clean GREEN circle. No people in the frame.", "f", "white", ""),
# 064
("one simple flat brown coat drawn very large and centred, with a flat GREEN check mark "
 "floating beside its left shoulder and a bold RED X floating beside its right shoulder. No "
 "people in the frame.", "f", "snow", ""),
# 065
("one simple flat brown coat hanging alone in the middle of a completely empty frame with one "
 "large bold black numeral beside it. No people in the frame.", "m", "snow",
 'one large bold black numeral "0" beside the coat.'),
# 066
("one simple flat brown coat drawn large and centred with three short curved orange heat lines "
 "rising from it, and one bold RED X drawn across the heat lines only. No people in the frame.",
 "f", "snow", ""),
# 067
("one simple flat pale blue folded blanket sitting inside a plain rectangular freezer box "
 "outline with an open door, drawn large and centred. No people in the frame.", "m", "snow", ""),
# 068
("the same simple flat pale blue folded blanket drawn very large and centred with one small "
 "flat white snowflake resting on top of it. No people in the frame.", "m", "snow", ""),
# 069
("a simple flat side-view diagram drawn large and centred: one vertical flat pink body band on "
 "the left, one flat brown coat layer just outside it, and open space to the right, with three "
 "short thin orange arrows creeping slowly out through the coat layer, drawn short and thin to "
 "show a slow leak. No people in the frame.", "f", "snow", ""),
# 070
("one large flat black numeral in a simple circle badge drawn large and centred in an "
 "otherwise empty frame. No people in the frame.", "f", "white",
 'a large bold black numeral "2" inside a simple black circle.'),
# 071
(M + " sitting relaxed on a small plain chair inside one simple square room outline drawn with "
   "clean thin lines, calm content face.", "w", "grey", ""),
# 072
(A + " placing one simple flat grey stone block onto a low stack of blocks with both mitten "
   "hands, focused face.", "m", "white", ""),
# 073
("one tall plain flat grey wall slab drawn large and centred with one bold RED X drawn across "
 "it. No people in the frame.", "f", "snow", ""),
# 074
("one simple flat pale blue rounded blob with a small cartoon weight symbol on it and one "
 "thick black arrow pointing straight DOWN beneath it, drawn large and centred. No people in "
 "the frame.", "f", "snow", ""),
# 075
("one simple square room outline drawn with clean thin black lines, with three thin ORANGE "
 "arrows curving upward in the top half and three thin BLUE arrows curving downward in the "
 "bottom half, and a flat pale blue pool of colour settled along the floor. No people in the "
 "frame.", "f", "snow", ""),
# 076
("one simple square room outline drawn with clean thin black lines, tilted slightly, with a "
 "flat pale blue liquid pool settling into the lowest corner and a few small blue droplets "
 "running down toward it. No people in the frame.", "f", "snow", ""),
# 077
("a simple flat side-view cutaway diagram drawn with clean white lines: a low sunken entrance "
 "tunnel on the left running below floor level, rising up into a small raised sleeping "
 "platform on the right. No people in the frame.", "f", "tan", ""),
# 078
("the same simple flat side-view cutaway diagram with the sunken entrance tunnel on the left, "
 "and a flat pale blue mass rolling down the slope and settling along the bottom of the "
 "tunnel, with two thin blue arrows pointing down into it. No people in the frame.", "f",
 "tan", ""),
# 079
(A + " lying peacefully asleep on the raised sleeping platform on the right of a simple flat "
   "side-view cutaway diagram, eyes closed with a tiny smile, while a flat pale blue mass sits "
   "trapped in the sunken tunnel far below and to the left, a thin blue arrow stopping short "
   "with a small red line.", "w", "tan", ""),
# 080
("one simple flat white landmass shape drawn large and centred with a clean black outline and "
 "one bold RED map pin planted near its top edge, and a small dashed red circle around the "
 "pin. No people in the frame.", "f", "white", ""),
# 081
("a simple flat side-view cutaway diagram drawn with clean white lines showing a long low "
 "entrance tunnel, with a thin white measuring line and two end arrows running along the "
 "tunnel's length and a short label above it. No people in the frame.", "f", "cave",
 'a small bold white ALL-CAPS label "3 m" above the measuring line.'),
# 082
("the same simple flat side-view cutaway diagram drawn with clean white lines, with one thick "
 "white arrow pointing straight DOWN from the living floor level to the lower tunnel floor and "
 "a short dashed white level line at each height. No people in the frame.", "f", "cave", ""),
# 083
("a simple flat side-view cutaway outline of a sunken entrance tunnel drawn large and centred, "
 "with one small grey cartoon gear wheel floating beside it under a bold RED X. No people in "
 "the frame.", "f", "tan", ""),
# 084
("one simple flat pale blue rounded blob with a small grumpy cartoon face on it, sliding down "
 "a short black slope with one thick black arrow pointing straight DOWN, drawn large and "
 "centred. No people in the frame.", "f", "tan", ""),
# 085
("one simple square room outline drawn with clean thin black lines with orange arrows curving "
 "up one side and blue arrows curving down the other in a closed loop, and one small empty "
 "white label tag beside the loop holding a single black question mark. No people in the "
 "frame.", "f", "tan", ""),
# 086
("one large cartoon magnifying glass with a black handle held over a simple flat dome-shaped "
 "shelter outline, drawn large and centred. No people in the frame.", "m", "white", ""),
# 087
("one simple flat dome-shaped shelter outline drawn large and centred with a ragged black hole "
 "torn open through the middle of it and empty space showing through. No people in the frame.",
 "f", "white", ""),
# 088
("one simple flat dome-shaped shelter outline drawn large and centred with one large bold "
 "black numeral floating inside it. No people in the frame.", "f", "white",
 'one large bold black numeral "0" inside the shelter.'),
# 089
("one simple square room interior outline drawn with clean white lines, completely empty "
 "inside, with a lot of dark empty space. No people in the frame.", "w", "cave", ""),
# 090
(A + " sitting cross-legged and small beside one small flat ORANGE campfire inside a simple "
   "square room interior outline drawn with clean white lines, warm orange glow lines spreading "
   "from the fire, calm face.", "w", "cave", ""),
# 091
("one simple flat brown coat on the left and one simple flat dome-shaped shelter outline on "
 "the right, with a single wide black bracket drawn underneath joining them both to one small "
 "red tag below. No people in the frame.", "f", "white",
 'a short bold white ALL-CAPS word "SAME" on the small red tag.'),
# 092
("two large cupped mitten hands drawn close together in the centre of the frame, holding one "
 "small warm ORANGE glow between them with a few short orange glow lines. No full character in "
 "the frame.", "c", "white", ""),
# 093
("one enormous bold black question mark standing alone in the middle of one simple square room "
 "outline drawn with clean thin black lines, the rest of the frame completely empty. No people "
 "in the frame.", "w", "white", ""),
# 094
("one enormous bold black question mark drawn in the centre of the frame with a soft warm "
 "ORANGE glow and a few short orange glow lines radiating out from behind it. No people in the "
 "frame.", "f", "white", ""),
# 095
(M + " standing large and centred pointing at his own chest with both mitten hands, a calm "
   "confident half smile, one small bright flat orange flame doodle glowing in the middle of "
   "his chest.", "m", "fire", ""),
# 096
(M + " standing with a flat straight deadpan mouth and half-lidded eyes, one small orange "
   "flame doodle glowing at his chest and one tiny black clock face floating beside his "
   "shoulder.", "m", "white", ""),
# 097
(M + " drawn large and centred with three small flat ORANGE flame doodles glowing inside the "
   "line of his torso, calm neutral face.", "m", "tan", ""),
# 098
("one simple flat cartoon thermometer drawn large and upright in the centre of the frame with "
 "a red bulb and the red column stopped exactly at one bold black tick mark, and one long "
 "perfectly flat horizontal black line running out sideways from that mark to both edges of "
 "the frame. No people in the frame.", "f", "tan", ""),
# 099
("one simple flat white plate holding a few pieces of cute flat food on the left, one thin "
 "black arrow pointing right to a small black running-legs icon, and one bold RED X drawn "
 "across the running-legs icon. No people in the frame.", "f", "tan", ""),
# 100
("one simple black body outline drawn large and centred with a few flat ORANGE flame doodles "
 "inside it and four wavy orange heat lines rising up out of the top of the outline and off "
 "the top edge of the frame. No people in the frame.", "f", "tan", ""),
# 101
(M + " standing large and centred with a flat straight deadpan mouth and half-lidded eyes, one "
   "small black cast-iron furnace door with a tiny handle drawn on the middle of his chest and "
   "warm orange light glowing out around its edges.", "m", "fire", ""),
# 102
("one large flat black numeral in a simple circle badge on the left of the frame and one large "
 "bold black question mark on the right, with a thin black arrow between them. No people in "
 "the frame.", "f", "white", 'a large bold black numeral "3" inside a simple black circle.'),
# 103
("one simple flat brown coat on the left with a bold RED X drawn across it and one simple flat "
 "dome-shaped shelter outline on the right with a second bold RED X drawn across it, drawn "
 "with clean white lines. No people in the frame.", "f", "cold", ""),
# 104
("one large round burner control dial drawn very large and centred with a white face and a "
 "short black needle turned far to the right, and one flat ORANGE flame doodle above it drawn "
 "big and bright with a small thin arrow curving upward beside it. No people in the frame.",
 "f", "fire", ""),
# 105
("one simple flat white map shape of the South American continent with a clean black outline, "
 "drawn large and centred, with one bold RED map pin planted at its very bottom tip and a "
 "small dashed red circle around the pin. No people in the frame.", "f", "white", ""),
# 106
("four or five small flat pale island shapes scattered across the lower half of the frame "
 "drawn with clean white lines, with several long white speed lines slanting hard across the "
 "frame from one side to show wind. No people in the frame.", "w", "cold", ""),
# 107
("one simple flat cartoon thermometer drawn large and upright with a pale blue column stopped "
 "just above one bold white tick mark, and one small flat white snowflake floating beside the "
 "mark. No people in the frame.", "f", "cold", ""),
# 108
(A + " standing small and upright on one small flat pale island shape in the middle of a large "
   "empty frame, calm steady deadpan face.", "w", "cold", ""),
# 109
(A + " standing upright and still with both mitten hands at his sides and a calm deadpan face, "
   "wearing only one very small simple brown hide wrap at the waist and nothing else, with "
   "several small white snowflakes drifting around him.", "m", "cold", ""),
# 110
(M + " with his arms folded across his chest, smug half-lidded eyes, one thin eyebrow raised "
   "high and a flat straight sceptical mouth.", "c", "sage", ""),

# ── ĐỢT 3 · shot 111-185 — Darwin · Yaghan · mỡ nâu · máy quét · KẾT ────────
# 111
(M + " with folded arms and half-lidded sceptical eyes, one large white thought bubble above "
   "his head holding a neat stack of flat brown furs.", "m", "sage", ""),
# 112
("one simple flat open book on the left with a thin black arrow stretching upward out of its "
 "pages to show exaggeration, and one plain black body outline on the right with a bold RED X "
 "drawn across it. No people in the frame.", "f", "sage", ""),
# 113
(M + " tilting his head slightly with one mitten hand raised palm-up in a small conceding "
   "gesture, a flat straight deadpan mouth, eyebrows level.", "c", "white", ""),
# 114
("a plain black-outline stickman scholar with a large bushy flat grey beard covering his lower "
 "face and a bald round white head, holding one small white notebook open in his mitten hands "
 "and looking down at it with a calm focused face.", "m", "white", ""),
# 115
("one simple flat brown sailing ship with two plain white sails, drawn large and centred, "
 "floating on one short flat band of darker water along the bottom of the frame. No people in "
 "the frame.", "w", "cold", ""),
# 116
(AF + " sitting upright in one small simple flat brown canoe drawn on the lower left, holding "
    "one tiny wrapped bundle close against her, with the tall hull of a flat brown sailing ship "
    "rising along the right edge of the frame.", "w", "cold", ""),
# 117
("many short slanting white sleet dashes falling steadily across the whole frame at the same "
 "angle, evenly spaced, with nothing else in the frame. No people in the frame.", "w", "navy", ""),
# 118
(AF + " standing upright holding one tiny wrapped bundle against her shoulder, drawn with clean "
    "white lines, several short slanting white sleet dashes landing on her shoulders and on the "
    "bundle, calm steady face.", "m", "navy", ""),
# 119
("one large close-up of a single white sleet dash turning into one small round clear water "
 "droplet, with one tiny curl of white steam rising off it, drawn very large and centred. No "
 "people in the frame.", "c", "navy", ""),
# 120
(AF + " standing perfectly still and small in the middle of a large empty frame, drawn with "
    "clean white lines, both feet planted, calm steady deadpan face, white sleet dashes falling "
    "all around her.", "w", "navy", ""),
# 121
(A + " standing upright drawn with clean white lines, with one small cartoon flexing-bicep icon "
   "floating beside him under a bold RED X.", "m", "cold", ""),
# 122
("one plain body outline drawn large and centred with clean white lines, with one small flat "
 "ORANGE engine block icon with a tiny chimney drawn glowing inside its chest instead of "
 "anything else. No face in the frame.", "f", "navy", ""),
# 123
("one simple flat white clipboard holding a small black line chart, drawn large and centred, "
 "with one small black stopwatch and one small black gas mask icon lying beside it. No people "
 "in the frame.", "f", "white", ""),
# 124
("one tall flat ORANGE bar rising from the bottom of the frame with one enormous bold black "
 "percentage figure printed beside it. No people in the frame.", "f", "ivory",
 'one enormous bold black "160%" printed beside the tall bar.'),
# 125
("a simple flat bar chart with exactly two bars side by side, one shorter flat grey bar on the "
 "left and one taller flat ORANGE bar on the right, with a small bold black label under each. "
 "No people in the frame.", "f", "white",
 'a small bold black "100%" under the grey bar and "160%" under the orange bar.'),
# 126
("one small cartoon vibration symbol made of short curved shake lines drawn large and centred, "
 "with one bold RED X drawn across it, drawn with clean white lines. No people in the frame.",
 "f", "snow", ""),
# 127
(M + " shivering hard with short white shake lines on both sides of his body, a nervous wavy "
   "mouth and a sweat drop, drawn with clean white lines.", "m", "snow",
 'a short bold white ALL-CAPS word "EMERGENCY" on a small red tag beside him.'),
# 128
("one simple flat cartoon battery drawn large and centred with clean white lines, almost fully "
 "drained to empty with one thin red segment left, and a few short white shake lines and tiny "
 "friction sparks around it. No people in the frame.", "f", "snow", ""),
# 129
(A + " sitting cross-legged and perfectly still with both mitten hands resting on his knees "
   "and a calm closed-eye face, drawn with clean white lines, with a soft warm ORANGE glow and "
   "a few orange glow lines spreading out from his chest.", "m", "navy", ""),
# 130
("one small rounded flat BROWN tissue blob with a clean outline drawn large and centred, with "
 "one thin black pointer line running from it to a small white label tag. No people in the "
 "frame.", "f", "white",
 'a short bold black ALL-CAPS label "BROWN FAT" on the small white tag.'),
# 131
("one large rounded flat PALE YELLOW fat blob with a clean black outline drawn large and "
 "centred, with one bold RED X drawn across it. No people in the frame.", "f", "white", ""),
# 132
("one flat PALE YELLOW warehouse building with a wide roll-up door standing open and several "
 "small stacked brown boxes visible inside, drawn large and centred. No people in the frame.",
 "m", "white", ""),
# 133
("one small rounded flat BROWN tissue blob drawn large and centred with one bright flat ORANGE "
 "flame doodle burning on top of it and a few short orange glow lines. No people in the frame.",
 "f", "fire", ""),
# 134
("a simple flat left-to-right diagram drawn large: one small brown fuel droplet on the left, "
 "one thin black arrow, one rounded flat BROWN tissue blob in the middle, one thin black "
 "arrow, and three wavy ORANGE heat lines on the right. No people in the frame.", "f", "fire", ""),
# 135
("one simple cartoon flexing-arm muscle icon drawn large and centred with one bold RED X drawn "
 "across it. No people in the frame.", "f", "white", ""),
# 136
("one small squat cast-iron furnace with a little round door and a short chimney, drawn large "
 "and centred with a flat BROWN body and warm orange light glowing out around the door edges. "
 "No people in the frame.", "m", "fire", ""),
# 137
("one simple flat DNA double helix drawn large and upright in the centre of the frame with "
 "clean white lines and evenly spaced rungs. No people in the frame.", "f", "navy", ""),
# 138
(M + " standing on the right holding a small white clipboard and looking at it with a focused "
   "face, with two small icons floating on the left, one flat brown tissue blob and one flat "
   "white snowflake, joined by a short thin black bracket.", "m", "white", ""),
# 139
("one simple flat DNA double helix drawn large and upright with clean white lines, with "
 "exactly one rung near the middle drawn in bold RED and a small dashed red circle around that "
 "one rung. No people in the frame.", "f", "navy", ""),
# 140
("one simple flat brown coat on the left with a bold RED X across it and one tall plain flat "
 "grey wall slab on the right with a second bold RED X across it. No people in the frame.",
 "f", "white", ""),
# 141
(A + " standing still and centred drawn with clean white lines, with one large bright flat "
   "ORANGE flame doodle burning in the middle of his chest and long orange glow lines "
   "radiating outward.", "m", "navy", ""),
# 142
("one large bright flat ORANGE flame doodle burning in the centre of the frame, with three "
 "small cute food icons around it, a little grey fish, a small brown shellfish and a few red "
 "berries, each with a thin white arrow pointing into the flame. No people in the frame.", "f",
 "navy", ""),
# 143
("one simple flat open white book drawn large and centred, with a small row of tiny "
 "black-outline stickmen printed across its open pages. No large character in the frame.",
 "m", "white", ""),
# 144
("one simple flat open white book lying at the bottom of the frame, and above it one plain "
 "oval hand mirror drawn large with clean white lines, showing one round bald white stickman "
 "head with surprised wide round eyes reflected in its glass.", "m", "navy", ""),
# 145
("a neat stack of three or four simple flat textbooks in muted colours drawn large and centred "
 "with clean black outlines. No people in the frame.", "m", "grey", ""),
# 146
("one small baby stickman doodle drawn large and centred, a round white head with one tiny "
 "curl of hair and a simple happy face, lying on a small white blanket, with one small rounded "
 "flat BROWN tissue blob drawn beside it and a thin black pointer line joining them.", "m",
 "sage", ""),
# 147
("one small baby stickman doodle on a small white blanket drawn large and centred, with a "
 "cartoon vibration symbol of short curved shake lines floating beside it under one bold RED "
 "X.", "m", "sage", ""),
# 148
("one small baby stickman doodle on a small white blanket drawn large and centred, with a soft "
 "warm ORANGE glow and a few short orange glow lines spreading gently around it.", "m", "fire",
 ""),
# 149
("one long horizontal black timeline line across the middle of the frame with three small "
 "rounded flat BROWN tissue blobs sitting along it, the left one large, the middle one small, "
 "and the right one gone and replaced by a faint dotted outline. No people in the frame.",
 "w", "white", ""),
# 150
("one plain adult body outline drawn large and centred, completely empty inside, with one "
 "large bold black numeral floating in the middle of the empty chest. No face in the frame.",
 "f", "sage", 'one large bold black numeral "0" inside the empty body outline.'),
# 151
(M + " lying flat on his back on a narrow white table sliding into the opening of one large "
   "plain grey ring-shaped scanner machine, calm neutral face.", "w", "grey", ""),
# 152
("one plain rounded body-scan silhouette drawn large and centred with clean white lines, "
 "completely dark and empty inside with no bright areas at all. No face in the frame.", "f",
 "black", ""),
# 153
("one large round thermostat dial drawn with clean white lines with its short needle turned "
 "far to the left, and one small flat white snowflake beside it, and the plain grey ring of a "
 "scanner machine visible at the edge of the frame. No people in the frame.", "f", "snow", ""),
# 154
("one plain rounded body-scan silhouette drawn large and centred with clean white lines, with "
 "several bright flat ORANGE patches glowing clearly across the upper chest, shoulders and "
 "neck areas and short orange glow lines around them. No face in the frame.", "f", "black", ""),
# 155
("one plain rounded body-scan silhouette with bright orange glowing patches drawn on the left, "
 "and one large bold white numeral on the right with one bold RED X drawn across the numeral. "
 "No face in the frame.", "f", "black",
 'one large bold white numeral "1" with a red X across it.'),
# 156
("one enormous bold white fraction printed across the centre of an otherwise completely empty "
 "frame, with a small row of tiny glowing orange dots beneath it. No people in the frame.",
 "f", "black", 'one enormous bold white "23 / 24" filling the middle of the frame.'),
# 157
("one plain body outline drawn large and centred with clean white lines, with one small squat "
 "furnace with a little round door drawn faintly inside its chest and a thin dashed white "
 "circle around the furnace. No face in the frame.", "f", "navy", ""),
# 158
("one small squat cast-iron furnace with a little round door drawn large and centred with "
 "clean white lines, the door shut and completely dark inside, with one thin white pull cord "
 "hanging beside it untouched. No people in the frame.", "m", "navy", ""),
# 159
("a plain black-outline stickman with a round bald white head wearing a simple flat blue "
 "short-sleeved t-shirt, standing relaxed with a calm content half smile, several small flat "
 "white snowflakes drifting around him.", "m", "snow", ""),
# 160
("the same plain black-outline stickman in the simple flat blue short-sleeved t-shirt standing "
 "calmly with his mitten hands at his sides, with one small cartoon flexing-bicep icon "
 "floating beside him under a bold RED X and one small sparkle icon under a second bold RED X.",
 "m", "snow", ""),
# 161
("one large round burner control dial with a white face and a short black needle turned far to "
 "the right, drawn large and centred, with one big bright flat ORANGE flame doodle burning "
 "above it. No people in the frame.", "f", "fire", ""),
# 162
("one large round burner control dial drawn with clean white lines with its short needle "
 "turned all the way to the left, and one very tiny pale flame doodle barely visible above it. "
 "No people in the frame.", "f", "snow", ""),
# 163
(M + " sitting relaxed on a small plain chair with a calm content face and both mitten hands "
   "resting easily, inside one simple square room outline drawn with clean thin lines.", "w",
 "grey", ""),
# 164
("one tall plain flat grey wall slab on the left and one simple flat brown coat hanging on a "
 "small hook on the right, drawn large. No people in the frame.", "f", "white", ""),
# 165
("one big round thermostat dial drawn very large and centred with a flat white face, a clean "
 "black outline, a short black needle and a bold black number on its face. No people in the "
 "frame.", "f", "white", 'a large bold black number "72" printed clearly on the dial face.'),
# 166
("one long horizontal black timeline line running the full width of the frame with a row of "
 "many small flat white snowflakes sitting evenly spaced along it. No people in the frame.",
 "w", "snow", ""),
# 167
("one small flat YELLOW lightning-bolt signal travelling along one long thin white line that "
 "runs across the frame, with two short white motion dashes trailing behind the bolt. No "
 "people in the frame.", "w", "navy", ""),
# 168
("one long thin white line running from the left of the frame and stopping dead against one "
 "tall plain flat wall slab in the middle, with one small flat yellow lightning-bolt signal "
 "crumpled at the point of contact and one bold RED X over the break, and empty space beyond "
 "the wall. No people in the frame.", "w", "navy", ""),
# 169
("one simple drooping cartoon arm icon hanging limp, drawn large and centred, with one bold "
 "RED X drawn across it. No people in the frame.", "f", "white", ""),
# 170
("one big round thermostat dial mounted flat on a plain wall panel, drawn large and centred "
 "with clean white lines, with one small flat GREEN check mark floating beside it. No people "
 "in the frame.", "f", "grey", ""),
# 171
(M + " standing large and centred with one mitten hand held out flat, palm up, a calm level "
   "deadpan face.", "m", "grey", ""),
# 172
("one simple cartoon boxing glove icon drawn large on the left with one bold RED X across it, "
 "and one flat white snowflake drawn large on the right, drawn with clean white lines. No "
 "people in the frame.", "f", "cold", ""),
# 173
("one very thick plain wall slab drawn large and centred with a warm ORANGE glow filling the "
 "space behind it and several short orange heat lines trapped inside, none of them getting "
 "past the wall. No people in the frame.", "f", "fire", ""),
# 174
("one plain body outline drawn large and centred with clean white lines, with one small "
 "burnt-out grey flame shape in the middle of its chest and one thin curl of grey smoke rising "
 "from it. No face in the frame.", "f", "navy", ""),
# 175
("one tall plain wall slab drawn large with clean white lines, with one small white sealed "
 "envelope resting unopened against its base and a thin white arrow stopping short at the "
 "wall. No people in the frame.", "w", "navy", ""),
# 176
("one small squat cast-iron furnace with a little round door drawn large and centred with "
 "clean white lines, unlit and dark inside, with one small white bell hanging beside it drawn "
 "perfectly still with no sound lines at all. No people in the frame.", "m", "navy", ""),
# 177
("two large cupped mitten hands drawn with clean white lines holding out one small bright flat "
 "ORANGE flame, offering it forward toward the edge of the frame. No full character in the "
 "frame.", "c", "navy", ""),
# 178
("one large cupped mitten hand drawn with clean white lines receiving one small round "
 "thermostat dial with a flat white face and a bold black number on it. No full character in "
 "the frame.", "c", "navy", 'a small bold black number "72" on the dial face.'),
# 179
(M + " standing alone and small in the middle of a very large empty frame, drawn with clean "
   "white lines, both mitten hands at his sides, a flat straight deadpan mouth.", "w", "navy", ""),
# 180
(M + " standing calmly with one mitten hand reaching up and resting flat on the back of his "
   "own neck, calm neutral face, eyes looking slightly sideways.", "c", "white", ""),
# 181
(M + " with his hand still on the back of his neck, eyes closed in mild contentment, three "
   "tiny curved warm-orange heat lines rising from under his hand.", "c", "white", ""),
# 182
("one large close-up of the back of a round white stickman head and neck drawn with clean "
 "white lines, with one small squat furnace shape drawn faintly showing through under the skin "
 "at the base of the neck and a thin dashed white circle around it.", "c", "navy", ""),
# 183
("one small squat cast-iron furnace with a little round door drawn large and centred with "
 "clean white lines, fully built and complete with every bolt and its short chimney in place, "
 "unlit and dark inside, with one small flat white snowflake resting on its lid.", "m", "navy",
 ""),
# 184
("one small squat cast-iron furnace drawn large and centred with clean white lines, unlit and "
 "complete, with one flat GREEN check mark floating beside it. No people in the frame.", "m",
 "navy", ""),
# 185
("one small squat cast-iron furnace drawn small in the very middle of an enormous empty frame, "
 "clean white lines, unlit and dark inside, with one single tiny white snowflake falling far "
 "away near the top edge and nothing else at all. No people in the frame.", "w", "navy", ""),
]

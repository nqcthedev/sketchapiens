# -*- coding: utf-8 -*-
"""V20 COLD — "What Did Ancient Humans Do When the Fire Went Out?"

    (line, kind, subj, text, bg, face)

kind : SCENE_A mot nguoi co dai | GROUP nhom | SCENE_N khong nguoi
       BEAST con vat ve CHI TIET | OBJ vat khoa hoc hien dai | CARD the
bg   : fire_side fire_ring ember frozen_ground night_open dig lab_cold map dawn white
face : flat shock tired worry scared asleep curious calm

⚠️ DUNG LAI TU DAU LAN THU BA — 21/08/2026.
   Bo shot cu (282) thuoc KICH BAN 1. Bo shot 426 thuoc KICH BAN 2.
   Ban 61 la kich ban thu ba, viet lai toan bo. Hai bo cu giu o
   _cu_shot_data_ban1.py va _cu_shot_data_kichban2.py

2.455 tu / 208 cau -> 320 shot. Audio 13:20 -> ~2,5 giay/shot.
Dong-shot sinh boi tools/chia_shot.py (co cong ghep-lai-khop-tung-ky-tu).

═══════════════════════════════════════════════════════════════════════════
NGON NGU HINH CUA V20 — day du o STYLE_HINH_V20.md
═══════════════════════════════════════════════════════════════════════════

1. 🔴 HAI NHIET DO MAU TREN CHINH THAN NGUOI — thu khong kenh nao co.
   Ben huong lua CAM AM, ben kia XANH LANH, ranh gioi doc than nguoi.
   Dai cam CO LAI dan theo bai:
     lua to (shot 96-160)      -> phu het mot ben nguoi
     lua thanh than (261-275)  -> con mot vet hep
     nguoi nam ria (272)       -> chi cham toi vai
     khung cuoi (320)          -> chi con dong o BAN TAY

2. TI LE 60 canh / 40 the. Doi thu: Ink 59% canh, Mack 64%. V17 cua kenh: 25% -> nguoc han.

3. ZOOM CHAM la mac dinh cho moi CARD va OBJ. Mot anh giu duoc 3-4 giay vi no dang bo vao.
   Do la ly do khong can 320 anh khac nhau tuyet doi.

4. MOT Y = MOT CHUOI 3-6 shot, khong phai mot dong loi = mot anh.

5. CON VAT ve CHI TIET hon nguoi rat nhieu (hoc Stickly). Nguoi van la que.

6. ⛔ KHONG CO NHAN VAT HIEN DAI. Lane "ve BAN" da bo 10/08.
   -> BERLIN ve bang CHO TRONG: gam giuong trong, khe sau tu, hoc ke.
      Co dau vet cho biet co nguoi tung chui vao. Rung ron hon ve thang.
   -> KHOA HOC HIEN DAI (Krauchi, Haskell, Samson) ve DO VAT, khong ve nguoi.
      Nhung VAN GIU hai nhiet do mau, de mat nguoi xem khong thay dut mach.

7. CO CHE SINH LY ve TREN THAN NGUOI CO DAI, khong ve thanh so do.
   Ban tay nam <-> ban tay mo. Hoi nong boc len khoi da. Khong bao gio ve mach mau cat ngang.
   ⚠️ V19 hong vi 62% khung la the.

8. ⛔ Khung nao cung phai qua duoc mot cau hoi:
   "che loi doc di, khung nay con noi duoc gi khong?"
   V18 tung co bieu do cot KHONG MOT CHU SO, can thang bang hai ben deu la "?".
"""

# ── NỀN RIÊNG CỦA V20 ─────────────────────────────────────────────────────
# ⚠️ KHÔNG sửa identity/style.py cho riêng một video. Khai ở đây, build_prompts.py
#    tự merge. Khi 2-3 video cùng dùng thì mới nâng lên file bản sắc.
# 🔴 Sáu nền này đều mang NGÔN NGỮ HAI NHIỆT ĐỘ MÀU của V20: một phía cam ấm,
#    một phía xanh lạnh. Dải cam CO LẠI dần từ fire_side -> ember -> dawn.
BG_THEM = {
 "fire_side": ("a small fire drawn as a wobbly orange shape with a yellow centre on one side of the "
               "frame, throwing a warm orange patch across flat brown ground, and on the opposite side "
               "of the frame a flat block of cold blue-grey with frost on the ground"),
 "ember":     ("a low bed of dull dark-red coals with no flame at all on one side, giving off only a "
               "small tight patch of dim orange, and the rest of the frame a flat block of cold "
               "blue-grey ground under almost-black navy"),
 "frozen_ground": ("one flat strip of pale frosted grey-brown ground filling the lower half, hard and "
               "bare with a few grey stones, under a flat block of cold blue-grey night sky"),
 "dig":       ("one flat block of dry cracked grey-brown mud filling most of the frame, a shallow "
               "squared-off pit cut into it with straight edges, under a flat pale sky"),
 "lab_cold":  ("a plain flat block of pale grey wall meeting a flat strip of pale floor, empty, with "
               "one edge of the frame tinted faintly warm and the opposite edge tinted faintly cold"),
 "dawn":      ("a flat band of pale grey-orange dawn sky low across the top, over one flat strip of "
               "frosted grey-brown ground, with the last dull red coals as one small shape"),
}

# ── KIND RIÊNG CỦA V20: cận một phần cơ thể, KHÔNG có mặt ────────────────
# V20 có trục BÀN TAY, nên 11 shot là cận bàn tay / cẳng tay / vai, gồm cả khung
# CUỐI CÙNG. Dùng SCENE_A thì prompt ép vẽ đầu, mắt, tóc, áo da vào khung chỉ có
# một bàn tay. Dùng SCENE_N thì NO_PERSON cấm luôn "no hands".
WHO_THEM = {
 "BODY": ("ONE part of a body only, drawn close: a hand, a forearm, a shoulder. "
          "NO head, NO face, NO eyes, NO hair anywhere in this frame. "
          "Hands and feet are small and SOLID WHITE like the head would be, never skin-coloured. "
          "Any sleeve or hem visible is ragged brown hide. Arms are thin crooked black lines. "),
}
KHONG_MAT = ("BODY",)   # engine bỏ khối FACE cho kind này

SHOTS = [

# ═════════════════ HOOK — 8 shot · CANH co dai, hai nhiet do mau xuat hien ngay ═════════════════
("The sun has just gone down.","SCENE_N","a low winter sun sitting right on a flat frozen horizon, the sky above it going from dull orange to deep blue","no text","night_open","flat"),
("Someone is looking for a place to lie down,","SCENE_A","he stands on frozen open ground with his hide pulled tight around him, looking down at the ground, deciding","no text","frozen_ground","tired"),
("close enough to the fire to reach it.","SCENE_A","he crouches an arm's length from a small fire, one side of him lit warm orange, the other side blue with cold","no text","fire_side","tired"),
("There is a whole winter night to get through before it gets light.","SCENE_N","a wide flat night sky full of small white stars over a dark empty plain, one tiny orange dot of fire far below","no text","night_open","flat"),
("And before sleep can come,","SCENE_A","he lies down on his side facing the fire, eyes still open, one shoulder orange and one shoulder blue","no text","fire_side","tired"),
("that person has to finish something they do not know they are doing.","SCENE_A","close on him lying still, eyes open, the warm orange edge running down the front of his body","no text","fire_side","curious"),
("It happens in the hands.","BODY","very close on one hand lying on the ground in firelight, fingers still curled shut","no text","fire_side","flat"),
("Hold on to that.","SCENE_N","the same closed hand alone in the frame, warm orange light on the knuckles, everything behind it dark","no text","fire_side","flat"),

# ═════════════════ BERLIN — 20 shot · ve bang CHO TRONG, khong nguoi hien dai ═════════════════
("But before we walk through that night,","SCENE_A","he lies beside the small fire, seen from a long way off across dark ground, very small in the frame","no text","night_open","asleep"),
("there is something you should know about freezing to death.","CARD","a plain thermometer drawn by hand with the liquid column dropped almost to the very bottom","no text","white","flat"),
("People picture someone lying down in the snow and quietly fading out.","SCENE_N","a smooth blank field of snow with one shallow dip pressed into it, soft blue shadow inside the hollow","no text","frozen_ground","flat"),
("The records do not say that.","CARD","a stack of plain paper case files tied with string, the top one open but blank","no text","white","flat"),
("For sixteen years,","CARD","sixteen small tally marks scratched in a row across a plain white card","a hand-lettered label \"SIXTEEN YEARS.\"","white","flat"),
("Michael Rothschild and Volkmar Schneider at the Berlin Institute of Legal Medicine went back through every death by cold they could find.","CARD","two plain case folders side by side on a bare table, one open, a small hand-drawn city skyline behind them","a small hand-lettered label \"BERLIN\"","white","flat"),
("Sixty nine people.","CARD","sixty nine tiny identical marks arranged in a neat grid filling the middle of a plain white card","a very large hand-lettered number \"69\"","white","flat"),
("A quarter of them had taken their clothes off,","SCENE_N","a coat and a boot lying discarded on snow, drawn in the real world not on a card","no text","frozen_ground","flat"),
("and this has a name, paradoxical undressing.","CARD","a folded pile of clothes drawn on bare ground with nobody near it","a hand-lettered label \"PARADOXICAL UNDRESSING.\"","white","flat"),
("And almost every one of those was found somewhere very strange.","CARD","a plain floor plan of a room drawn from above with three small circles marked in odd corners","no text","white","flat"),
("Under a bed.","SCENE_N","the dark narrow gap under a bed frame seen from floor level, empty, one shoe left just outside it","no text","frozen_ground","flat"),
("Behind a wardrobe.","SCENE_N","the thin dark slot between a wardrobe and a wall, empty, dust and one scrap of cloth on the floor","no text","frozen_ground","flat"),
("Wedged into a shelf.","SCENE_N","a low shelf unit with its contents pushed out and scattered on the floor, the empty space left behind it","no text","frozen_ground","flat"),
("Nobody put them there.","CARD","a plain outline of a hand reaching in, with a red X drawn through it","no text","white","flat"),
("They crawled in.","SCENE_N","two long drag marks in dust on a floor, leading into a dark gap, drawn from above","no text","frozen_ground","flat"),
("The last thing a freezing person does is not lie down and drift off.","SCENE_N","the same smooth snow field with the shallow body-shaped dip, now with a red X drawn over it","no text","frozen_ground","flat"),
("It is to find a den and crawl into it,","SCENE_N","a dark burrow mouth in a bank of frozen earth, tracks leading straight into it","no text","frozen_ground","flat"),
("the way an animal does.","BEAST","a fox drawn in full detail with thick fur and shadow, low to the ground, disappearing into a burrow mouth","no text","frozen_ground","flat"),
("Something very old is still running inside us,","SCENE_A","he lies curled tight on his side on frozen ground, knees drawn up, both hands pulled in against his chest","no text","frozen_ground","asleep"),
("and in the last minutes it takes over.","SCENE_A","the same curled figure seen from further back, very small on a wide field of frost, blue all over","no text","frozen_ground","flat"),

# ═════════════════ CAU HOI LOI — 8 shot ═════════════════
("If a human body is that fragile in the cold,","SCENE_A","he stands upright on open frozen ground with his arms slightly out, whole body drawn in cold blue","no text","frozen_ground","worry"),
("then twenty thousand years ago,","CARD","a single long horizontal line with one bright dot near the left end and nothing after it","a hand-lettered label \"20,000 YEARS AGO\"","white","flat"),
("how did anyone lie outside all night","SCENE_A","he lies flat on his back on bare frozen ground under an open sky, arms at his sides","no text","night_open","worry"),
("and still get up in the morning?","SCENE_A","the same man sitting up on the same ground, pale dawn light behind him","no text","dawn","tired"),
("Not on one unlucky night.","CARD","one small square drawn alone on a white card","no text","white","flat"),
("Every night, for months, for hundreds of generations.","CARD","the same small square repeated into a huge grid that runs off all four edges of the frame","a hand-lettered label \"EVERY NIGHT\"","white","flat"),
("So let us go back to","SCENE_N","the low winter sun back on the horizon again, sky orange to blue, the frame slightly wider than before","no text","night_open","flat"),
("that night and walk through it from the start.","SCENE_A","he crouches beside the small fire again, one side orange one side blue, hands out toward the flame","no text","fire_side","calm"),

# ═════════════════ LUA LA CAU TRA LOI AI CUNG NGHI — 6 shot ═════════════════
("The answer everyone reaches for is fire.","SCENE_N","a small fire burning alone on bare ground, its orange glow reaching only a short way out before the dark takes over","no text","fire_side","flat"),
("Fire solves part of it,","SCENE_N","the same fire with a thin ring of warm orange ground drawn around it, and cold blue ground beyond the ring","no text","fire_side","flat"),
("and we will get there,","SCENE_A","he sits with his back to us facing the fire, orange rim light along one side of his body","no text","fire_side","calm"),
("including the part where it fails.","SCENE_N","the same fire drawn much lower, mostly dark red coals, the orange ring around it shrunk to almost nothing","no text","ember","flat"),
("But the thing that kills you first","SCENE_A","he stands still and looks down at the ground under his own feet","no text","frozen_ground","worry"),
("that night is not even in the air.","CARD","a plain drawing of empty air with a few motion lines, and a red X through it","no text","white","flat"),

# ═════════════════ MAT DAT RUT NHIET — 12 shot · CO CHE tren than nguoi ═════════════════
("It is directly under your back.","SCENE_A","he lies on his back on frozen ground seen from the side, the ground under him drawn hard and blue-white","no text","frozen_ground","worry"),
("Lie down on frozen ground","SCENE_A","the same figure lying flat, with short blue arrows drawn leaving his back and going down into the earth","no text","frozen_ground","tired"),
("and it pulls heat out of you far faster than cold air does.","SCENE_A","the same figure, the blue arrows into the ground now thick and many, while only a few thin ones rise into the air","no text","frozen_ground","tired"),
("Air barely touches you.","SCENE_A","the same figure with only two faint thin arrows drifting up off his chest into the open air","no text","frozen_ground","flat"),
("The ground holds your whole back,","SCENE_A","seen from directly above, the whole length of his back pressed flat against the ground, contact edge drawn hard","no text","frozen_ground","flat"),
("and it never warms up.","SCENE_N","a bare patch of frozen ground alone in the frame, frost still on it, no glow anywhere","no text","frozen_ground","flat"),
("Nobody lies flat on that","SCENE_A","the figure lying flat on bare frozen ground with a red X drawn across the whole image","no text","frozen_ground","flat"),
("and gets up in the morning.","SCENE_N","the same bare frozen patch at dawn, empty, one body-shaped mark of melted frost left on it","no text","dawn","flat"),
("So nobody did.","SCENE_A","he stands holding a thick armful of dry grass, about to put it down on the ground","no text","frozen_ground","calm"),
("There was always something in between, every night,","SCENE_A","he lies on a thick mat of grass, with a clear drawn gap between his body and the hard ground below","no text","frozen_ground","calm"),
("replaced when it rotted or got wet.","SCENE_A","he pulls a dark soggy handful of old grass out from under the mat and drops it aside","no text","frozen_ground","flat"),
("Grass, leaves, hide, whatever was there.","CARD","three items laid out in a row and drawn separately: a bundle of dry grass, a heap of leaves, a folded hide","small hand-lettered labels \"GRASS\" \"LEAVES\" \"HIDE\"","white","flat"),

# ═════════════════ KHONG KHI TRONG CO — 8 shot ═════════════════
("The thing doing the work in","SCENE_N","a close cross-section of a mat of grass stems, cut open so the spaces between the stems are visible","no text","white","flat"),
("that pile of grass is not the grass.","CARD","the same cross-section with the stems themselves shaded grey and a red X over them","no text","white","flat"),
("It is the air trapped between the stems,","CARD","the same cross-section again, this time the gaps between stems filled with small pale blue pockets","a small hand-lettered label \"AIR\"","white","flat"),
("which makes heat much slower to travel down into the ground.","CARD","the same cross-section with one slow arrow struggling down through the pockets, drawn thin and broken","no text","white","flat"),
("Tonight there is a whole layer under your back doing exactly that,","SCENE_A","he presses a hand down into the thick grass mat and it gives under his weight","no text","frozen_ground","calm"),
("and you call it a mattress.","OBJ","the same mattress whole again, drawn simply, sitting alone on a plain floor","a hand-lettered label \"A MATTRESS.\"","white","flat"),
("It was never about softness.","OBJ","a hand pressing down into a soft mattress surface, with a red X beside it","no text","white","flat"),
("It is about keeping the ground from reaching you.","OBJ","the same mattress in cross-section with cold blue arrows coming up from below and stopping at the layer","no text","white","flat"),
# ═════════════ OHALO II — 25 shot · THE ban do + mat cat, xen CANH khai quat ═════════════════
("But that is reasoning.","CARD","a thin dotted outline of a grass mat drawn on a plain card, unfinished, one corner fading out","no text","white","flat"),
("Has anyone ever dug one of these up?","SCENE_N","a hand-drawn trowel stuck upright in dry cracked earth, alone in the frame","no text","dig","flat"),
("Yes, and the clearest one surfaced because of a drought.","SCENE_N","a wide cracked lake bed under a hard pale sky, the water line far away at the back","no text","dig","flat"),
("Through the eighties the Sea of Galilee kept dropping,","CARD","a simple side-view of a lake basin with four water lines drawn one below the other, each lower than the last","no text","white","flat"),
("from drought and from pumping,","CARD","the same basin with a small sun above one side and a thin pipe drawing water out the other","no text","white","flat"),
("until the water sat more than six hundred feet below sea level","CARD","the same basin with a long vertical measuring line from a sea-level mark down to the water","a hand-lettered label \"600 FEET DOWN\"","white","flat"),
("and the old lake bed came up into the air.","SCENE_N","the cracked bed now fully exposed and dry, sunlight raking across it, the lake pushed back to the horizon","no text","dig","flat"),
("In 1989,","CARD","a long horizontal line with one bright dot near the right end","a very large hand-lettered number \"1989\"","white","flat"),
("on that freshly exposed mud,","SCENE_N","close on wet grey mud with the first dark shapes just beginning to show through it","no text","dig","flat"),
("something appeared that had been underwater for twenty three thousand years.","CARD","the same long line, now with a second dot at the far left end and a huge gap drawn between the two","a hand-lettered label \"23,000 YEARS\"","white","flat"),
("A camp, six huts,","SCENE_N","a plan view of six oval hut outlines arranged loosely together on flat ground","no text","dig","flat"),
("and it was given the name Ohalo Two.","CARD","a hand-drawn map of the eastern Mediterranean with one red pin pressed into the Sea of Galilee","a hand-lettered label \"OHALO II\"","white","flat"),
("Dani Nadel and his team","GROUP","two people kneeling in a shallow square pit, working with hand tools, seen from above","no text","dig","curious"),
("from the University of Haifa had about two years to dig","CARD","two small suns drawn side by side above a shallow pit, and a wave line creeping in from the right edge","a small hand-lettered label \"TWO YEARS\"","white","flat"),
("before the water came back.","SCENE_N","the same pit with a thin sheet of water already spreading across one corner of it","no text","dig","worry"),
("Waterlogged mud is one of the very few places soft things survive,","CARD","a cross-section of wet dark mud with a thin pale layer preserved inside it, everything above it dry and crumbled","no text","white","flat"),
("and the floor of one hut still had its bedding lying on it.","SCENE_N","the floor of a hut cleared of soil, a pale patch of flattened plant material lying across the middle of it","no text","dig","flat"),
("Not a dark stain in the soil.","CARD","a vague dark smudge on a plain card with a red X drawn through it","no text","white","flat"),
("Not the shadow of something that used to be there.","CARD","a faint hollow outline on a plain card with a red X drawn through it","no text","white","flat"),
("Actual grass.","SCENE_N","very close on real grass stems, drawn in full detail, individual blades pressed flat and clearly visible","no text","dig","flat"),
("Bundles of marsh grass, partly charred,","SCENE_N","a bundle of grass stems where one end is blackened and burnt and the rest is pale","no text","dig","flat"),
("pressed flat under a thin layer of clay.","CARD","a cross-section showing a thin clay sheet lying directly on top of a flattened grass layer","small hand-lettered labels \"CLAY\" and \"GRASS\"","white","flat"),
("And they were not lying at random.","CARD","a scattered pile of grass drawn loosely, with a red X through it","no text","white","flat"),
("Nadel recorded that they were laid out in a repeated pattern, on the floor,","CARD","a plan view of a hut floor with grass bundles drawn in a clear repeating arrangement","no text","white","flat"),
("around a hearth in the middle.","CARD","the same plan view with a small dark fire circle drawn at the centre and the bundles ringed around it","no text","white","flat"),

# ═════════════════ TACH BANG CHUNG / SUY LUAN — 8 shot ═════════════════
("Then the water came back and covered it again.","SCENE_N","the same hut floor with water sheeting over it, the pale bedding patch dimming under the surface","no text","dig","flat"),
("What the ground will say is that they had bedding,","CARD","the plan view of bedding and hearth again, drawn solid and confident, with a tick mark beside it","no text","white","flat"),
("and that they arranged it around a fire.","CARD","the same plan view with the ring arrangement traced by a firm hand-drawn circle","no text","white","flat"),
("That the bedding was there to stop the ground","SCENE_A","he lies on a grass mat with cold blue arrows rising from the earth and stopping at the layer","no text","frozen_ground","calm"),
("from pulling heat out of them,","SCENE_A","the same figure, the blue arrows now clearly blocked, none of them reaching his back","no text","frozen_ground","calm"),
("the ground does not say.","CARD","the same arrow drawing, now sketched in faint dotted lines instead of solid ones","no text","white","flat"),
("That part is still ours,","CARD","two hands setting two separate pieces of card next to each other on a table","a hand-lettered label \"OURS\"","white","flat"),
("laid alongside what we know about how heat moves through contact.","CARD","one warm shape touching one cold shape, arrows crossing where they meet","small hand-lettered labels \"WARM\" and \"COLD\"","white","flat"),

# ═════════════════ LUA KHONG SUOI AM DEM — 20 shot · dai cam RONG NHAT o day ═════════════════
("Now the fire,","SCENE_N","a fire burning strongly on bare ground, its orange glow thrown wide across the frame","no text","fire_side","flat"),
("and this is the part it took me longest to accept.","SCENE_A","he sits close to the fire with his chin down, one whole side of him orange, thinking","no text","fire_side","curious"),
("Everyone assumes the fire is there to make the night warmer.","GROUP","four figures sitting evenly spaced around a fire, all of them drawn evenly warm orange all over","no text","fire_ring","calm"),
("It cannot do that.","GROUP","the same four figures, now correctly drawn with only the fire-facing half of each body orange and the rest blue","no text","fire_ring","flat"),
("Fire does heat the air around it,","SCENE_N","a fire with a soft warm halo drawn in the air immediately above the flame","no text","fire_side","flat"),
("that air just goes straight up and leaves,","SCENE_N","the same halo drawn stretching up and thinning out into the dark sky above","no text","fire_side","flat"),
("and out in the open the wind takes the rest.","SCENE_N","the warm halo bent hard sideways and torn apart by drawn wind lines crossing the frame","no text","fire_side","flat"),
("A heater warms a whole room,","OBJ","a plain room drawn in cross-section, evenly filled with warm colour from floor to ceiling, one small heater on the wall","no text","white","flat"),
("and then you forget it exists.","OBJ","the same room drawn again with the heater faded almost to nothing on the wall","no text","white","flat"),
("Sit in front of a fire","SCENE_A","he sits facing a fire, seen from the side, the split down his body sharp and obvious","no text","fire_side","flat"),
("and your face burns while your back stays cold.","SCENE_A","close on him from the side, face and chest bright orange, shoulders and back deep blue","no text","fire_side","worry"),
("What reaches your face is radiation,","SCENE_N","straight orange rays drawn from the flame to a facing surface, arriving in straight lines","no text","fire_side","flat"),
("travelling straight from the flame to your skin,","SCENE_A","the same straight rays landing on the side of his face and stopping there","no text","fire_side","flat"),
("with no air carrying it.","CARD","the same straight rays with the air between them left completely blank and untouched","no text","white","flat"),
("So it only reaches the side","SCENE_A","seen from above, only the fire-facing arc of his body is orange, the rest of the outline blue","no text","fire_ring","flat"),
("that is turned toward it.","SCENE_A","the same figure turned slightly, the orange arc turning with him to stay facing the flame","no text","fire_ring","flat"),
("It cannot hold a room warm.","OBJ","the plain room in cross-section again, this time cold blue throughout, with one small fire in the middle","no text","white","flat"),
("It cannot hold the ground warm.","SCENE_N","bare ground beside a burning fire, the frost on it drawn still intact right up to the fire's edge","no text","fire_side","flat"),
("What it can keep warm is one strip of skin.","SCENE_A","close on his side, one narrow vertical band of skin lit warm orange, everything around it blue","no text","fire_side","flat"),
("And this is where one strip of skin turns out to matter more than any of it.","SCENE_A","the same narrow orange band alone in the frame, the rest of the image dark","no text","fire_side","flat"),

# ═════════════════ BASEL — 22 shot · KHOA HOC = VAT, nhung GIU hai nhiet do mau ═════════════════
("What predicts whether you fall asleep fast","OBJ","a plain bed drawn alone in the dark, one side of the covers faintly warm, the other faintly cold","no text","lab_cold","flat"),
("or lie there for hours is whether your body can get heat out.","OBJ","the same bed with small warm arrows leaving the covers and rising into the dark air above","no text","lab_cold","flat"),
("Not lying still.","SCENE_A","he lies dead still on the grass mat with his eyes wide open, a small red X beside him","no text","fire_side","tired"),
("Not being tired enough.","SCENE_A","close on his face, eyes heavy and half closing but still awake, a small red X beside him","no text","fire_side","tired"),
("Getting rid of heat, through the skin, actively.","CARD","a simple skin surface in cross-section with warm arrows passing out through it","a small hand-lettered label \"THROUGH THE SKIN\"","white","flat"),
("In 2000,","CARD","a long horizontal line with a single bright dot at the far right end","a very large hand-lettered number \"2000\"","white","flat"),
("Kurt Kräuchi and his colleagues at the Psychiatric University Clinic in Basel wired people up in a sleep lab and asked one question.","OBJ","a plain lab bed with thin sensor wires running from it to a small recording box, everything drawn simply","a small hand-lettered label \"BASEL\"","lab_cold","flat"),
("Of everything you can measure on a person lying in the dark,","OBJ","the same bed in near darkness with four small sensor points glowing faintly on it","no text","lab_cold","flat"),
("what predicts how fast they fall asleep?","CARD","a plain clock face with a question mark drawn where the hands should be","no text","white","flat"),
("They measured all the obvious things.","CARD","three small measuring instruments drawn in a neat row on a plain card","no text","white","flat"),
("Core temperature.","CARD","a thermometer drawn alone, its bulb sitting at the centre of a simple torso outline","a hand-lettered label \"CORE TEMPERATURE\"","white","flat"),
("Melatonin.","CARD","a small vial with a few drops in it, drawn alone","a hand-lettered label \"MELATONIN\"","white","flat"),
("Heart rate.","CARD","a single flat line with three heartbeat spikes in it","a hand-lettered label \"HEART RATE\"","white","flat"),
("None of those won.","CARD","the three previous cards drawn small side by side, a red X struck through all three at once","no text","white","flat"),
("It was the gap between the hands","SCENE_A","he lies on the mat with his hands drawn warm orange and his chest drawn cool blue","no text","fire_side","asleep"),
("and feet and the middle of the body.","OBJ","the same outline with the feet also warm orange, and a measuring line drawn between limb and centre","no text","white","flat"),
("Not the head.","CARD","a plain head outline with a red X beside it","no text","white","flat"),
("The hands.","SCENE_A","both of his hands lying open on the bedding in firelight, drawn large, warm orange","a hand-lettered label \"THE HANDS.\"","fire_side","calm"),
("You fall asleep because your core has already cooled,","SCENE_A","he lies on his side, the centre of his body drawn cooling from orange down to pale blue","no text","fire_side","asleep"),
("and the place that heat leaves from is your hands.","SCENE_A","the same sleeping figure with warm arrows streaming out through both open hands","no text","fire_side","asleep"),
("Stick a foot out from under the covers tonight","OBJ","a plain bed with one bare foot pushed out past the edge of the covers into the cool air","no text","lab_cold","flat"),
("and you are doing that on purpose.","OBJ","the same foot with small warm arrows lifting off it into the dark","no text","lab_cold","flat"),

# ══════════ LANH DONG BAN TAY LAI — 8 shot · CO CHE tren than nguoi co dai ══════════
("Now take that same body outside on a night below freezing.","SCENE_A","he stands out on open frozen ground with his arms at his sides, whole body drawn cold blue","no text","frozen_ground","worry"),
("The cold hits the skin","BODY","close on his bare forearm with fine frost drawn settling on the skin","no text","frozen_ground","shock"),
("and it does the oldest thing it knows how to do.","SCENE_A","the same forearm with the skin surface drawing tight and the colour draining from it","no text","frozen_ground","shock"),
("It clamps down on the blood flow to your hands.","SCENE_A","his open hand curling hard shut, the fingers going pale blue from the tips inward","no text","frozen_ground","scared"),
("Blood is pulled out of the fingers","BODY","close on the shut hand, the fingertips drawn palest and the colour pulling back toward the wrist","no text","frozen_ground","worry"),
("and toes and sent to the middle,","SCENE_A","a full body from the side, hands and feet drawn pale blue while the chest keeps its warm colour","no text","frozen_ground","worry"),
("around the organs that are not allowed to cool.","SCENE_A","the same body with a small steady warm core held at the centre and everything outward drawn cold","no text","frozen_ground","flat"),
("Hold a cold can a little too long","SCENE_A","one hand gripping a cold hard object, the fingers already stiffening and losing colour","no text","frozen_ground","worry"),
# ══════════ LANH DONG BAN TAY — 12 shot · CO CHE tren than nguoi co dai ══════════
("and you have felt the first part of that.","BODY","close on his hand curled tight around a cold object, fingers stiff, knuckles pale blue","no text","frozen_ground","worry"),
("But sleep needs those vessels open.","BODY","close on an open relaxed hand lying palm up, warm orange, fingers loose","no text","fire_side","calm"),
("The cold just closed them.","SCENE_A","the same hand snapping shut into a tight fist, drawn cold blue","no text","frozen_ground","shock"),
("And that is why one warm strip of skin matters so much.","SCENE_A","he lies on his side, one narrow orange band running down the front of his body, hand at the end of it","no text","fire_side","calm"),
("Someone lying with one side toward the fire has exactly one patch of skin kept warm enough","SCENE_A","close on the fire-facing flank, a clearly bounded warm patch, cold blue on either side of it","no text","fire_side","flat"),
("that the vessels there stay open.","SCENE_A","the same warm patch with the hand at its edge slowly uncurling","no text","fire_side","calm"),
("The hands can open.","SCENE_A","the hand fully open now, palm up, warm orange, fingers spread","no text","fire_side","calm"),
("The heat can leave.","SCENE_A","small warm arrows lifting off the open palm into the dark air above","no text","fire_side","calm"),
("And sleep follows.","SCENE_A","his face relaxes and his eyes close, one side of his face orange","no text","fire_side","asleep"),
("That last step is reasoning, not measurement.","CARD","the chain of small drawings from warm skin to open hand to sleep, redrawn in faint dotted lines","no text","white","flat"),
("Nobody has ever put sensors on a person lying beside a campfire.","OBJ","a sensor wire and pad drawn beside a campfire scene, with a red X through the sensor","no text","fire_side","flat"),
("But it is the same skin","BODY","close on his forearm and hand in firelight, skin drawn with fine texture lines","no text","fire_side","flat"),

# ══════════ KHOI VA CAI GIA CUA LUA — 8 shot ══════════
("and the same vessels we are all still carrying.","OBJ","the same forearm and hand drawn alone on a plain card, one side warm one side cool","no text","white","flat"),
("Except the fire gives nothing away for free.","SCENE_N","a fire with thick grey smoke pouring off one side of it, bending low across the ground","no text","fire_side","flat"),
("A fire far enough away to feel pleasant does nothing for your skin,","SCENE_A","he sits well back from the fire, his whole body drawn cold blue, the orange glow stopping short of him","no text","fire_side","tired"),
("and a fire close enough to warm one side of you breathes smoke into your face for as long as it burns.","SCENE_A","he lies close to the flame, one side orange, thick smoke curling directly across his face","no text","fire_side","worry"),
("And you cannot move away from it,","SCENE_A","the same figure with cold blue drawn pressing in hard from the side away from the fire","no text","fire_side","worry"),
("because on your other side is the cold.","SCENE_A","seen from above, a narrow warm band on one side of him and deep blue on the other, no room between","no text","fire_ring","tired"),
("Warm on one side, breathing that, all night.","SCENE_A","close on his face, eyes half shut against the smoke, one cheek orange one cheek blue","no text","fire_side","tired"),
("Nobody paints that, and it happened every night.","SCENE_N","the same smoky fireside scene drawn small and plain, no drama, just repeated","no text","fire_side","flat"),

# ══════════ NGUOI NAM CANH — 12 shot ══════════
("And there was one more heat source in that camp,","SCENE_N","the camp at night from above, the fire glowing, and a second smaller warm shape lying near it","no text","fire_ring","flat"),
("and this one does not burn.","CARD","a flame drawn on a plain card with a red X through it","no text","white","flat"),
("It is the person lying next to you.","GROUP","two figures lying back to back on a grass mat, a warm orange seam running along where they touch","no text","fire_side","asleep"),
("A body gives off heat all night whether it wants to or not,","SCENE_A","a single sleeping figure with faint warm arrows lifting off the whole length of his body","no text","fire_side","asleep"),
("and pressed against another body it is doing exactly what the fire does.","GROUP","the two figures pressed together, the warm seam between them drawn as bright as the firelight","no text","fire_side","asleep"),
("One warm surface, against skin,","GROUP","close on the contact line between two backs, warm orange right at the join","no text","fire_side","asleep"),
("and this one never goes out.","GROUP","the same pair drawn later with the fire behind them almost dark, but the seam between them still warm","no text","ember","asleep"),
("Sleep alone and you get one warm side at best,","SCENE_A","one figure alone on the mat, only the fire-facing side orange, the whole back deep blue","no text","fire_side","tired"),
("and only while the fire holds.","SCENE_A","the same lone figure with the fire behind him drawn low, his orange side already narrowing","no text","ember","worry"),
("Which means the worst place in","GROUP","a plan view of the camp with figures ringed around the fire and one figure set apart at the edge","no text","fire_ring","flat"),
("that camp is not the coldest corner.","CARD","the same plan view with the outer cold edge marked, then crossed out with a red X","no text","white","flat"),
("It is being on your own.","SCENE_A","the lone figure at the edge, drawn small, cold blue on every side of him","no text","frozen_ground","tired"),

# ══════════ SU TU HANG — 17 shot · CON VAT ve CHI TIET (hoc Stickly) ══════════
("And what else is out there in the dark?","SCENE_N","flat blackness with a single pair of eyes catching the firelight at the far edge","no text","night_dark","flat"),
("The cave lion.","BEAST","a cave lion drawn in full detail, thick winter mane, individual fur strokes, heavy shoulders, standing side on in the dark","no text","night_dark","flat"),
("A skeleton of an adult male dug up at Siegsdorf, in Germany,","CARD","a hand-drawn map of central Europe with a single red pin pressed into southern Germany","a hand-lettered label \"SIEGSDORF\"","white","flat"),
("stood about four feet at the shoulder,","CARD","the detailed lion in profile with a vertical measuring line from ground to shoulder","a hand-lettered label \"4 FEET TALL\"","white","flat"),
("with a body close to seven feet long before the tail.","CARD","the same lion with a horizontal measuring line running nose to hip, tail left out","a hand-lettered label \"7 FEET\"","white","flat"),
("Hervé Bocherens and his team read the isotopes in the bones of more than three hundred and seventy meat eaters","CARD","a grid of many small animal bone shapes filling a plain card, a few of them circled","a hand-lettered label \"370 ANIMALS\"","white","flat"),
("and plant eaters across twenty five sites,","CARD","a hand-drawn map of Europe with twenty five small pins scattered across it","a hand-lettered label \"25 SITES\"","white","flat"),
("to rebuild who was eating whom.","CARD","three animals drawn in outline joined by arrows showing which ate which, drawn as a simple chain","no text","white","flat"),
("For cave lions,","BEAST","the detailed lion drawn alone in the centre of a plain card, looking straight ahead","no text","white","flat"),
("the answer was that they did not all eat the same way.","CARD","two identical lion outlines side by side, each with a different food item drawn beneath it","no text","white","flat"),
("Some leaned heavily toward reindeer.","BEAST","a reindeer drawn in full detail with heavy antlers and thick coat, standing in snow","a small hand-lettered label \"REINDEER\"","frozen_ground","flat"),
("Others carried the signature of young cave bears.","BEAST","a cave bear cub drawn in full detail with soft dense fur, small and low to the ground","a small hand-lettered label \"CAVE BEAR CUB\"","frozen_ground","flat"),
("The isotopes do not tell you how it got hold of that bear cub.","CARD","a cave mouth drawn with a large question mark inside it, everything beyond the entrance left blank","no text","white","flat"),
("They only tell you that the cub ended up inside a lion.","CARD","a single bone fragment drawn large and alone, with a thin measuring scale beside it","a hand-lettered label \"ONE CUB\"","white","flat"),
("Nobody knows what hours it hunted.","CARD","a plain clock face with all the hour marks drawn but no hands at all","no text","white","flat"),
("That is not the frightening part.","BEAST","the detailed lion drawn walking away into darkness, only the hind quarters still lit","no text","night_dark","flat"),
("The frightening part is that a sleeping person does not know where it is.","SCENE_A","he lies asleep beside the fire, eyes closed, and the darkness around the whole frame is completely empty","no text","fire_side","asleep"),

# ══════════ LUA LUI — 13 shot · dai cam CO LAI ══════════
("And that camp still has to sleep.","GROUP","the ring of figures lying around the fire, all asleep, the warm zone still wide","no text","fire_ring","asleep"),
("Then comes the stretch where the wood loaded at dusk has mostly burned through.","SCENE_N","the fire lower than before, most of the wood gone to grey ash, a few sticks left standing","no text","ember","flat"),
("The flame drops down to coals.","SCENE_N","no flame left, only a bed of dull red coals, the orange glow now very small","no text","ember","flat"),
("A hide does not switch off halfway through the night.","OBJ","a folded hide drawn alone on a plain card, unchanged and solid","no text","white","flat"),
("A fire does.","SCENE_N","the same coal bed drawn twice side by side, bright on the left and nearly dark on the right","no text","ember","flat"),
("Nobody recorded that night,","CARD","a blank sheet of paper drawn alone, nothing written on it","no text","white","flat"),
("but heat still moves through human skin the same way,","OBJ","a simple skin cross-section with warm arrows crossing it, drawn solid and confident","no text","white","flat"),
("so what follows is a reconstruction.","CARD","the same fireside scene redrawn entirely in thin dotted outline instead of solid lines","no text","white","flat"),
("When the fire finally dies down,","GROUP","the ring of sleepers with the warm orange zone shrunk to a narrow band right at the coals","no text","ember","asleep"),
("the warm side cools within minutes, the vessels close,","SCENE_A","close on a sleeping figure whose orange side is draining to blue, his open hand curling shut","no text","ember","asleep"),
("and the people around it begin waking up shivering before they understand why.","GROUP","the ring of figures with small shake lines coming off their shoulders, eyes opening","no text","ember","shock"),
("One person may notice first.","SCENE_A","one figure at the outer edge of the ring already lying with eyes open, head slightly lifted","no text","ember","curious"),
("They are lying at the outer edge of the warm zone,","GROUP","a plan view of the ring with the warm zone drawn shrinking inward, one figure right on its retreating edge","no text","fire_ring","flat"),

# ══════════ DOLNI VESTONICE — 16 shot · THE mat cat dia tang ══════════
("the part that shrinks first as the flame drops.","GROUP","the same plan view a moment later, the warm circle smaller again, that figure now fully outside it","no text","fire_ring","flat"),
("And there is one place","SCENE_N","a hand-drawn trowel resting on a cleared patch of dark earth","no text","dig","flat"),
("where the ground tells us part of this story.","SCENE_N","a shallow excavation square with dark banded layers visible in its cut wall","no text","dig","flat"),
("In what is now Moravia there is a camp called Dolní Věstonice,","CARD","a hand-drawn map of central Europe with a red pin pressed into Moravia","a hand-lettered label \"DOLNÍ VĚSTONICE\"","white","flat"),
("about twenty six thousand years old,","CARD","a long horizontal line with one dot far to the left and a wide empty span to the right","a very large hand-lettered number \"26,000\"","white","flat"),
("and the houses there have hearths built inside them.","SCENE_N","a cutaway of a low hut with a dark fire circle set into the floor inside it","no text","dig","flat"),
("Those hearths are not one fire.","CARD","a single simple fire circle drawn flat, with a red X through it","no text","white","flat"),
("They are layers.","CARD","a vertical cross-section of ground showing several distinct dark bands stacked one on another","no text","white","flat"),
("Ash on charcoal on burnt bone,","CARD","the same cross-section with each band drawn differently: pale ash, black charcoal, white bone fragments","small hand-lettered labels \"ASH\" \"CHARCOAL\" \"BURNT BONE\"","white","flat"),
("the same spot lit again and again.","SCENE_A","a figure kneeling at the same hearth spot, drawn three times overlapping in the same place","no text","ember","calm"),
("What the ground tells us for certain is only that much,","CARD","the layer stack drawn solid and firm, with a tick mark beside it","no text","white","flat"),
("that the spot was lit a great many times,","SCENE_N","the hearth circle seen from above, the ground around it worn smooth and dark from use","no text","dig","flat"),
("over a great many years.","CARD","the stack with a long vertical time arrow drawn beside it, running from bottom to top","no text","white","flat"),
("It does not tell us","CARD","the same layer stack now drawn in faint dotted outline","no text","white","flat"),
("who lit it, at what hour,","CARD","a plain figure outline and a plain clock face side by side, both left completely blank inside","no text","white","flat"),
("or whether anyone was assigned to tend it.","CARD","a duty roster ruled into empty cells, every cell left blank","a hand-lettered heading \"WHO TENDS IT\"","white","flat"),

# ══════════ AI DAY TIEP LUA + SAMSON — 19 shot ══════════
("The rest is reasoning, and I am saying so plainly.","CARD","two cards laid side by side, one drawn solid and one drawn dotted","no text","white","flat"),
("But a fire does not burn","SCENE_N","a bed of coals drawn very low, almost dark, thin smoke rising","no text","ember","flat"),
("until morning on its own.","SCENE_N","the same coals gone completely grey and cold, dawn light just touching them","no text","dawn","flat"),
("So if it was still going at dawn,","SCENE_N","a small fire still burning as pale dawn light comes across the ground behind it","no text","dawn","flat"),
("then someone got up in the night, in the dark,","SCENE_A","a figure kneeling at the coals in near darkness, placing a stick onto them, lit only from below","no text","ember","tired"),
("in a place that killed people.","SCENE_A","he kneels at the coals seen from far back, very small, open black ground all around him","no text","night_dark","worry"),
("The question is who.","GROUP","a ring of sleeping figures seen from above, each one identical, no way to tell them apart","no text","fire_ring","asleep"),
("Nothing in the ground answers that,","CARD","the layer cross-section again with a large question mark drawn over it","no text","white","flat"),
("but something alive today answers part of it.","OBJ","a small wrist tracker drawn alone on a plain card","no text","white","flat"),
("In 2017,","CARD","a long horizontal line with a bright dot at the far right end","a very large hand-lettered number \"2017\"","white","flat"),
("David Samson and his team tracked thirty three Hadza people in Tanzania over twenty nights.","CARD","thirty three small wrist-tracker symbols arranged in a grid on a plain card","a hand-lettered label \"33 PEOPLE\"","white","flat"),
("Across all twenty nights,","CARD","twenty narrow vertical bars in a row, each one representing one night","no text","white","flat"),
("the total time when everyone wearing a tracker was asleep at once came to eighteen minutes.","CARD","the same twenty bars, with one tiny sliver shaded dark near the middle of the row","a very large hand-lettered label \"18 MINUTES\"","white","flat"),
("Nobody had scheduled that.","CARD","the same blank duty roster with a red X drawn across the whole sheet","a hand-lettered heading \"NO ROTA\"","white","flat"),
("People of different ages simply ran on slightly different body clocks.","CARD","four small clock faces in a row, each set to a slightly different time","no text","white","flat"),
("Those are living people,","OBJ","a plain modern wrist with the tracker on it, drawn alone, no face and no body","no text","white","flat"),
("not people from twenty three thousand years ago.","CARD","the same wrist tracker with a long time arrow pointing away from it into empty space","no text","white","flat"),
("But it shows a group can have someone awake","GROUP","a ring of sleeping figures with exactly one of them drawn with eyes open","no text","fire_ring","asleep"),
("or only lightly asleep almost all night,","GROUP","the same ring, one figure with eyes half open, drawn slightly lighter than the rest","no text","fire_ring","asleep"),

# ══════════ HASKELL + CAI CHAN — 24 shot · KHOA HOC = VAT ══════════
("without anyone handing out shifts.","CARD","the same blank roster drawn faint and pushed to one corner","a hand-lettered label \"NOBODY ASSIGNED\"","white","flat"),
("So whoever got up and fed","SCENE_A","the kneeling figure at the coals again, seen closer, feeding a stick into the glow","no text","ember","calm"),
("that fire was probably not chosen.","CARD","a ring of identical figures with a pointing hand drawn beside them, and a red X through the hand","no text","white","flat"),
("They were just already awake.","SCENE_A","close on one face lying on the ground with eyes already open in the dark","no text","ember","curious"),
("Tonight nobody in your house has to get up.","OBJ","a plain room drawn dark and still, a bed made, nobody in the frame","no text","lab_cold","flat"),
("But cold does not have to reach freezing to wreck a night.","SCENE_A","he lies awake on the mat on a mild night, no frost anywhere, still unable to settle","no text","fire_side","tired"),
("In 1981,","CARD","a long horizontal line with a bright dot near the right end","a very large hand-lettered number \"1981\"","white","flat"),
("a team led by Haskell had six men sleep in nothing but shorts on a nylon mesh frame,","OBJ","a bare nylon mesh bed frame drawn alone, air gaps clearly visible through the mesh","no text","lab_cold","flat"),
("in a room they could set to any temperature.","OBJ","a plain sealed room in cross-section with a single control dial drawn on the outside wall","no text","lab_cold","flat"),
("They tried five temperatures.","CARD","five thermometers drawn in a row, each column at a different height","no text","white","flat"),
("The temperature that disrupted sleep the most was seventy degrees.","CARD","the same five thermometers with the lowest one circled heavily by hand","a very large hand-lettered label \"70°\"","white","flat"),
("Room temperature.","CARD","a plain wall dial drawn alone, the needle sitting at an ordinary comfortable setting","a hand-lettered label \"ROOM TEMPERATURE.\"","white","flat"),
("Roughly what people set a bedroom to","OBJ","the same wall dial drawn on a plain bedroom wall, everything around it ordinary","no text","lab_cold","flat"),
("and then never think about again.","OBJ","the same dial drawn faded almost to nothing on the wall","no text","lab_cold","flat"),
("The difference is not the number seventy.","CARD","the large number drawn again with a red X struck through it","no text","white","flat"),
("The difference is that you are lying under something.","SCENE_A","he lies under a heavy hide pulled up over his shoulder, the hide clearly separate from his body","no text","fire_side","asleep"),
("A blanket does hold heat in, that much is true.","OBJ","a blanket in cross-section with warm colour held underneath it","no text","white","flat"),
("But the part worth noticing is not the heat it keeps.","OBJ","the same cross-section with the held warmth shaded grey and passed over","no text","white","flat"),
("It is where it lets the heat go,","OBJ","the same cross-section with warm arrows moving out from the core and into the skin layer","no text","white","flat"),
("out of your core and into your skin.","SCENE_A","him under the hide, the centre of his body cooling to pale blue while the skin edge warms to orange","no text","fire_side","asleep"),
("It puts a warm surface against you,","BODY","close on the underside of the hide meeting his shoulder, a warm seam right where they touch","no text","fire_side","asleep"),
("the vessels in your skin agree to open,","SCENE_A","an open relaxed hand drawn warm orange, fingers loose, lying on bedding","no text","white","calm"),
("and the core inside you gets to cool.","SCENE_A","the same sleeping figure with the centre of him now fully cooled to pale blue","no text","fire_side","asleep"),
("Warm on the outside so you can cool on the inside.","OBJ","a warm orange ring drawn around a cool blue centre","small hand-lettered labels \"WARM\" and \"COOL\"","white","flat"),

# ══════════ CHAN = LUA GAP LAI + KHUC THANH THAT — 12 shot ══════════
("A blanket is a campfire, folded up.","OBJ","a campfire and a folded blanket drawn side by side, joined by a hand-drawn equals sign","no text","white","flat"),
("Except this one never goes out.","OBJ","the folded blanket drawn alone, warm and unchanged, no flame anywhere","no text","white","flat"),
("And that is all the evidence there is.","CARD","three small cards laid in a row on a plain surface, nothing else around them","no text","white","flat"),
("Nobody recorded that night,","CARD","a blank sheet drawn alone again, still empty","no text","white","flat"),
("and all we have is grass bedding, layers of ash,","CARD","a pressed grass layer and a banded ash stack drawn side by side","no text","white","flat"),
("and living bodies measured in a lab","OBJ","a plain lab bed with sensor wires, drawn small","no text","lab_cold","flat"),
("and in a camp in Tanzania.","CARD","a hand-drawn map of east Africa with a single red pin in it","a hand-lettered label \"TANZANIA\"","white","flat"),
("The most precise number in this whole video comes from just six people.","CARD","six small identical figure outlines standing in a row on a plain card","no text","white","flat"),
("Six.","CARD","the six figures drawn very small in the centre of a large empty card","a very large hand-lettered number \"6\"","white","flat"),
("What the ground tells us is where they lay, not how they slept.","SCENE_A","a bedding patch drawn solid on the ground and a resting figure drawn above it in dotted outline","no text","dig","asleep"),
("But where they lay, it turns out,","GROUP","the sleeping arrangement seen from directly above, bodies and fire and grass all in place","no text","fire_ring","asleep"),
("is most of the story.","GROUP","the same arrangement drawn wider and closer, filling the whole frame","no text","fire_ring","asleep"),

# ══════════ CLIMAX — 14 shot · CANH, va day la khung nguoi xem phai nho ══════════
("Because this is where the familiar picture falls apart.","GROUP","the common image drawn plainly: figures hunched tight in a tense huddle around a fire","no text","fire_ring","scared"),
("Everyone carries the same image of these people,","GROUP","the same hunched huddle drawn again, smaller, like a picture in a frame","no text","fire_ring","scared"),
("huddled around a fire because they were cold.","GROUP","the same huddle with everyone drawn shivering, shake lines on every shoulder","no text","fire_ring","scared"),
("It is the other way around.","CARD","the huddle image drawn on a card and turned upside down","no text","white","flat"),
("They were not huddling around the fire","GROUP","the tense huddle drawn once more with a red X through it","no text","white","flat"),
("so much as lying in the right place.","GROUP","the same people now lying calm and deliberate, evenly placed, each one angled to the fire","no text","fire_ring","calm"),
("One strip of skin toward the fire.","SCENE_A","one sleeper in profile, a clear warm orange band down the fire-facing side of the body","no text","fire_side","asleep"),
("Another person against the back.","GROUP","the same sleeper with a second body pressed to his back, a warm seam where they meet","no text","fire_side","asleep"),
("A layer of grass against the ground.","SCENE_A","the same sleeper from below, a thick grass mat between his back and the frozen earth","no text","fire_side","asleep"),
("The three support one another,","GROUP","the full arrangement in one frame: fire on one side, second body on the other, grass beneath","no text","fire_side","asleep"),
("and taking one away means the other two have to carry more.","GROUP","the same arrangement with the grass mat removed and cold blue flooding up from the ground","no text","frozen_ground","worry"),
("What kept them alive that night was not an object.","CARD","a fire, a hide and a cave drawn in a row, all three struck through with one red X","no text","white","flat"),
("Not the fire, not the hide, not the cave.","CARD","the same three objects drawn faded and pushed to the edges of the card","no text","white","flat"),
("It was the way those three were arranged around the sleeper.","GROUP","the full arrangement drawn from directly above, the three elements ringed around one body","no text","fire_ring","asleep"),

# ══════════ BAN TAY + BINH MINH — 24 shot · dai cam CO LAI CON BAN TAY ══════════
("It is what appears when you set three pieces of evidence side by side,","CARD","three separate cards laid out touching each other, a single shape emerging across all three","no text","white","flat"),
("not something anybody dug up whole.","CARD","an excavation square drawn empty, nothing in it","no text","white","flat"),
("That was not surviving a night.","CARD","a plain figure drawn barely hanging on, with a red X beside it","no text","white","flat"),
("That was running one.","GROUP","the full sleeping arrangement drawn calm and working, seen wide, fire steady","no text","fire_side","asleep"),
("Now back to where we started.","SCENE_A","the sleeper in profile again, exactly as in the opening, one side orange one side blue","no text","fire_side","asleep"),
("The hands.","BODY","very close on one hand lying open on the bedding, warm orange","no text","fire_side","calm"),
("Tonight, when you lie down,","OBJ","a plain bed in a dark room, covers turned back, nobody in frame","no text","lab_cold","flat"),
("the skin of your hands usually warms","SCENE_A","one hand lying open, the skin edge warming to orange from the fingertips inward","no text","fire_side","calm"),
("while the core inside you cools.","SCENE_A","the sleeping figure with the centre cooling to pale blue and both hands warm at the ends","no text","fire_side","asleep"),
("You will not feel it.","CARD","the same body outline drawn very faintly, almost invisible","no text","white","flat"),
("Nobody ever does.","CARD","a row of identical faint body outlines, none of them marked","no text","white","flat"),
("And on the nights it refuses to happen,","OBJ","the hand outline drawn closed and cool, no warm edge at all","no text","white","flat"),
("you lie there exhausted and wide awake, with no idea why.","OBJ","a plain bed in a dark room with the covers rumpled and thrown back, still nobody in frame","no text","lab_cold","flat"),
("The person lying beside that fire twenty three thousand years ago was waiting for the same thing.","SCENE_A","the ancient sleeper in profile, hand open on the bedding, warm band down one side","no text","fire_side","asleep"),
("The difference is that they had to build a world","SCENE_A","he kneels arranging the grass mat and setting stones around the fire before dark","no text","frozen_ground","calm"),
("that would let it happen.","GROUP","the finished arrangement at dusk, everything in place, nobody lying down yet","no text","fire_side","calm"),
("And that world asked for nine separate things, packed into one night.","CARD","nine small hand-drawn symbols in a three by three grid, each with a short label beneath it","a hand-lettered line above them \"NINE SEPARATE THINGS.\" and small labels \"GROUND\" \"HANDS\" \"ONE SIDE\" \"SMOKE\" \"THE OTHER SIDE\" \"ALONE\" \"THE LION\" \"THE FIRE DIES\" \"SOMEONE WAKES\"","white","flat"),
("None of them went away.","GROUP","the full sleeping arrangement again, all nine problems visible in one scene, nothing crossed out","no text","fire_side","asleep"),
("They just got handed out to a wall, a roof, a mattress, a blanket,","OBJ","a wall, a roof, a mattress and a blanket drawn in a row, each with thin lines leading back to the nine symbols","no text","white","flat"),
("and a box on the wall.","OBJ","a small plain box drawn on a wall, a single number on its face","no text","white","flat"),
("Twenty three thousand years,","CARD","a long horizontal line with a dot at each end and a wide span between","a hand-lettered label \"23,000 YEARS\"","white","flat"),
("from a ring of grass around a hearth to a room that handles all nine.","CARD","a ring of grass around a hearth drawn on the left, a plain quiet room drawn on the right, an arrow between","no text","white","flat"),
("It is nearly light.","SCENE_N","the sky above the camp turning from deep blue to pale grey, the coals almost out","no text","dawn","flat"),
("Someone turns over.","SCENE_A","a sleeping figure rolling from one side onto the other, seen from above","no text","dawn","asleep"),

# ══════════ BA SHOT CUOI — dai cam chi con o BAN TAY ══════════
("The cold side goes toward the coals,","SCENE_A","the figure now facing the dying coals, the blue side of his body turned toward the faint warmth","no text","dawn","asleep"),
("the warm side goes into the dark.","SCENE_A","the same figure from the other side, the last warm band turning away into shadow","no text","dawn","asleep"),
("The shivering stops.","BODY","close on his shoulder, the small shake lines fading away to nothing","no text","dawn","asleep"),
("And the hand that had been clenched against the cold slowly opens.","BODY","very close on one hand on the bedding, fingers uncurling, and the only warm orange left in the whole frame is on that hand","no text","dawn","calm"),
]

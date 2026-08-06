# -*- coding: utf-8 -*-
# GEN PROMPTS — Video09 "Why Are Your Teeth Worse Than a Caveman's?" (cụm Cơ thể Đồ Đá)
# 1 dòng narration = 1 shot = 1 ảnh. Nhất quán bằng LẶP CHỮ (STYLE/CONSIST/NEG y nguyên).
# TRẠNG THÁI: ĐỢT 1 (shot 1-36: HOOK + Setup + Ch1). DATA sẽ nối tiếp Ch2->KẾT ở đợt sau.

STYLE = ("Clean flat 2D cartoon explainer with smooth, even, confident medium-bold black "
         "outlines (single clean strokes, not scratchy, not wobbly, not heavy marker), a crisp "
         "minimalist educational look,")

CONSIST = ("The people are clean STICK-FIGURE doodles: a LARGE round white-filled head with a "
           "simple expressive face (two big round white eyes with small black pupils, thin "
           "expressive eyebrows, a tiny mouth, no nose) sitting on a THIN body made of clean black "
           "lines (a single medium-weight line for the torso plus thin noodle arms and legs), with "
           "simple rounded mitten hands and small oval feet, kept identical every time. The modern "
           "man has a BALD round head with NO hair; ONLY the caveman/farmer has hair. The body is "
           "bare line-art with no colour fill; a character only wears a garment if their own "
           "description names it. Any teeth, bacteria, animals and props are simple and cute in flat "
           "SOLID COLOUR, drawn with a little more detail and volume than the plain stick people. "
           "Clean smooth evenly-weighted medium-bold black outlines, flat colours, NO gradient "
           "shading, a clean flat digital-explainer look (not 3D, not glossy).")

NEG = ("Family-friendly, wholesome, cute, gentle, non-violent, no blood, no gore. no gradients, no "
       "textures, no photorealism, no 3D, no glossy render, no sketchy scratchy lines, no extra "
       "limbs or fingers, no watermark, no logo, no frame borders, no collage, no picture-in-"
       "picture, no split-screen panels, 16:9, clean educational YouTube explainer doodle style.")

# ---- Nhân vật (lặp y nguyên) ----
CHAR = {
 'you':   ("the recurring modern guy, the same plain black-outline STICK FIGURE with a plain round "
           "BALD white head and NO hair, a bare thin bold black stick-line body, thin noodle arms "
           "and legs, rounded mitten hands and small oval feet, "),
 'cave':  ("the recurring caveman, the same plain black-outline stickman with a messy scribbly tuft "
           "of short spiky dark doodle hair, wearing a simple ragged brown animal-hide smock as a "
           "flat brown shape over the torso, barefoot with small white oval feet, "),
 'farmer':("the recurring ancient farmer, a plain black-outline stickman with short dark doodle "
           "hair, wearing a simple flat beige tunic shape over the torso, barefoot, "),
 'dent':  ("a dentist stickman with a plain bald white head, wearing a flat pale-blue mask and a "
           "small round head-mirror, "),
 'none':  "",
}

# ---- Nền theo ngữ cảnh (khái niệm=trắng; kể chuyện=cảnh phẳng-màu) ----
SCENE = {
 'wh':    ("Set on a plain solid WHITE background with lots of clean empty space and a soft "
           "light-grey shadow under the subject; a clear concept/diagram look."),
 'mouth': ("Set inside a big friendly cartoon mouth, flat pale-pink gums and a few big flat white "
           "cartoon teeth, clean and simple, lots of space."),
 'sav':   ("Set in a flat Stone Age savanna, flat olive-green and tan ground meeting a flat "
           "pale-blue sky, maybe one simple bush, lots of clean space."),
 'dig':   ("Set on flat tan dirt and soil ground with an archaeological-dig feel, plain and "
           "low-detail, lots of clean space."),
 'farm':  ("Set in a simple early farm field, flat golden wheat and tan soil under a flat pale-blue "
           "sky, low-detail, clean space."),
 'town':  ("Set on a simple 1850s industrial street, flat grey-brown buildings and one smokestack "
           "in the back, muted and low-detail."),
 'cave':  ("Set in a flat dark-brown cave interior, plain, with a small warm orange firelight glow, "
           "lots of clean space."),
 'bath':  ("Set in a simple flat modern bathroom, a pale tiled wall and a mirror, low-detail, clean "
           "space."),
}

# ---- Khung hình (đổi liên tục để đè nhịp đơn điệu) ----
FRAME = {
 'med':  "a medium shot, the subject drawn big and centered with clean breathing space around it.",
 'wide': "a WIDE establishing shot, the subject fairly small inside a large scene.",
 'close':"a tight CLOSE-UP, the expressive face or object filling most of the frame.",
 'high': "a HIGH-ANGLE shot looking DOWN, making the subject look small.",
 'low':  "a LOW-ANGLE shot looking UP, making the subject look powerful.",
}

def textpart(t):
    return ('a small "%s" in bold white ALL-CAPS letters on a little red tag.' % t) if t else "no text or letters."

def build(char, bg, frame, action, text):
    subj = action if char == 'none' else CHAR[char] + action
    return "%s %s. Framing: %s %s %s %s %s" % (STYLE, subj, FRAME[frame], CONSIST, SCENE[bg], textpart(text), NEG)

# DATA: (shotline, char, bg, frame, action, red-text)
DATA = [
 # ---- HOOK (1-14) ----
 ("You brush your teeth twice a day.", 'you','bath','med',"standing at the sink brushing his teeth with a toothbrush, a little white foam, a bored routine expression",""),
 ("You floss. Sometimes. You buy the fancy paste, the one with fluoride and a name you can't pronounce.", 'you','wh','med',"holding up a fancy blue toothpaste tube and a roll of floss with a slightly smug shrug",""),
 ("You see a dentist who scrapes, drills, and tells you to do better.", 'you','wh','med',"lying back nervously in a dentist chair while the dentist leans over him with a small drill","dent"),
 ("And you still get cavities. Crooked teeth. Wisdom teeth that don't even fit in your own head.", 'you','wh','close',"opening his mouth wide to reveal crooked teeth and one dark cavity marked with a small red spot, dismayed face",""),
 ("Now meet a caveman.", 'cave','sav','med',"standing proudly with hands on hips and a friendly confident grin",""),
 ("He never brushed. Never flossed. Never met a dentist, or a mint, or a tube of anything.", 'cave','wh','med',"shrugging cheerfully beside a toothbrush and toothpaste tube that have a big red X drawn over them",""),
 ("He ate with his mouth and cleaned it with nothing.", 'cave','sav','med',"biting happily into a big chunk of meat on a bone, relaxed",""),
 ("And his teeth were straighter than yours. Stronger than yours. And almost never rotted.", 'cave','close',"close",None),  # placeholder-fix below
]

# fix shot 8 (build tuple cleanly)
DATA[7] = ("And his teeth were straighter than yours. Stronger than yours. And almost never rotted.",
           'cave','wh','close',"a huge open proud grin showing a full row of perfect straight white teeth","")

DATA += [
 ("A man who did nothing, beating a man who does everything.", 'none','wh','med',"the caveman on the LEFT grinning with perfect teeth and the modern bald stickman on the RIGHT looking defeated, standing together in one scene, a versus feel",""),
 ("Skulls thousands of years old turn up with a full set of clean, straight teeth. The kind you pay thousands for.", 'none','dig','med',"one ancient human skull lying on the tan dirt with a full set of clean straight white teeth, a tiny price tag hanging off it",""),
 ("So what happened?", 'you','wh','close',"a big confused shrug with palms up and a large question mark floating over his head",""),
 ("Why is the modern mouth, with all its weapons, quietly losing to a Stone Age one?", 'none','wh','med',"on the LEFT a modern mouth surrounded by a toothbrush, floss and toothpaste held like weapons, on the RIGHT a plain simple caveman grin, the modern side clearly losing",""),
 ("Because your teeth were never built for the world you feed them.", 'you','wh','med',"looking down worried at a plate piled with a donut and a soda cup",""),
 ("And the reason they're failing starts the day humans did the smartest, and worst, thing they ever did.", 'farmer','farm','wide',"kneeling to plant the very first seeds into the soil, a small fateful moment, long shadow",""),
 # ---- SETUP (15-24) ----
 ("Here's the first thing to get straight. This is not your fault.", 'you','wh','close',"holding up both hands reassuringly with a calm honest face","NOT YOUR FAULT"),
 ("You didn't get cavities because you're lazy. Your teeth aren't crooked because you skipped a night of flossing.", 'you','wh','med',"looking a little guilty and waving off a roll of floss",""),
 ("Something bigger is going on. A mismatch.", 'none','wh','med',"two puzzle pieces that do NOT fit together, one drawn like an old stone tool and one like a modern donut, a small red gap between them","MISMATCH"),
 ("Your teeth are ancient hardware, tens of thousands of years old, running in a mouth you feed like a modern human.", 'none','wh','med',"a single tooth drawn like an old chipped stone tool with a tiny gear, looking outdated and ancient",""),
 ("And the gap between those two things is where everything goes wrong.", 'none','wh','med',"a timeline arrow running from an ancient tooth to a modern donut with a red crack splitting open in the middle",""),
 ("It's not one cause. It's a stack of them, piled up over time.", 'none','wh','med',"a wobbly leaning stack of labeled blocks piling up, tilting to one side",""),
 ("What actually eats a tooth. What your ancestors ate that saved theirs. The exact moment humans broke their own mouths.", 'none','wh','med',"three simple icons in a row, a small red bacteria blob, a piece of raw meat, and a cracking tooth",""),
 ("And a twist most people never hear. Your jaw is still shrinking, right now, generation by generation.", 'none','wh','med',"a human jaw bone getting visibly smaller across three left-to-right arrows, with a small red shrinking arrow","STILL SHRINKING"),
 ("We saved that one for the end.", 'you','wh','close',"holding one finger up with a knowing look and pointing forward",""),
 ("So start at the beginning. What is actually destroying your teeth?", 'none','wh','med',"one big white tooth in the center with a large question mark and a tiny red crack just starting","?"),
 # ---- Ch1: cái gì ăn mòn răng (25-36) ----
 ("A tooth is one of the hardest things your body makes. Harder than bone.", 'none','wh','med',"one big proud white tooth flexing like a strongman beside a plain bone, a small 'harder' arrow",""),
 ("It's built to last a lifetime, and then some. So what's strong enough to destroy it?", 'none','wh','med',"a strong white tooth holding a tiny shield, a question mark hovering beside it",""),
 ("Not sugar directly. Not acid you drink. Something alive.", 'none','wh','med',"a sugar cube and an acid soda cup each with a red X, and a tiny grinning bacteria blob with a green check",""),
 ("Your mouth is not empty. It's an ecosystem, packed with hundreds of species of bacteria.", 'none','mouth','wide',"the inside of a cartoon mouth teeming with lots of tiny cute colorful bacteria characters crawling over the teeth",""),
 ("Most of them are harmless. Some are even helping you.", 'none','mouth','med',"a few friendly green bacteria blobs with little smiles giving a thumbs up on a clean tooth",""),
 ("But a few of them have one favorite food. Sugar.", 'none','mouth','med',"one nasty red bacteria blob with sharp teeth eyeing a white sugar cube hungrily","SUGAR"),
 ("Every time you eat something sweet or starchy, you're not just feeding yourself. You're feeding them.", 'you','wh','med',"biting a donut while a little speech bubble below shows tiny bacteria cheering",""),
 ("And when those bacteria eat sugar, they do what living things do. They produce waste.", 'none','mouth','med',"the red bacteria blob munching a sugar cube with little waste drips coming off it",""),
 ("Their waste is acid.", 'none','mouth','close',"a single glowing green acid droplet with a menacing little face dripping down toward a tooth","ACID"),
 ("That acid sits on your tooth and slowly dissolves it, molecule by molecule, from the outside in.", 'none','mouth','med',"green acid pooling on a white tooth, the tooth surface visibly pitting and eroding with small red damage",""),
 ("That's a cavity. Not dirt. Not rot from the air. A tiny acid attack, fed by what you eat.", 'none','wh','close',"a big white tooth with a dark cavity hole, a small red arrow pointing to the hole","CAVITY"),
 ("Which means the real question was never how you clean your teeth. It's what you feed the things living on them.", 'you','wh','med',"holding a toothbrush with a red X in one hand and a plate of food with a green check in the other, a realization face",""),
]

DATA += [
 # ---- Ch2: miệng caveman (37-50) ----
 ("So let's go feed a caveman.", 'cave','sav','med',"grinning and rubbing his hands together, hungry and ready, beside a small pile of raw food",""),
 ("For most of human history, we were hunter-gatherers. No farms. No shops. No sugar.", 'cave','sav','wide',"walking across the open savanna with a spear, gathering food, wide empty land with no buildings anywhere",""),
 ("You ate what you could catch, dig up, or pull off a plant.", 'cave','sav','med',"holding up a caught fish in one hand and pulling a root out of the ground with the other",""),
 ("Meat. Fish. Roots. Nuts. Wild greens. Tough, fibrous, gritty food.", 'none','wh','med',"a simple row of icons, a chunk of meat, a fish, a root, a handful of nuts and some green leaves",""),
 ("Food you had to rip and grind for a long time before you could swallow it.", 'cave','sav','close',"chewing hard on a tough strip of meat, jaw working, cheeks straining with effort",""),
 ("And almost none of it was the soft, sweet, sticky sugar those bacteria crave.", 'none','wh','med',"a sugar cube and a sticky candy with a big red X drawn over them","NO SUGAR"),
 ("So the acid attack barely happened. The bacteria that rot teeth had almost nothing to eat.", 'none','mouth','med',"a sad hungry red bacteria blob sitting on a clean tooth beside an empty food bowl",""),
 ("This isn't a guess. We have their skulls.", 'none','dig','med',"an ancient human skull resting on tan dirt with a small magnifying glass hovering over its teeth",""),
 ("Dig up a hunter-gatherer from twenty thousand years ago, and you often find a full set of teeth.", 'none','dig','med',"a skull half-uncovered in the dirt showing a full complete set of clean white teeth",""),
 ("Worn down from all that hard chewing, yes. But clean. Strong. And cavity-free.", 'none','wh','close',"a close-up of one ancient tooth, slightly flattened from wear but clean and solid, a small green check",""),
 ("Some skulls go a whole lifetime without a single hole.", 'none','dig','med',"a skull with a perfect cavity-free grin and a small green check mark beside it",""),
 ("A mouth that never saw a toothbrush, outperforming yours, which owns three.", 'none','wh','med',"on the LEFT an ancient skull with a green check, on the RIGHT a modern bald stickman holding three toothbrushes looking confused",""),
 ("Now, it wasn't always perfect. A few groups who leaned hard on starchy wild foods, like acorns, did get some decay.", 'none','wh','med',"a small pile of acorns beside one tooth with a tiny brown decay spot and a small caution mark",""),
 ("But as a rule, for tens of thousands of years, human teeth were fine. Then we changed everything.", 'none','wh','med',"a long calm timeline of healthy white teeth ending at a red dot marked change",""),
 # ---- Ch3: nong nghiep (51-63) ----
 ("About twelve thousand years ago, humans did something that changed the species forever.", 'farmer','farm','wide',"standing at the edge of a freshly planted field, a big turning-point moment, long shadow",""),
 ("We started to farm.", 'farmer','farm','med',"planting seeds into a row of soil with a simple digging stick",""),
 ("Instead of chasing food, we grew it. Wheat. Barley. Rice. Corn.", 'none','farm','med',"four simple stalks in a row, wheat, barley, rice and corn, growing from the soil",""),
 ("In a lot of ways, it was the smartest thing we ever did. It built villages, cities, everything you know.", 'none','wh','med',"a little cluster of simple houses and a rising city skyline growing up out of a single stalk of wheat",""),
 ("It was also a disaster for your mouth.", 'you','wh','close',"wincing and clutching his cheek in sudden tooth pain",""),
 ("Because those crops had one thing in common. They were packed with starch.", 'none','wh','med',"a grain sack cut open to show tiny starch molecules packed densely inside","STARCH"),
 ("And starch, once it hits your saliva, starts breaking down into sugar.", 'none','mouth','med',"a piece of bread on the tongue turning into little white sugar cubes with a small arrow",""),
 ("For the first time, those acid-making bacteria had a steady, endless buffet.", 'none','mouth','med',"the red bacteria blob at a long buffet table piled high with sugar cubes, delighted",""),
 ("And they multiplied.", 'none','mouth','med',"one red bacteria blob becoming a whole crowd of them multiplying across a tooth",""),
 ("Dig up human skulls from right after farming begins, and you see it appear. Cavities.", 'none','dig','med',"a post-farming skull in the dirt now with visible dark cavity holes in its teeth, small red marks",""),
 ("The same species, the same teeth, suddenly starting to rot.", 'none','wh','med',"two identical teeth side by side, one clean with a green check and one rotting with a red mark",""),
 ("The switch from hunting to farming is written, plain as day, in the holes in our ancestors' teeth.", 'none','wh','med',"an open timeline showing a clean hunter tooth then a farmer tooth full of dark holes",""),
 ("We traded a hard, varied diet for a soft, starchy one. And our mouths paid the bill.", 'none','wh','med',"a balance scale, tough raw food rising on one side and soft bread sinking on the other, a small receipt",""),
 # ---- Ch4: duong cong nghiep (64-76) ----
 ("But farming was only the first hit. The knockout came much later.", 'none','wh','med',"a small boxing glove in front and a much bigger boxing glove looming behind it",""),
 ("Fast forward to around the year eighteen fifty. The Industrial Revolution.", 'none','town','wide',"a simple 1850s industrial street with a smokestack puffing, a calendar page in the corner","1850"),
 ("For the first time in history, sugar became cheap. And processed flour became everywhere.", 'none','town','med',"stacks of cheap white sugar sacks and flour bags piled high with tiny price tags",""),
 ("Suddenly the average person wasn't just eating starch. They were eating pure, refined sugar, every single day.", 'you','town','med',"happily eating a heaping spoonful of pure white sugar straight from a bowl",""),
 ("In tea. In bread. In sweets. In things that had never been sweet before.", 'none','wh','med',"a teacup, a slice of bread and a candy in a row, each with a little sugar cube on top",""),
 ("To the bacteria in your mouth, this was paradise.", 'none','mouth','med',"red bacteria blobs lounging happily on a little beach of sugar, tiny sunglasses on, a paradise vibe",""),
 ("The whole ecosystem tipped. The acid-makers took over, and they never gave the mouth back.", 'none','mouth','med',"the red bad bacteria crowding out the few green good ones and planting a tiny flag on a tooth",""),
 ("Study ancient plaque across time, and there's a clear line. Around the Industrial Revolution, the rot-causing bacteria go from a minority to the rulers of your mouth.", 'none','wh','med',"a simple line graph of red bacteria spiking sharply up at a point marked Industrial Revolution",""),
 ("That's the mouth you inherited. Not the caveman's balanced one. The industrial one, flooded with sugar and run by the wrong bacteria.", 'none','mouth','wide',"a mouth flooded with sugar and red bacteria in charge, a tiny crown on the biggest red blob",""),
 ("So you brush. You floss. You fight a holding action, twice a day, against an ecosystem built to lose.", 'you','bath','med',"brushing hard and determined with a sweat drop, tiny red bacteria pushing back against the brush",""),
 ("And you still lose ground, slowly, filling by filling.", 'you','wh','med',"looking tired while holding up a tooth x-ray marked with several silver fillings",""),
 ("Your ancestors didn't win this fight because they were cleaner than you.", 'cave','sav','med',"the caveman shrugging with empty open palms, holding no toothbrush at all",""),
 ("They won it because they never started it.", 'cave','sav','close',"the caveman with a calm satisfied grin showing perfect teeth, never had to fight",""),
 # ---- Ch5: ham co lai (77-90) ----
 ("But cavities are only half the story. Look in the mirror at the other half.", 'you','bath','med',"leaning toward the bathroom mirror and pulling his lip to inspect his teeth",""),
 ("Your teeth are probably a little crooked. Crowded. Maybe you wore braces to force them straight.", 'you','wh','close',"an open mouth showing crooked crowded teeth, some fitted with tiny braces brackets",""),
 ("And somewhere in the back, you've got wisdom teeth that either hurt, got pulled, or never had room to come in.", 'none','wh','med',"a jaw diagram with a wisdom tooth at the very back glowing red, squeezed with no room",""),
 ("Here's the strange part. Your ancestors almost never had this problem.", 'cave','sav','close',"the caveman flashing a perfectly straight complete grin, totally relaxed",""),
 ("Their teeth came in straight. All of them. Wisdom teeth included, sitting in a neat, complete row.", 'none','wh','med',"an ancient jaw diagram with a full neat row of straight teeth all fitting, a small green check",""),
 ("So why does modern humanity need braces and oral surgery just to fit its own teeth in its own mouth?", 'you','wh','med',"a modern guy with braces and a surgical mask nearby, a confused shrug and a big question mark",""),
 ("Because your jaw is smaller than it was built to be.", 'none','wh','med',"two jaw outlines overlaid, a big ancient one and a smaller modern one inside it, a red gap",""),
 ("A jaw isn't a fixed size. It grows based on how hard you use it as a child.", 'none','wh','med',"a small child's jaw with an arrow showing it can grow bigger or smaller depending on use",""),
 ("Chew tough, raw, fibrous food for years, and the jaw grows big and strong, with room for every tooth.", 'cave','sav','med',"as a child chewing tough raw fibrous food hard, a big strong jaw developing with room for every tooth, a green check",""),
 ("Chew soft, cooked, processed modern food, and the jaw grows up underdeveloped. Too small.", 'you','wh','med',"as a child eating soft mushy modern food, a small underdeveloped jaw, a red shrink arrow",""),
 ("So you end up with a full ancient set of teeth, crammed into a shrunken modern jaw.", 'none','wh','med',"a full set of big teeth crammed and overlapping inside a too-small jaw outline, red pressure marks",""),
 ("They twist. They overlap. And the last ones in, the wisdom teeth, find the door already closed.", 'none','wh','med',"wisdom teeth at the back pushing against a literal closed door in the jaw, stuck outside",""),
 ("Your crooked smile isn't bad luck. It's a jaw that never got the workout it evolved to need.", 'you','wh','close',"a slightly crooked smile with a tiny dumbbell nearby, a jaw that missed its workout",""),
 ("Which raises a darker question we'll come back to. If soft food is still shrinking us, where does it end?", 'none','wh','med',"a jaw shrinking smaller and smaller down a row of arrows, fading into a question mark","?"),
 # ---- Ch6: nha khoa co dai (91-102) ----
 ("Now, none of this means the ancient world was painless.", 'cave','cave','close',"a caveman wincing and holding his jaw in pain",""),
 ("Teeth still cracked. They wore down to the nerve. Abscesses happened, and an abscess could kill you.", 'none','wh','med',"a cracked tooth with a red throbbing spot at the root and a small warning skull",""),
 ("And here's the part that stops you cold. They tried to fix them.", 'cave','cave','med',"a caveman holding up a tiny sharp stone tool with a determined look, about to work on a tooth",""),
 ("In a cave in Italy, researchers found a tooth from about fourteen thousand years ago, with a cavity that had been scraped clean with a tiny sharp stone.", 'none','cave','med',"a tooth resting on a stone while a tiny sharp flint carefully scrapes out a cavity","14,000 YRS"),
 ("That's dentistry, older than farming.", 'none','wh','med',"a timeline with a tiny stone-tool dentistry icon placed BEFORE the farming icon, a small arrow",""),
 ("In what's now Pakistan, they found teeth from around nine thousand years ago with neat, round holes, drilled with a tiny bow drill.", 'none','cave','med',"a small ancient bow drill spinning a neat round hole into a tooth",""),
 ("Someone sat another person down, and drilled into a living tooth. With a stone. On someone who was wide awake.", 'cave','cave','med',"one caveman drilling into another caveman's tooth with a bow drill, the patient wide awake with huge nervous eyes",""),
 ("Somewhere else, a broken tooth was patched with a filling made of beeswax.", 'none','wh','close',"a cracked tooth being patched with a blob of golden-yellow beeswax","BEESWAX"),
 ("Sit with that. Before writing, before the wheel, humans were performing dentistry.", 'none','wh','med',"a stone-tool dentistry icon sitting first on a timeline, before a scroll and a wheel",""),
 ("They didn't understand bacteria. They had nothing to numb the pain. Just a problem, and the stubborn human refusal to live with it.", 'cave','cave','close',"a caveman gritting through the pain with a fierce determined face and one clenched fist",""),
 ("So they weren't living in some cavity-free paradise by luck. Their diet did most of the work.", 'none','wh','med',"a plate of tough raw food doing most of the heavy lifting on a scale, a clean caveman tooth",""),
 ("But when their teeth did fail, they fought back with stone tools and beeswax. Which is either horrifying or heroic, depending on your dentist.", 'none','wh','med',"a tiny stone drill and a blob of beeswax crossed like heroic tools, one half scared face and one half proud face",""),
 # ---- Ch7: ban chai chi chua ngon (103-113) ----
 ("So where does that leave you and your toothbrush?", 'you','bath','med',"standing holding a toothbrush and looking at it uncertainly, a question mark over his head",""),
 ("Brushing helps. It really does. It scrapes off the bacteria and buys you time.", 'you','bath','med',"brushing and scraping little red bacteria off a tooth, a small green check and a clock icon",""),
 ("But understand what you're actually doing. You're managing a problem, not fixing its cause.", 'none','wh','med',"a leaking pipe with a stickman mopping the floor instead of fixing the leak, a manage-versus-fix idea",""),
 ("The cause is on your plate, three times a day.", 'you','wh','med',"pointing down at a plate of sugary food, a small clock showing three meal times",""),
 ("You could brush perfectly and still lose, if you feed those bacteria enough sugar between brushings.", 'you','wh','med',"brushing perfectly but sneaking sugar cubes on the side, red bacteria still winning, a frown",""),
 ("And you could brush badly and be mostly fine, if you ate like your ancestors did.", 'cave','sav','med',"the caveman with a messy never-brushed grin but healthy teeth, eating tough food, a green check",""),
 ("That's the uncomfortable truth the toothpaste ads leave out.", 'none','wh','med',"a shiny toothpaste ad poster with a small hidden asterisk and the fine print peeled back",""),
 ("Your teeth aren't rotting because you're not scrubbing hard enough.", 'you','bath','close',"scrubbing furiously with a toothbrush and sweating, but it misses the point, a red X",""),
 ("They're rotting because you're feeding an ancient mouth a diet it has no defense against.", 'none','mouth','med',"an ancient mouth holding a shield being overwhelmed by a flood of sugar and red bacteria, the shield cracking",""),
 ("The toothbrush is you, standing at the door with a mop, while the flood keeps coming from the kitchen.", 'you','wh','wide',"standing at a doorway with a mop holding back a flood of sugar pouring in from a kitchen behind",""),
 ("It's not a character flaw. It's a mismatch, and you were born into the losing side of it.", 'none','wh','med',"the mismatch puzzle pieces again, an ancient tooth piece and a modern donut piece not fitting, a red losing-side arrow","MISMATCH"),
 # ---- Ch8: cu lat, ham VAN dang co (114-126) ----
 ("But the mismatch isn't finished with you yet.", 'you','wh','close',"a worried glance over the shoulder, sensing something still coming",""),
 ("Remember that shrinking jaw? Here's the part I saved for the end.", 'none','wh','med',"a shrinking jaw icon reappearing with a small saved-for-the-end star bookmark","THE TWIST"),
 ("It's still happening. Right now. To you, and to everyone younger than you.", 'none','wh','med',"a row of jaws from older to younger, each slightly smaller, a red now arrow",""),
 ("Our food keeps getting softer. More processed. Easier to chew.", 'none','wh','med',"a row of foods getting softer left to right, from raw meat to baby-soft processed mush",""),
 ("And with every generation that grows up barely having to chew, the jaw gets a little smaller. A little more crowded.", 'none','wh','med',"three child jaws across generations, each smaller and more crowded with overlapping teeth",""),
 ("Wisdom teeth used to fit. Now, for millions of people, they simply don't, and have to be cut out.", 'none','wh','med',"a wisdom tooth being removed with tiny pliers, a red no-room mark beside it",""),
 ("A body part that worked fine for millions of years is becoming, in real time, a defect.", 'none','wh','med',"a wisdom tooth stamped from a green check over to a red DEFECT stamp","DEFECT"),
 ("Some researchers think we're watching a slow deformation of the human face, driven not by genes, but by diet.", 'none','wh','med',"a human face profile slowly changing shape across arrows, driven by a small fork-and-knife icon, a crossed-out DNA strand",""),
 ("Your children's mouths may be more crowded than yours. Their children's, more crowded still.", 'none','wh','med',"two smaller and smaller child mouths in a row, each more crowded, fading forward",""),
 ("This is evolution's cruel joke. Not a slow improvement over millions of years.", 'none','wh','med',"an evolution ladder icon flipped upside down, a small ironic laughing mask beside it",""),
 ("A fast breakdown, over a few hundred, caused entirely by the world we built.", 'none','wh','med',"a steep downhill red arrow over a very short timeline, a tiny modern city at the top",""),
 ("The caveman with the perfect smile isn't behind us on some ladder.", 'cave','sav','med',"the caveman standing tall with a perfect confident smile, not below on any ladder",""),
 ("In the one thing we're talking about, his mouth simply worked better than yours ever will.", 'none','wh','med',"the caveman's clean grin with a green check beside the modern crooked grin with a red mark",""),
 # ---- KET (127-140) ----
 ("So. Why are your teeth worse than a caveman's?", 'none','wh','med',"the caveman grin and the modern crooked grin side by side with a big central question mark","?"),
 ("Not because you're careless. Not because he was cleaner.", 'none','wh','med',"a toothbrush and a bar of soap both crossed out with red X marks",""),
 ("Because his mouth got the diet it was designed for, and yours never has.", 'none','wh','med',"a caveman tooth matched perfectly to tough raw food with a green check, a modern tooth mismatched to a donut with a red X",""),
 ("He ate hard, wild, unsweetened food, and his teeth grew straight and stayed whole.", 'cave','sav','med',"the caveman biting into tough wild food, a straight whole healthy grin, a green check",""),
 ("You were handed sugar, softness, and starch, and your ancient mouth was never built to survive it.", 'you','wh','med',"being handed a tray of sugar, soft bread and candy, his ancient tooth overwhelmed",""),
 ("Every cavity you've ever had is a small record of that mismatch.", 'none','wh','close',"a single tooth with a cavity, the dark hole shaped like a tiny record mark",""),
 ("Every crooked tooth is your jaw telling you it never got fed the way it needed.", 'none','wh','med',"a crooked tooth with a tiny speech bubble coming from the jaw, a small plea",""),
 ("It's not a flaw in you. It's a Stone Age mouth, doing its best in a world it was never made for.", 'none','wh','med',"a Stone Age mouth icon doing its best, surrounded by modern skyscrapers and fast food",""),
 ("So the next time a dentist tells you to do better, you can. Brushing is real, and it matters.", 'you','bath','med',"brushing with a small determined nod, a green check, it really does matter",""),
 ("But know what you're really up against.", 'you','wh','close',"a serious knowing look aimed straight ahead",""),
 ("You're not fighting bad habits. You're fighting ten thousand years of a diet your mouth never agreed to.", 'you','wh','med',"standing small but firm facing a huge looming wave labeled with ten thousand years of diet","10,000 YEARS"),
 ("That crooked, patched-up, hard-working smile in the mirror is the most modern thing about you.", 'you','bath','med',"smiling a crooked patched-up smile into the bathroom mirror, a little proud",""),
 ("The caveman never had to fix his. He just ate, and the world hadn't broken his mouth yet.", 'cave','sav','med',"the caveman simply eating with a calm whole grin, the world still unbroken behind him",""),
 ("That's the difference. That's you.", 'you','wh','close',"pointing at himself with a small crooked-but-honest smile, a quiet identity payoff",""),
]

if __name__ == "__main__":
    import io
    lines = [d[0] for d in DATA]
    prompts = [build(d[1], d[2], d[3], d[4], d[5]) for d in DATA]
    n = len(DATA)
    with io.open("SHOTLINES_FULL.txt","w",encoding="utf-8") as f:
        f.write("\n".join(lines))
    with io.open("PROMPTS_FULL.txt","w",encoding="utf-8") as f:
        for i,p in enumerate(prompts,1):
            f.write("%03d.\n%s\n\n" % (i,p))
    with io.open("Script_Video09_narration_FROMGEN.txt","w",encoding="utf-8") as f:
        f.write("\n".join(lines))
    tag = "FULL 140" if n==140 else ("PARTIAL (%d shots)"%n)
    print("Shots: %d  [%s]" % (n, tag))

    # --- Tu kiem: shotline PHAI khop 100% voi file narration that (chong lech sync TTS) ---
    try:
        with io.open("Script_Video09_narration.txt","r",encoding="utf-8") as f:
            nar = [l.rstrip("\n") for l in f if l.strip()!=""]
        mism = 0
        if len(nar)!=n:
            print("!! WARNING: narration co %d dong nhung DATA co %d shot" % (len(nar), n))
        for i in range(min(len(nar), n)):
            if nar[i].strip()!=lines[i].strip():
                mism += 1
                if mism<=3:
                    print("!! LECH dong %03d:\n   narration: %s\n   DATA     : %s" % (i+1, nar[i], lines[i]))
        print("Kiem khop narration: %s (%d dong lech)" % ("OK 100%" if mism==0 and len(nar)==n else "CO LECH", mism))
    except FileNotFoundError:
        print("(khong thay Script_Video09_narration.txt de doi chieu)")

    print("=== SAMPLE 097 (nha khoa: khoan rang tinh) ===\n"+prompts[96])

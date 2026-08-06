# -*- coding: utf-8 -*-
# Generator prompt ảnh — Video06 "Why Do You Jerk Awake as You Fall Asleep?"
# Xuất: Script_Video06_narration.txt · SHOTLINES_FULL.txt · PROMPTS_FULL.txt
import os
HERE = os.path.dirname(os.path.abspath(__file__))

STYLE = ("Clean flat 2D cartoon explainer with smooth, even, confident medium-bold black outlines "
         "(single clean strokes, not scratchy, not wobbly, not heavy marker), a crisp minimalist educational look,")

CONSIST = ("The people are clean STICK-FIGURE doodles: a LARGE round white-filled head with a simple expressive face "
           "(two big round white eyes with small black pupils, thin expressive eyebrows, a tiny mouth, no nose) sitting on a THIN body "
           "made of clean black lines (a single medium-weight line for the torso plus thin noodle arms and legs) — NOT a filled or solid body shape, "
           "just clean stick lines, with simple rounded mitten hands and small oval feet, ALWAYS drawn as the SAME stickman, kept identical in every image. "
           "The modern man has a BALD round head with NO hair. Any animals and apes are simple and cute in flat SOLID COLOUR (never black-and-white), "
           "each with a little face, drawn with more detail and body volume than the simple stick people. "
           "Clean smooth evenly-weighted medium-bold black outlines; flat colours, NO gradient shading, a clean flat digital-explainer look, evenly drawn (not 3D, not glossy).")

NEG = ("Family-friendly, wholesome, cute, gentle, non-violent, no blood, no gore, no injury. no gradients, no textures, no photorealism, no 3D, "
       "no glossy render, no sketchy scratchy lines, no extra limbs or fingers, no watermark, no logo, no frame borders, no duplicate characters, "
       "no collage, no picture-in-picture, 16:9, clean educational YouTube explainer doodle style.")

CHAR = {
 'you': ("the recurring modern guy, the same plain black-outline STICK FIGURE with a plain round BALD white head and NO hair (just a simple face), "
         "a bare thin bold black stick-line body, thin noodle arms and legs, simple rounded mitten hands and small oval feet, "),
 'treeape': ("a small cute ancestor tree-ape, a stick-limbed primate with a round head, big round white eyes with black pupils, "
             "a flat light-brown furry body and long arms, "),
 'ape': ("a cute flat-coloured great ape (chimp / orangutan / gorilla) with a little round face and a solid brown or orange fur body, "),
 'none': "",
}

FRAME = {
 'm': "a medium shot, the subject drawn big and centered with clean breathing space around it.",
 'w': "a WIDE establishing shot, the subject fairly small inside a large scene.",
 'cu': "a tight CLOSE-UP on the face and shoulders, the expressive face filling most of the frame.",
 'hi': "a HIGH-ANGLE shot looking DOWN, making the subject look small and vulnerable.",
 'lo': "a LOW-ANGLE shot looking UP, making the subject look powerful.",
}

SCENE = {
 'br':   "ONE single scene: a flat dark navy-blue bedroom at night, a simple bed, a flat black floor line, lots of clean empty space, a soft dark-grey shadow; the white-filled black-outline doodle reads clearly on the dark background,",
 'wh':   "ONE single scene on a plain WHITE background with lots of clean empty space and a soft light-grey shadow under the subject; RED is the accent for danger/warnings/a big red X, GREEN for a check/yes, a small YELLOW lightbulb for an idea,",
 'brain':"ONE single scene on a plain WHITE background: one big simple cartoon brain shape as the focus, clean flat pink-beige fill with black outline, lots of empty space, small labels/arrows in black,",
 'tree': "ONE single scene: a flat blue sky over flat green treetops, one simple tree with a thick brown branch, lots of clean space, a soft grey shadow,",
 'treen':"ONE single scene: a flat dark-navy night sky with tiny white star dots over dark tree silhouettes, one thick branch, a calm moonlit tone,",
 'ground':"ONE single scene: a flat dark-navy night over a flat black-brown open ground line, tiny stars, wide empty space, a soft grey shadow,",
 'sav':  "ONE single scene: a flat dark-navy night over a flat olive-brown savanna ground, a distant acacia-tree silhouette, tiny stars,",
}

# (shotline, char, bg, frame, action, text)
DATA = [
 ("You're almost asleep.",'you','br','m',"lying in bed, eyelids heavy and half-closed, drowsy",""),
 ("Not quite dreaming, but close. That warm, heavy, sinking feeling.",'you','br','cu',"eyes nearly shut, a calm sinking expression, a tiny forming 'z'",""),
 ("You're safe. You're lying completely still. Nothing in the room has moved.",'you','br','w',"lying perfectly still in a quiet dark bedroom, everything calm",""),
 ("And then, out of nowhere, your whole body flinches.",'you','br','m',"whole body jolting violently, limbs snapping out, wide shocked eyes",""),
 ("Maybe your leg kicks. Maybe your arms shoot out.",'you','br','m',"one leg kicking out and arms shooting outward over the blanket",""),
 ("And for a split second, you're absolutely certain you were falling.",'you','wh','cu',"wide terrified eyes, arms flailing in a falling pose","FALLING?"),
 ("You weren't. You're in bed. You've been in bed the whole time.",'you','br','w',"sitting up a little, confused, looking around the still bedroom",""),
 ("But your heart's pounding like you just caught yourself at the edge of a cliff.",'you','br','cu',"a mitten hand on the chest, wide eyes, a small red pounding heart above",""),
 ("Here's the strange part.",'you','wh','m',"standing, tilting the head, a thought bubble with a question mark","?"),
 ("Almost everyone does this. Most of us, over and over, our whole lives.",'you','wh','w',"a row of several identical tiny stick figures in little beds, each jerking",""),
 ("It even has a name. Scientists call it a hypnic jerk.",'none','wh','m',"a big bold label card centered on white","HYPNIC JERK"),
 ("And nobody fully agrees on why it happens.",'you','wh','m',"several stick scientists shrugging with question marks above","?"),
 ("But the best explanation is a little unsettling.",'you','wh','cu',"leaning in with a curious, slightly worried face",""),
 ("Because your body isn't glitching. Your body thinks you're falling out of a tree.",'you','wh','m',"a thought bubble showing a tiny tree with a small figure slipping off it",""),
 ("Not a metaphor. An actual tree.",'none','wh','m',"one single simple flat green tree centered on white",""),
 ("The kind your ancestors slept in for millions of years, before there were beds, or floors, or a couch to drool on.",'treeape','tree','w',"a small furry ape asleep curled on a thick tree branch, tiny 'z'",""),
 ("That jolt might be one of the oldest reflexes you own.",'you','wh','m',"a small glowing 'ancient' scroll tag pinned on the chest",""),
 ("A twenty-million-year-old alarm, still going off, in a bedroom where there's nothing left to fall from.",'you','br','m',"lying in bed with a small red alarm bell ringing above the head",""),
 ("Stick around, because the weirdest part isn't the jerk itself.",'you','wh','m',"pointing forward with a curious expression",""),
 ("It's the tiny lie your brain tells you a split second after. We saved that one for the end.",'none','wh','m',"a simple brain shape with a small sneaky speech bubble","LATER"),
 # SETUP
 ("Let's get one thing straight first, because it flips how you see this.",'you','wh','m',"flipping a big card over with both hands",""),
 ("That jerk isn't your body failing to fall asleep.",'you','br','m',"in bed with a red X crossing out a small 'FAIL' tag","FAIL"),
 ("It's an older part of you refusing to fall without checking first.",'you','wh','m',"a small ancient guard-version of the figure holding one hand up, stop",""),
 ("And like most things about you, it isn't one clean story. It got built in layers.",'none','wh','m',"a neat stack of three labeled horizontal layers",""),
 ("One layer is what actually happens in your brain in the last second before sleep.",'none','brain','m',"a simple brain with a tiny clock reading one second",""),
 ("One is why falling, of all things, is the one danger that ancient part of you can't ignore.",'none','wh','m',"a small falling-figure icon circled in red",""),
 ("And the deepest layer is what your sleeping brain invents to explain the jolt after the fact.",'none','wh','m',"a brain with a little open storybook thought bubble",""),
 ("That last one is the part that'll stay with you.",'you','br','cu',"a thoughtful, faintly unsettled face in the dark",""),
 ("So let's climb back up into the trees, to a time when falling asleep and falling were the same deadly problem.",'treeape','tree','w',"a small ape climbing up a tall tree toward the branches",""),
 # CHUONG 1
 ("So let's slow the whole thing down, to the last few seconds before you're gone.",'you','br','m',"lying in bed, a small slow-motion clock symbol nearby",""),
 ("Falling asleep isn't a switch. It's a handover.",'none','wh','m',"two mitten hands passing a small glowing baton",""),
 ("All day, a system deep in your brainstem keeps you awake and alert.",'none','brain','m',"a brain with a glowing alert node at the base",""),
 ("Think of it as the part of you that runs the lights.",'you','wh','m',"standing beside a big light switch panel",""),
 ("As you drift off, it starts powering down, room by room.",'none','wh','w',"a little house cutaway with lights switching off room by room",""),
 ("Your heart slows. Your breathing gets long and even. Your muscles begin to let go.",'you','br','m',"lying relaxed, a slow heart symbol and calm breathing waves",""),
 ("That letting go is the important part.",'you','br','cu',"a peaceful loosening face, limbs going soft",""),
 ("Because to sleep, your body has to quietly switch off its own muscles.",'you','br','m',"muscles going limp, a small 'off' toggle over the arm",""),
 ("It powers you down on purpose, so you lie still instead of thrashing through the night.",'you','br','m',"lying perfectly still with a faint calm glow",""),
 ("And most nights, that shutdown is smooth. You never notice it.",'you','br','w',"sleeping peacefully in the dark bedroom, tiny 'z z z'",""),
 ("But sometimes, the timing slips.",'none','wh','m',"two gears slightly out of sync, one tooth catching",""),
 ("The wake system and the sleep system overlap for a moment, both half on.",'none','brain','m',"a brain split half-bright awake and half-dim asleep",""),
 ("And in that overlap, your brain picks up a strange signal.",'none','brain','cu',"a brain with a strange jagged red signal blip",""),
 ("It feels your muscles suddenly going slack. All of them. At once.",'you','br','m',"whole body going limp all at once, arms dropping",""),
 ("To a sleeping brain, one obvious thing makes a whole body go limp in an instant.",'none','wh','m',"a thought bubble weighing options, one glowing brighter",""),
 ("You've lost your grip. You're falling.",'you','wh','cu',"wide-eyed figure in a falling pose, hands grasping upward","FALLING"),
 ("So it does the only thing a body can do while it's falling. It fires. Hard.",'you','wh','m',"every muscle tensing, red action lines bursting outward",""),
 ("Every muscle it can reach, all at once, to grab something. Anything.",'you','wh','m',"arms and legs flinging out, grasping open hands",""),
 ("That's the kick. That's the flail.",'you','br','m',"a sharp kick-and-flail jolt in the bed",""),
 ("That's you, lying safely in bed, trying to catch a branch that isn't there.",'you','br','m',"reaching up to grab a faint dotted-outline branch that isn't there",""),
 ("Your body, running a rescue mission for a problem you don't have.",'you','wh','m',"a tiny rescue figure with a red cross saluting over a calm sleeper",""),
 ("And here's the detail that gives it all away.",'you','wh','m',"holding up a magnifying glass to a small clue",""),
 ("It happens most when you're overtired, stressed, or sleeping somewhere awkward. A chair. A plane. A desk.",'you','wh','w',"three tiny vignettes: asleep on a chair, on a plane seat, and at a desk",""),
 ("Exactly the situations where, a long time ago, dozing off in the wrong spot could get you killed.",'treeape','ground','m',"a small ape dozing in the open on the ground, a shadow with glowing eyes nearby",""),
 ("Which leaves one question hanging.",'you','wh','m',"a big question mark hanging over a tilted head","?"),
 ("Your brain had a hundred ways to misread a limp body.",'none','brain','m',"a brain with many little branching thought arrows",""),
 ("So why does it always jump straight to falling?",'none','wh','m',"one bold red arrow pointing down to a small falling icon",""),
 ("For that, we have to leave the bedroom. And climb.",'you','wh','w',"the stick figure walking toward a tall tree at the edge of frame",""),
 # CHUONG 2
 ("So climb.",'you','tree','w',"a stick figure starting to climb up a tall tree",""),
 ("Go back far enough, past the first cities and the first fields, and your ancestors aren't on the ground at all.",'none','wh','w',"a timeline: a tiny city, then a field, then a tree, an arrow going back in time",""),
 ("They're up in the trees.",'treeape','tree','w',"several small apes resting up in the treetops",""),
 ("For tens of millions of years, that's where primates like us slept. Up in the branches, off the ground.",'treeape','tree','w',"an ape asleep wedged in a fork of branches high up",""),
 ("And it was a good deal. The leopards and hyenas working the dark below mostly couldn't reach you up there.",'none','treen','w',"a cute leopard and a hyena prowling the dark ground far below a tall tree",""),
 ("But safety is never free. It just changes the bill.",'none','wh','m',"a small receipt/bill icon being handed over",""),
 ("On the ground, the danger was being eaten. In a tree, the danger was simpler. And dumber.",'none','wh','m',"a split card: a toothy predator icon versus a plain down-arrow",""),
 ("It was falling off.",'treeape','treen','m',"a small ape slipping off a branch, motion lines pointing down",""),
 ("And a fall back then wasn't a cast and a week off work.",'none','wh','m',"a red X over an arm cast and a calendar",""),
 ("It was a broken body, in a world with no medicine and a lot of hungry animals watching.",'none','treen','w',"a small ape crumpled on the ground with glowing predator eyes in the dark around",""),
 ("It didn't just hurt. It ended your line.",'none','wh','m',"a family-tree line snapping in two with a small red break",""),
 ("So for a sleeping tree-ape, one quiet threat outranked almost everything. Not the predator. Gravity.",'treeape','treen','m',"an ape on a branch, a big down-arrow labelled gravity bigger than a small predator icon",""),
 ("And evolution's fix was elegant, and a little paranoid.",'none','wh','m',"a small blueprint and gear with a tiny watchful eye",""),
 ("It wired in a reflex that never fully clocked out, not even in sleep.",'treeape','treen','cu',"a sleeping ape's face with one tiny alert eye half-open",""),
 ("A part of the brain that kept one eye on your grip, your balance, the tension in your muscles.",'none','brain','m',"a brain with a small eye watching a gripping-hand icon",""),
 ("And the instant that tension vanished, the way it does when you start to fall, it threw every muscle into grabbing back on.",'treeape','treen','m',"an ape suddenly clenching all four limbs to grab the branch",""),
 ("Re-grip. Now. Questions later.",'treeape','treen','cu',"an ape hand snapping shut tightly around a branch","GRIP"),
 ("That reflex kept your ancestors wedged in their branches, night after night, for millions of years.",'treeape','treen','w',"several apes safely wedged asleep across branches under the stars",""),
 ("The ones born without it slipped, and fell, and never became anyone's ancestor.",'treeape','treen','m',"one small ape falling away into the dark with a faint down-trail",""),
 ("You come from the good grippers.",'treeape','tree','m',"a proud ape holding a branch tightly with a small green check mark",""),
 ("And other apes still live this every night. A chimp, an orangutan, a gorilla.",'ape','tree','w',"a cute chimp, an orangutan and a gorilla, each up in a tree",""),
 ("Each one builds a fresh nest in the trees before dark, and sleeps holding on. They never had to give it up.",'ape','treen','m',"an ape settling into a leafy tree nest at dusk, holding a branch",""),
 ("But somewhere along the way, we did something they didn't. We came down.",'treeape','tree','m',"an ape climbing down the trunk toward the ground",""),
 ("We started sleeping on the ground. Flat, solid earth, with nothing to fall from and nothing to hold.",'treeape','ground','w',"an early human lying on flat open ground at night, arms at the sides",""),
 ("The tree is gone. The branch is gone. The drop is gone.",'none','wh','m',"a tree, a branch and a downward arrow, each with a small grey X",""),
 ("But the reflex is still in there. Fully staffed. Waiting for a slip that can't happen anymore.",'you','br','m',"a modern stick figure asleep with a faint old guard silhouette standing watch inside",""),
 ("So it waits. And most nights, nothing.",'you','br','w',"sleeping calmly in bed, quiet dark room, a tiny 'z'",""),
 ("Then, every so often, as you let go into sleep, it feels your grip disappear.",'you','br','m',"a mitten hand relaxing open in sleep, a faint dotted branch slipping away",""),
 ("And for one honest second, a twenty-million-year-old part of you is sure you're back in the tree, and the branch just gave way.",'you','treen','cu',"the sleeper's face overlaid with a ghostly branch snapping",""),
 ("Which should be the end of it. A charming old glitch, case closed.",'none','wh','m',"a closed file folder with a small tree doodle, stamped","CLOSED"),
 ("Except it isn't. Because this reflex does something a harmless leftover shouldn't.",'none','wh','m',"the closed folder popping back open with a red question mark","?"),
 ("It gets stronger when you're stressed, when you're worn out, when you're sleeping somewhere new.",'you','wh','w',"three vignettes: a stressed figure, an exhausted figure, a figure in a strange room",""),
 ("Almost like it isn't just remembering the fall. Like it's still on duty.",'you','br','m',"a small glowing guard badge on the sleeping figure","ON DUTY"),
 ("And that's where this stops being about trees, and starts being about something your brain is still doing tonight.",'none','brain','m',"a brain with a small active glowing watch-light",""),
 # CHUONG 3
 ("So let's follow the reflex forward, out of the trees, and into you.",'none','wh','w',"an arrow leading from a tree to a modern stick figure",""),
 ("Because that grip-check in your brain was never really about branches.",'none','brain','m',"a brain with a gripping-hand icon and a small fading branch",""),
 ("Branches were just the first thing it learned to guard.",'treeape','tree','m',"a small ape gripping a branch with a tiny shield symbol",""),
 ("Underneath, it's a simpler, older rule. When your body lets go, check that it's safe to.",'none','wh','m',"a simple rule card with a check mark and a relaxing hand",""),
 ("And that rule got wired straight into the part of you that watches for danger.",'none','brain','m',"a brain with a small watchtower/eye node glowing",""),
 ("Which is why the jerk isn't random. It has a pattern.",'none','wh','m',"scattered dots resolving into a clear pattern line",""),
 ("It shows up most on the worst nights. The overtired ones. The stressed ones. The first night somewhere unfamiliar.",'you','wh','w',"three tired vignettes of a figure struggling to sleep",""),
 ("Think about when that is.",'you','wh','m',"a figure with a thought bubble listing small icons",""),
 ("A strange room. A hard deadline. A body running on four hours of sleep.",'you','br','w',"a figure lying awake in an unfamiliar room, a clock showing four hours",""),
 ("To your ancient wiring, those aren't just inconveniences. They're threat signals.",'none','wh','m',"small icons each turning into a red alert triangle",""),
 ("New place, might not be safe. Exhausted, can't afford to be caught off guard. Stressed, something's wrong.",'treeape','ground','w',"a wary ape sitting up alert on open ground at night",""),
 ("And on nights like that, the part of you that keeps watch is reluctant to fully clock out.",'you','br','m',"a small inner guard refusing to lie down, one eye open",""),
 ("It hovers. Half-awake. One hand still on the switch.",'you','br','cu',"a half-open eye in the dark, a mitten hand near a light switch",""),
 ("Which means the handover into sleep gets rougher, and the misfires come more often.",'none','wh','m',"two gears grinding with small red spark misfires",""),
 ("The jerk isn't the guard failing. The jerk is the guard refusing to sit all the way down.",'you','br','m',"a determined little guard standing firm beside the sleeper",""),
 ("And this got more important, not less, the day we climbed down.",'treeape','ground','m',"an early human lying exposed on the open ground under the stars",""),
 ("Because sleeping on open ground is far more exposed than sleeping in a tree.",'none','sav','w',"a small figure sleeping in the open savanna with distant glowing eyes",""),
 ("Out there, a body that fully switched off, in the open, all night, was a body that might not wake up.",'none','sav','m',"a sleeping figure with a faint red warning and predators in the dark",""),
 ("So the watchfulness stayed. It just changed what it was watching for.",'none','wh','m',"an eye icon swapping a 'branch' label for a 'danger' label",""),
 ("From don't fall, to don't let go completely.",'none','wh','m',"two cards, a 'DON'T FALL' arrow changing into 'DON'T LET GO'",""),
 ("That's the same reason a new hotel room keeps you up, and the same reason you snap awake at 3am for no reason.",'you','br','w',"a figure wide awake in a plain hotel-like room, a clock at 3:00",""),
 ("It's one old system, still doing its job, in a body that no longer needs it to.",'you','br','m',"a tiny ancient machine ticking inside a peaceful sleeper",""),
 ("But we're still not at the strangest part.",'you','wh','m',"a figure peeking around a corner, curious",""),
 ("Because so far, this is just a jerk. A muscle, a misfire, a guard on edge.",'you','br','m',"a simple jolt in bed with small labels muscle and misfire",""),
 ("The truly odd thing is what your mind does with it, in the half-second after.",'none','brain','m',"a brain with a tiny stopwatch at half a second",""),
 ("It doesn't just wake you up. It hands you a story.",'none','wh','m',"a brain holding out a little open storybook",""),
 # CHUONG 4
 ("You've felt this, even if you've never named it.",'you','br','cu',"a knowing, slightly startled face in the dark",""),
 ("The jerk hits, and it doesn't arrive alone.",'you','br','m',"a jolt in bed with a small flash bubble appearing beside it",""),
 ("It comes wrapped in a tiny, vivid flash. You missed a step. You slipped off a curb. The ground wasn't where you left it.",'you','wh','w',"three quick flash images: missing a stair, slipping off a curb, ground vanishing",""),
 ("A half-second dream of falling, perfectly timed to the kick.",'you','br','m',"a dream bubble of falling synced with the leg kick",""),
 ("And here's the question that breaks people's brains a little.",'you','wh','m',"a figure with a slightly glitching question-mark over the head","?"),
 ("Which one came first?",'none','wh','m',"two cards, 'JERK' and 'DREAM', with a versus question mark","?"),
 ("It feels obvious. You dreamed you were falling, so your body flinched. Cause, then effect.",'none','wh','m',"an arrow from a dream icon to a jerk icon, labelled cause and effect",""),
 ("But the timing doesn't work that way.",'none','wh','m',"the arrow flipping around with a red X on the old order",""),
 ("The muscle jerk comes from a fast, primitive part of the brain. It fires almost instantly.",'none','brain','m',"a brain with a fast lightning bolt at the base",""),
 ("The dream, the story, the missed step, comes from slower machinery. The part that makes sense of things.",'none','brain','m',"a brain with a slow gear at the top, thinking",""),
 ("Which means the fall you remember didn't cause the jerk.",'none','wh','m',"a 'fall memory' card with a grey X, not the cause",""),
 ("The jerk came first. And then your sleeping brain, blindsided by a sudden jolt, went looking for a reason.",'none','brain','m',"a startled brain holding a flashlight, searching",""),
 ("And in a fraction of a second, it wrote one.",'none','wh','m',"a quick pen writing a tiny story in a flash",""),
 ("It reached for the oldest explanation it had for a body lurching in the dark, and served it back to you as a memory.",'none','wh','m',"a brain pulling an old 'falling' file and stamping it MEMORY","MEMORY"),
 ("You didn't dream a fall and flinch.",'none','wh','m',"a crossed-out order, dream then flinch, with a grey X",""),
 ("You flinched, and your brain invented a fall to explain the flinch.",'none','wh','m',"the correct order, flinch then invented dream, with a green check",""),
 ("A story, built backward, faster than you could notice, to make a twitch feel like it made sense.",'none','wh','m',"a small story assembling itself in reverse",""),
 ("Sit with that for a second.",'you','wh','m',"a figure sitting quietly, thinking, a small pause symbol",""),
 ("The part of you that's supposed to be resting just fabricated a small false memory, in real time, and you believed it completely.",'you','br','cu',"an unsettled thoughtful face with a tiny false-memory bubble",""),
 ("That's not a bug in your sleep. That's your brain doing the one thing it can never stop doing. Explaining you to yourself.",'none','brain','m',"a brain gently narrating to a small figure of you",""),
 # KET
 ("So. Why do you jerk awake as you fall asleep?",'you','wh','m',"a figure standing with the big title question above",""),
 ("Not because you're stressed, though that doesn't help.",'you','wh','m',"a small grey 'stress' cloud with a grey X",""),
 ("Not because of the coffee, though that doesn't help either.",'you','wh','m',"a coffee cup with a grey X",""),
 ("You jerk awake because a piece of you never came down from the trees.",'treeape','tree','m',"a faint ape still up in a tree overlaid behind the modern figure",""),
 ("A twenty-million-year-old reflex, built to catch a falling ape, still standing guard over a body that sleeps on solid ground.",'you','br','m',"a ghostly ape-guard standing over the sleeping modern figure",""),
 ("The branch rotted away a hundred thousand centuries ago.",'none','wh','m',"an old branch crumbling to dust",""),
 ("The grip never did.",'you','wh','cu',"a strong tightly closed grip, still holding",""),
 ("So the next time you're drifting off, and your whole body kicks, and you snap back with your heart pounding over nothing.",'you','br','m',"a jolt awake in bed with a small red heart, over nothing",""),
 ("Don't be annoyed with it.",'you','br','cu',"a softening, understanding face",""),
 ("That flinch is a receipt.",'none','wh','m',"a small receipt with a tiny tree printed on it",""),
 ("It's proof you come from an unbroken line of animals who, every single night, for millions of years, did not fall.",'treeape','treen','w',"a long line of apes each safely gripping branches across generations",""),
 ("Every one of them held on. Long enough to make the next one. All the way down to you.",'none','wh','w',"a chain of tiny gripping hands leading to a modern stick figure",""),
 ("The tree is gone. The drop is gone. The danger is gone.",'none','wh','m',"a tree, a drop-arrow and a predator, each fading grey",""),
 ("But the grip is still there. Quiet. Loyal. Ready.",'you','br','cu',"a calm sleeping figure with a faint steady glow in the hand",""),
 ("Reaching, one more time, for a branch that isn't there.",'you','br','m',"asleep, one hand gently reaching up toward a faint dotted absent branch",""),
 ("That's not a glitch.",'none','wh','m',"a 'GLITCH' label with a grey X",""),
 ("That's you, still holding on.",'you','wh','m',"the stick figure holding on tight in a small proud stance",""),
 ("If you made it to the end, tell me one thing in the comments. When you jerk awake, do you ever see where you fell? A stair, a curb, a step? Tell me what your brain shows you.",'you','wh','m',"a figure beside a big comment box with a stair, curb and step icon","COMMENT"),
]

def textpart(t):
    return ('a small "%s" in bold white ALL-CAPS letters on a little red tag.' % t) if t else "no text or letters."

def build(subject_char, action, bg, frame, text):
    subj = (CHAR[subject_char] + action).strip()
    if subject_char == 'none':
        subj = action
    return "%s %s. Framing: %s %s %s %s %s" % (STYLE, subj, FRAME[frame], CONSIST, SCENE[bg], textpart(text), NEG)

shot_lines, prompts = [], []
for i,(line,ch,bg,fr,act,txt) in enumerate(DATA,1):
    n = "%03d" % i
    shot_lines.append("%s  %s" % (n, line))
    prompts.append("%s.\n%s" % (n, build(ch,act,bg,fr,txt)))

with open(os.path.join(HERE,"Script_Video06_narration.txt"),"w") as f:
    f.write("\n".join(l for (l,*_) in DATA))
with open(os.path.join(HERE,"SHOTLINES_FULL.txt"),"w") as f:
    f.write("\n".join(shot_lines))
with open(os.path.join(HERE,"PROMPTS_FULL.txt"),"w") as f:
    f.write("\n\n".join(prompts))

print("Shots:", len(DATA))
print("Files: Script_Video06_narration.txt, SHOTLINES_FULL.txt, PROMPTS_FULL.txt")

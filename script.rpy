
define r = Character("Rat")

define rw = Character("Rat waiter")

define s = Character("Salamander")

init python:
    renpy.music.register_channel("rain",loop=True)

label start:

    stop music fadeout 3.0

    scene sidewalk
    with dissolve

    play rain "audio/rain.mp3" loop fadein 3.0


    "A rat walks through the sidewalk."

    "There's no end in sight."

    show rat happy
    with dissolve

    "The rain falls lightly, the other people start to walk faster to avoid the rain."

    r "Looks like it's time for some food."

    "A kind restaurant, with a short menu of two items."

    "- Potatos in cheese sauce
     - Melted cheese over rice."

    r "I don't like cheese but it should do."

    "The Rat walked to the door and opened it."



    scene restaurant salamander

    play rain "audio/inside rain.mp3"


    show rat happy
    with dissolve

    "The Rat looked around."

    "Doesn't look well drawn but I'm starving, so I'll stay. He thought to himself."

    "The rat sat down in the table right to it's left, near the window"

    show rat happy

    scene restaurant both

    play music "audio/Tautology.mp3"

    "The rat waiter walked down from the kitchen to the table."

    rw "Welcome, would you like to drink something or shall I bring your main dish?"

    r "I would like some coffee first, no sugar."

    rw "Certainly, please excuse me."

    "A moment passes and the rat sees a salamander sitting at the other side of the room."

    s "Thank you for being here."

    s "Such an act of love is appreciated."

    "The rat began looking around him."

    r "Me?"

    s "Not quite, but yes, indeed I was also talking to you."

    r "What for?"

    "The salamander paused."

    s "For being with me here of course."

    s "Listening to music, paying attention to what I'm saying, I feel like it's an act of love."

    s "Don't you know what love is?"

    r "Intimate moments perhaps."

    s "Most certainly, I was reffering to love as respect."

    r "Respect?"

    s "Acceptance of the other party as a legitimate expression of themselves in coexistence."

    "The rat waiter had to cut the conversation in half, as she brought the coffe to the table."

    rw "Please excuse me kind gentlemen, here's your coffee, would you like to order now?"

    r "Yes, I would like..."


    menu:
        "Potatos in cheese sauce.":
            r  "Potatos in cheese sauce."


        "Melted cheese over rice.":
            r "Melted cheese over rice."

    rw "Most certainly."

    "As the waiter was walking back to the kitchen, the rat keep thinking about the thing that was said by the old salamander."


    menu:

        "I may not feel like I understand, but I think it's an interesting view.":
            jump No

        "Do you usually start conversations without looking at people?":
            jump Yes






label Yes:
    r "Do you usually start conversations without looking at people?"
    s "You'd have to excuse me."
    s "Not too long ago I was part of some experiments, while I was being drawn."
    s "They left my eyes like this."
    r "Does it hurt?"
    s "Not really, I can't really feel can I?"
    r "Interesting..."

    jump last




label No:
    r "I may not feel like I understand, but I think it's an interesting view."
    r "Where did you learned that?"
    s "When you're old you get to experience a lot."
    s "I was 92."
    s "You do seem younger than me, but only in age."
    r "Haha, what, do minds have ages now?"
    s "I may not have an answer for you."
    r "Interesting..."



    jump last

label last:

    s "Interesting or not, I can only feel what my body allows me to feel."
    r "And what are you feeling right now?"
    s "Roughness, toughness, not very colored being honest."
    "The rat waiter brought the food."
    rw "For you, please have a nice meal."
    "The rat began eating."
    s "Bon appetit."
    r "Thank you, perhaps you already had your food?"
    "The rat took a bite."
    s "I just come here for tea, but as you can see, I already finished it before you came in, as he was too lazy to draw it."
    "The rat wondered if he had really taken a bite."

    s "I must go now, but I feel like we'll be speaking again to eachother."

    s "See you again later."

    scene restaurant rat

    "The rat continued eating?"
    "Thinking a bit about the weird scene that had just happened. As the salamander had vanished into thin air."

    rw "Everything good? I see you already finished."

    r "Yes, thank you."

    rw "Perhaps you'd like something else?"

    menu:
        "No thanks.":
            r "No thanks."

        "Do you have (insert player favorite food)?":
            rw "I'm afraid we do not have it."
            r "Thats a shame..."

    r "How much is it?"

    rw "Do not worry sir, your food was already paid for."

    r "Wait what? By who?"

    rw "The kind sir salamander that just left, he always does this."

    r "I must go and thank him, thanks for the food."

    rw "Please come again!"

    stop music fadeout 3.0

    scene sidewalk
    with dissolve

    play rain "audio/rain.mp3" loop fadein 3.0

    "The rat ran outside to find the salamander, but it was nowhere to be seen."

    r "I couldn't thank him..."

    r "But this gives me a weird feeling."

    r "Maybe I already had that conversation?"

    "A rat walks through the sidewalk."

    "There's no end in sight."

    return

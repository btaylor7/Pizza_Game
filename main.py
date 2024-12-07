def on_on_overlap(sprite2, otherSprite2):
    game.over(False, effects.dissolve)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap)

def on_on_overlap2(sprite, otherSprite):
    global x, y
    info.change_score_by(1)
    # Play quick sound effect
    music.pew_pew.play()
    # A4 note for 100ms
    x = randint(20, scene.screen_width() - 20)
    y = randint(20, scene.screen_height() - 20)
    while abs(x - mySprite.x) < 30 or abs(y - mySprite.y) < 30:
        x = randint(20, scene.screen_width() - 20)
        y = randint(20, scene.screen_height() - 20)
    pizza.set_position(x, y)
    info.start_countdown(timer)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap2)

ghosts: List[Sprite] = []
mySprite2: Sprite = None
spawnY = 0
spawnX = 0
ghostCount = 0
previousScore = 0
y = 0
x = 0
pizza: Sprite = None
mySprite: Sprite = None
timer = 0
timer = 10
scene.set_background_color(8)
mySprite = sprites.create(img("""
        . . . . c c c c c c . . . . . . 
            . . . c 6 7 7 7 7 6 c . . . . . 
            . . c 7 7 7 7 7 7 7 7 c . . . . 
            . c 6 7 7 7 7 7 7 7 7 6 c . . . 
            . c 7 c 6 6 6 6 c 7 7 7 c . . . 
            . f 7 6 f 6 6 f 6 7 7 7 f . . . 
            . f 7 7 7 7 7 7 7 7 7 7 f . . . 
            . . f 7 7 7 7 6 c 7 7 6 f c . . 
            . . . f c c c c 7 7 6 f 7 7 c . 
            . . c 7 2 7 7 7 6 c f 7 7 7 7 c 
            . c 7 7 2 7 7 c f c 6 7 7 6 c c 
            c 1 1 1 1 7 6 f c c 6 6 6 c . . 
            f 1 1 1 1 1 6 6 c 6 6 6 6 f . . 
            f 6 1 1 1 1 1 6 6 6 6 6 c f . . 
            . f 6 1 1 1 1 1 1 6 6 6 f . . . 
            . . c c c c c c c c c f . . . .
    """),
    SpriteKind.player)
controller.move_sprite(mySprite)
pizza = sprites.create(img("""
        . . . . . . b b b b . . . . . . 
            . . . . . . b 4 4 4 b . . . . . 
            . . . . . . b b 4 4 4 b . . . . 
            . . . . . b 4 b b b 4 4 b . . . 
            . . . . b d 5 5 5 4 b 4 4 b . . 
            . . . . b 3 2 3 5 5 4 e 4 4 b . 
            . . . b d 2 2 2 5 7 5 4 e 4 4 e 
            . . . b 5 3 2 3 5 5 5 5 e e e e 
            . . b d 7 5 5 5 3 2 3 5 5 e e e 
            . . b 5 5 5 5 5 2 2 2 5 5 d e e 
            . b 3 2 3 5 7 5 3 2 3 5 d d e 4 
            . b 2 2 2 5 5 5 5 5 5 d d e 4 . 
            b d 3 2 d 5 5 5 d d d 4 4 . . . 
            b 5 5 5 5 d d 4 4 4 4 . . . . . 
            4 d d d 4 4 4 . . . . . . . . . 
            4 4 4 4 . . . . . . . . . . . .
    """),
    SpriteKind.food)

def on_forever():
    global spawnX, spawnY, mySprite2, ghostCount, previousScore, ghosts, timer
    if info.score() % 5 == 0 and info.score() != previousScore and ghostCount < 5:
        scene.set_background_color(randint(0, 100))
        spawnX = randint(20, scene.screen_width() - 20)
        spawnY = randint(20, scene.screen_height() - 20)
        while abs(spawnX - mySprite.x) < 30 or abs(spawnY - mySprite.y) < 30:
            spawnX = randint(20, scene.screen_width() - 20)
            spawnY = randint(20, scene.screen_height() - 20)
        mySprite2 = sprites.create(img("""
                ........................
                            ..........ffff..........
                            ........ff1111ff........
                            .......fb111111bf.......
                            .......f11111111f.......
                            ......fd11111111df......
                            ......fd11111111df......
                            ......fddd1111dddf......
                            ......fbdbfddfbdbf......
                            ......fcdcf11fcdcf......
                            .......fb111111bf.......
                            ......fffcdb1bdffff.....
                            ....fc111cbfbfc111cf....
                            ....f1b1b1ffff1b1b1f....
                            ....fbfbffffffbfbfbf....
                            .........ffffff.........
                            ...........fff..........
                            ........................
            """),
            SpriteKind.enemy)
        # Play quick sound effect
        music.spooky.play()
        mySprite2.set_velocity(randint(-30, 30), randint(-30, 30))
        mySprite2.set_flag(SpriteFlag.BOUNCE_ON_WALL, True)
        mySprite2.set_position(spawnX, spawnY)
        ghosts.append(mySprite2)
        ghostCount += 1
        previousScore = info.score()
    if ghostCount == 5 and info.score() % 25 == 1:
        for ghost in ghosts:
            ghost.destroy()
        ghosts = []
        ghostCount = 0
        if timer > 2:
            timer += 0 - 2
        game.show_long_text("Next stage: timer reduced by 2 seconds.",
            DialogLayout.CENTER)
        info.start_countdown(timer)
        previousScore = info.score()
    if info.score() >= 100:
        game.over(True)
forever(on_forever)

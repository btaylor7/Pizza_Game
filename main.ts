sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite2, otherSprite2) {
    game.over(false, effects.dissolve)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function (sprite, otherSprite) {
    info.changeScoreBy(1)
    // Play quick sound effect
    music.pewPew.play()
    // A4 note for 100ms
    x = randint(20, scene.screenWidth() - 20)
    y = randint(20, scene.screenHeight() - 20)
    while (Math.abs(x - mySprite.x) < 30 || Math.abs(y - mySprite.y) < 30) {
        x = randint(20, scene.screenWidth() - 20)
        y = randint(20, scene.screenHeight() - 20)
    }
    pizza.setPosition(x, y)
    info.startCountdown(timer)
})
let ghosts: Sprite[] = []
let mySprite2: Sprite = null
let spawnY = 0
let spawnX = 0
let ghostCount = 0
let previousScore = 0
let y = 0
let x = 0
let pizza: Sprite = null
let mySprite: Sprite = null
let timer = 0
timer = 10
scene.setBackgroundColor(8)
mySprite = sprites.create(img`
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
    `, SpriteKind.Player)
controller.moveSprite(mySprite)
pizza = sprites.create(img`
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
    `, SpriteKind.Food)
forever(function () {
    if (info.score() % 5 == 0 && info.score() != previousScore && ghostCount < 5) {
        scene.setBackgroundColor(randint(0, 100))
        spawnX = randint(20, scene.screenWidth() - 20)
        spawnY = randint(20, scene.screenHeight() - 20)
        while (Math.abs(spawnX - mySprite.x) < 30 || Math.abs(spawnY - mySprite.y) < 30) {
            spawnX = randint(20, scene.screenWidth() - 20)
            spawnY = randint(20, scene.screenHeight() - 20)
        }
        mySprite2 = sprites.create(img`
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
            `, SpriteKind.Enemy)
        // Play quick sound effect
        music.spooky.play()
        mySprite2.setVelocity(randint(-30, 30), randint(-30, 30))
        mySprite2.setFlag(SpriteFlag.BounceOnWall, true)
        mySprite2.setPosition(spawnX, spawnY)
        ghosts.push(mySprite2)
        ghostCount += 1
        previousScore = info.score()
    }
    if (ghostCount == 5 && info.score() % 25 == 1) {
        for (let ghost of ghosts) {
            ghost.destroy()
        }
        ghosts = []
        ghostCount = 0
        if (timer > 2) {
            timer += 0 - 2
        }
        game.showLongText("Next stage: timer reduced by 2 seconds.", DialogLayout.Center)
        info.startCountdown(timer)
        previousScore = info.score()
    }
    if (info.score() >= 100) {
        game.over(true)
    }
})

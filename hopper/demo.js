// Hopper //
var Beaver = function (x, y) {
    this.x = x;
    this.y = y;
    this.img = getImage("creatures/Hopper-Happy");
    this.sticks = 0;
};
// hopper y sus movimientos //
Beaver.prototype.draw = function () {
    fill(255, 0, 0);
    this.y = constrain(this.y, 0, height - 95);
    image(this.img, this.x, this.y, 40, 40);
};

Beaver.prototype.hop = function () {
    this.img = getImage("creatures/Hopper-Jumping");
    this.y -= 9;
};

Beaver.prototype.fall = function () {
    this.img = getImage("creatures/Hopper-Happy");
    this.y += 9;
};

Beaver.prototype.checkForStickGrab = function (stick) {
    if ((stick.x >= this.x && stick.x <= (this.x + 40)) &&
        (stick.y >= this.y && stick.y <= (this.y + 40))) {
        stick.y = -400;
        this.sticks++;
    }
};
// lo que tiene que juntar//
var Stick = function (x, y) {
    this.x = x;
    this.y = y;
};

Stick.prototype.draw = function () {

    image(getImage("avatars/leaf-green"), this.x, this.y, 41, 34);
    fill(89, 71, 0);
    rectMode(CENTER);
    rect(this.x - 84, this.y + 15, 5, 40);

};

var beaver = new Beaver(200, 300);

var sticks = [];
for (var i = 0; i < 40; i++) {
    sticks.push(new Stick(i * 40 + 300, random(20, 260)));
}

var grassXs = [];
for (var i = 0; i < 25; i++) {
    grassXs.push(i * 20);
}

draw = function () {

    // static
    background(208, 238, 242);
    fill(255, 255, 0);
    ellipse(26, 17, 80, 80);
    fill(9, 171, 9);
    rectMode(CORNER);
    rect(0, height * 0.90, width, height * 0.10);

    for (var i = 0; i < grassXs.length; i++) {
        image(getImage("cute/GrassBlock"), grassXs[i], height * 0.85, 20, 20);
        image(getImage("cute/TreeUgly"), grassXs[i], height * 0.85, 47, 47);
        grassXs[i] -= 1;
        if (grassXs[i] <= -20) {
            grassXs[i] = width;
        }
    }
    // conteo de puntos//    
    for (var i = 0; i < sticks.length; i++) {
        sticks[i].draw();
        beaver.checkForStickGrab(sticks[i]);
        sticks[i].x -= 1;
    }
    fill(23, 42, 250);
    textSize(18);
    text("Puntos: " + beaver.sticks, 81, 32);

    if (beaver.sticks / sticks.length >= 50) {
        fill(255, 234, 0);
        textSize(36);
        text("Ganaste!!!!", 100, 200);
    }

    if (keyIsPressed && keyCode === 0) {
        beaver.hop();
    } else {
        beaver.fall();
    }
    beaver.draw();
};

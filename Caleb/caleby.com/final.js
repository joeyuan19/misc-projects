var cy
var pause = false;
var key_held = false;
var frame = 0;
               //0             //1           //2             //3             //4             //5           //6            //7           //8          //9             //10           //11
var bg =       [[13, 29, 60],   [10, 10, 150],[170, 25, 25],  [175, 175, 175],[0,0,0],        [27, 77, 62], [238, 177, 17],[58, 21, 90], [0, 0, 0],   [255, 255, 255],[26, 148, 80], [2, 132, 130]];
var cy_color = [[130, 200, 230],[250, 69, 10],[200, 200, 200],[151, 105, 79], [230, 215, 135],[150, 10, 10],[10, 10, 255], [128, 0, 128],[50, 50, 50],[225, 225, 225],[255, 211, 25],[170, 3, 135]];
var amb_light = [20,             0,            50,             0,              0,              15,           15,            0,            0,           150,            0,             0];
//make entry for each color scheme
var color_scheme_index = 0;
// 0
// background - navy 13, 29, 60
// caleb - icey blue 0, 240, 200
// amb light - 75
// amb material - 255

// 1
// background - deep blue 10, 10, 150
// caleb - orange 250, 69, 10
// amb light - 20
// amb material - 255

// 2
// background - deep red 170, 25, 25
// caleb - light silver 200, 200, 200
// amb light - 0
// amb material -255

// 3
// background - off white 175
// caleb - bronze 151, 105, 79
// amb light - 20
// amb material - 255

// 4
// background - black 0
// caleb - light gold 230, 215, 135
// amb light - 0
// amb material - 255

// 5
// background - forest green 27, 77, 62
// caleb - burgundy 150, 10, 10
// amb light - 20
// amb material - 255 

// 6
// background - gold yellow 255, 195, 77
// caleb - blue 10, 10, 255
// amb light - 20
// amb material - 255 

// 7
// background - purple 58, 21, 90
// caleb - dutty purple 128, 0, 128
// amb light - 0
// amb material - 255

// 8
// background - black 0, 0, 0
// caleb - dark grey 50, 50, 50
// amb light - 150
// amb material - 255

// 9
// background - white 255, 255, 255
// caleb - dark white 225, 225, 225
// amb light - 150
// amb material - 255 

// 10
// background - Brazil green 26, 148, 80
// caleb - Brazil yellow 255, 211, 25
// amb light - 0
// amb material - 255 

// 11
// background - 
// caleb - 
// amb light - 0
// amb material - 255



function setup() {
	createCanvas(1050, 700, WEBGL);
	background(0);
	cy = loadModel("cyType.obj")
	color_scheme_index = int(bg.length*random());
}

function draw() {
	background(bg[color_scheme_index][0],bg[color_scheme_index][1],bg[color_scheme_index][2]);
	var mX = mouseX;//map(mouseX, 0, width, 0, 0);
	var mY = mouseY;//map(mouseY, 0, height, 0, 0);
	camera(0, 50, 0);
	ambientLight(amb_light[color_scheme_index]);
	var dirX = (mouseX / width -0.5) *(2000);
	var dirY = (mouseY / height - 0.5) *(-2000);
	// directionalLight(255, dirX, dirY, 500);
	// directionalLight(0, 250, 0, dirX, dirY, 100)
	pointLight(cy_color[color_scheme_index][0],cy_color[color_scheme_index][1],cy_color[color_scheme_index][2], dirX, dirY, -150);
	ambientMaterial(255);
	scale(20, 20);
	if (!pause) {
		frame += 1;
	}
	// rotateX(frame * -0.025);
	rotateY(frame * -0.02);
	// rotateZ(frame * 0.025);
	push();
	translate(-21, -19, 0);
	model(cy);
	// translate(21, 24, 1);
	// // fill(0, 240, 200);
	// box(47, 2, 2);
	pop();
	// rotateX(map(mouseY, 0, height, 0, PI));
	// rotateZ(map(mouseX, 0, width, 0, PI));
	// box(800, 200, 30);
}

function keyPressed() {
	pause = !pause;
	/*if (!key_held) {
		key_held = true;
		pause = !pause;

	}*/
}

// function keyReleased() {
// 	//key_held = false;
// }


// 1
// background - navy 13, 29, 60
// caleb - icey blue 0, 240, 200
// amb light - 75
// amb material - 255

// 2
// background - deep blue 10, 10, 150
// caleb - orange 250, 69, 10
// amb light - 20
// amb material - 255

// 3
// background - deep red 170, 25, 25
// caleb - light silver 200, 200, 200
// amb light - 0
// amb material -255

// 4
// background - off white 175
// caleb - bronze 151, 105, 79
// amb light - 20
// amb material - 255

// 5
// background - black 0
// caleb - light gold 230, 215, 135
// amb light - 0
// amb material - 255

// 6
// background - forest green 27, 77, 62
// caleb - burgundy 150, 10, 10
// amb light - 20
// amb material - 255 

// 7
// background - gold yellow 255, 195, 77
// caleb - blue 10, 10, 255
// amb light - 20
// amb material - 255 

// 8
// background - purple 58, 21, 90
// caleb - dutty purple 28, 0, 128
// amb light - 0
// amb material - 255


// greenish navy 10, 30, 50
// icier blue 130,200,230
// dark gold 160, 145, 70
// light bronze 151, 105, 79

// bogo size - coordinates: 50, 10, 2 - 20, 20, -2
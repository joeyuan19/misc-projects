#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <cmath>
#include <random>
#include <vector>
#include <sstream>
#include <SDL2/SDL.h>

using namespace std;

const int SQUARE_SIDE = 10;
const int SCREEN_WIDTH  = 25*SQUARE_SIDE;
const int SCREEN_HEIGHT = 25*SQUARE_SIDE;
const int FRAME_RATE = 200;

const int W = SCREEN_WIDTH/SQUARE_SIDE;
const int H = SCREEN_HEIGHT/SQUARE_SIDE;
const int C = 3; 

int image[W*H*C];

int N;
int image_index;

bool init_sdl();
bool loadMedia();
bool close();

SDL_Window * window = NULL;
SDL_Renderer * renderer = NULL;

int get(int w, int h, int c) {
    return image[w*H*C+h*C+c];
}

int set(int w, int h, int c, int value) {
    return image[w*H*C+h*C+c] = value;
}

int set(int n, int value) {
    return image[n] = value;
}

void renderFillRect(SDL_Renderer * renderer, int w, int h) {
    const SDL_Rect rect = {w*SQUARE_SIDE, h*SQUARE_SIDE, SQUARE_SIDE, SQUARE_SIDE}; 
    SDL_RenderFillRect(renderer, &rect);
}

void color() {
    SDL_SetRenderDrawColor(renderer,0xFF,0xFF,0xFF,0xFF);
    SDL_RenderClear(renderer);
    int w, h;
    for (w = 0; w < W; w++) {
        for (h = 0; h < H; h++) {
            SDL_SetRenderDrawColor(renderer, get(w,h,0), get(w,h,1), get(w,h,2), 0xFF);
            renderFillRect(renderer,w,h);
        }
    }
}
void process_line(string line) {
    int tmp, j = 0;
    string buf = "";
    for (int i = 0; i < line.size(); i++) {
        if (line[i] == ',') {
            stringstream(buf) >> tmp;
            set(j,tmp);
            j++;
            buf = "";
        } else {
            buf += line[i];
        }
    }
}

void load_image(int n) {
    ostringstream oss;
    oss <<  n;
    string fname = "out/img-evolve-" + oss.str() + ".txt";
    ifstream f (fname.c_str());
    string line;
    while (getline(f,line)) {
        process_line(line);
    }
    f.close();
}

void test() {
    for (int w = 0; w < W; w++) {
        for (int h = 0; h < H; h++) {
            set(w,h,0,125);
        }
    }
}

bool init() {
    image_index = 0;
    if (image_index <= N) {
        load_image(image_index);
        color();
        image_index++;
    }
    return true;
}


bool render() {
    bool success = true;
    
    if (image_index <= N) {
        load_image(image_index);
        color();
        image_index++;
    } else if (image_index == N+1) {
        cout << "END" << endl;
        image_index++;
    }
    
    SDL_Delay(FRAME_RATE);
    SDL_RenderPresent(renderer);
    return success;
}

bool init_sdl() {
    bool success = true;

    if ( SDL_Init( SDL_INIT_VIDEO ) < 0 ) {
        printf("SDL could not initialize! SDL_Error: %s\n", SDL_GetError());
        success = false;
    } else {
        if ( !SDL_SetHint( SDL_HINT_RENDER_SCALE_QUALITY, "1") ) {
            printf("Warning: Linear texture filtering not enabled!");
        }

        window = SDL_CreateWindow("SDL Tutorial", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, SCREEN_WIDTH, SCREEN_HEIGHT, SDL_WINDOW_SHOWN);
        if ( window == NULL ) {
            printf("Window could not be created! SDL_Error: %s\n", SDL_GetError());
            success = false;
        } else {
            renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);
            SDL_SetRenderDrawColor(renderer,0xff,0xff,0xff,0xff);
            SDL_RenderClear(renderer);
        }
    }
    return success;
}

bool loadMedia() {
    bool success = true;
    return success;
}

bool close() {
    SDL_DestroyRenderer(renderer);
    renderer = NULL;

    SDL_DestroyWindow(window);
    window = NULL;

    SDL_Quit();

    return true;
}


int main(int argc, char *argv[ ] )
{
    stringstream(argv[1]) >> N;
    if ( !init_sdl() || !init()) {
        printf("Failed to initialize!\n");
    } else {
        if ( !loadMedia() ) {
            printf("Failed to load media!\n");
        } else {
            bool quit = false;
            SDL_Event e;
            if (init()) {
                while ( !quit ) {
                    while ( SDL_PollEvent( &e ) != 0 ) {
                        if ( e.type == SDL_QUIT ) {
                            quit = true;
                        }
                    }
                    if (!render()) {
                        quit = true;
                    }
                }
            }
        }
    }
    
    close();

    return 0;
}

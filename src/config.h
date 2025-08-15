#pragma once

// Window and Frame Rate
const int WIDTH = 1600;
const int HEIGHT = 900;
const int FPS = 60;

// Simulation Parameters
const int PARTICLE_DENSITY = 20000; // Feel free to increase this significantly!
const float BLACKHOLE_SIZE = 20.0f;

const float GRAVITATION_CONSTANT = 1000.0f;
const float FIELD_VARIATION = 1.5f;
const float TANGENTIAL_FACTOR = 0.3f;
const float MAX_VELOCITY = 8.0f;

// 0: White, 1: Color by Force, 2: Color by Velocity
const int COLOR_VARIATION = 2;

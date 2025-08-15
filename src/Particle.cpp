#include "Particle.h"
#include "BlackHole.h"
#include "config.h"
#include <cmath>
#include <random>

// Helper for random number generation
namespace {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<> dis(-0.5, 0.5);
}

const float Particle::MAX_SPEED = MAX_VELOCITY;

Particle::Particle(float x, float y) : pos(x, y), speed(0), force(0) {
    vel.x = dis(gen);
    vel.y = dis(gen);
}

void Particle::update(const BlackHole& blackHole) {
    sf::Vector2f delta = blackHole.pos - this->pos;
    float dist = std::sqrt(delta.x * delta.x + delta.y * delta.y);

    if (dist > blackHole.radius) {
        // Gravitational force
        this->force = GRAVITATION_CONSTANT / std::pow(dist, FIELD_VARIATION);

        float angle = std::atan2(delta.y, delta.x);

        // Calculate gravitational and tangential acceleration
        sf::Vector2f acceleration;
        acceleration.x = this->force * std::cos(angle);
        acceleration.y = this->force * std::sin(angle);

        sf::Vector2f tangential_accel;
        tangential_accel.x = -this->force * TANGENTIAL_FACTOR * std::sin(angle);
        tangential_accel.y = this->force * TANGENTIAL_FACTOR * std::cos(angle);

        // Update velocity
        this->vel += acceleration + tangential_accel;

        // Limit velocity
        this->speed = std::sqrt(this->vel.x * this->vel.x + this->vel.y * this->vel.y);
        if (this->speed > MAX_SPEED) {
            this->vel = (this->vel / this->speed) * MAX_SPEED;
            this->speed = MAX_SPEED; // Update speed after clamping
        }
    } else {
        // To avoid division by zero or extreme forces if a particle gets too close
        this->force = 0;
        this->speed = 0;
    }

    // Update position
    this->pos += this->vel;
}

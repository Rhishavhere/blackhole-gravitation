#pragma once
#include <SFML/System/Vector2.hpp>

class BlackHole; // Forward declaration to avoid circular dependency

class Particle {
public:
    sf::Vector2f pos;
    sf::Vector2f vel;
    float speed;
    float force;
    static const float MAX_SPEED;

    Particle(float x, float y);

    void update(const BlackHole& blackHole);
};

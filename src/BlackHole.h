#pragma once
#include <SFML/Graphics.hpp>

class BlackHole {
public:
    sf::Vector2f pos;
    float radius;
    sf::CircleShape shape;

    BlackHole(float x, float y);

    void update(sf::Vector2f mousePos);
    void draw(sf::RenderWindow& window);
};

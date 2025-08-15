#include "BlackHole.h"
#include "config.h"

BlackHole::BlackHole(float x, float y) : pos(x, y) {
    radius = BLACKHOLE_SIZE;
    shape.setRadius(radius);
    shape.setOrigin(radius, radius); // Set origin to the center for easy positioning
    shape.setFillColor(sf::Color::Black);
}

void BlackHole::update(sf::Vector2f mousePos) {
    this->pos = mousePos;
    shape.setPosition(this->pos);
}

void BlackHole::draw(sf::RenderWindow& window) {
    window.draw(shape);
}

#include <iostream>
#include <vector>
#include <random>
#include <cmath>

#include <SFML/Graphics.hpp>
#include "config.h"
#include "Particle.h"
#include "BlackHole.h"

// --- Color Utility Functions ---
// These functions replicate the color logic from the Python version.

sf::Color lerp(const sf::Color& a, const sf::Color& b, float t) {
    t = std::max(0.0f, std::min(1.0f, t)); // Clamp t to [0, 1]
    return sf::Color(
        static_cast<sf::Uint8>(a.r + (b.r - a.r) * t),
        static_cast<sf::Uint8>(a.g + (b.g - a.g) * t),
        static_cast<sf::Uint8>(a.b + (b.b - a.b) * t)
    );
}

sf::Color getColorBasedOnSpeed(float speed, float max_speed) {
    float ratio = speed / max_speed;
    // Gradient: Blue -> Magenta -> Red
    if (ratio < 0.5f) {
        return lerp(sf::Color::Blue, sf::Color::Magenta, ratio * 2.0f);
    } else {
        return lerp(sf::Color::Magenta, sf::Color::Red, (ratio - 0.5f) * 2.0f);
    }
}

sf::Color getColorBasedOnForce(float force) {
    // Force can vary greatly, so we use a log scale for better visual range
    float ratio = std::log(1.0f + force) / std::log(1.0f + 20.0f); // Normalize against an estimated max force
    // Gradient: White -> Yellow -> Orange
    return lerp(sf::Color::White, sf::Color(255, 165, 0), ratio);
}

// --- Particle Generation ---
Particle generate_particle() {
    static std::random_device rd;
    static std::mt19937 gen(rd());
    std::uniform_int_distribution<> edge_dist(0, 3);

    float x, y;
    int edge = edge_dist(gen);

    if (edge == 0) { // Top edge
        std::uniform_real_distribution<> x_dist(-WIDTH, WIDTH * 2);
        std::uniform_real_distribution<> y_dist(-HEIGHT, 0);
        x = x_dist(gen);
        y = y_dist(gen);
    } else if (edge == 1) { // Bottom edge
        std::uniform_real_distribution<> x_dist(-WIDTH, WIDTH * 2);
        std::uniform_real_distribution<> y_dist(HEIGHT, HEIGHT * 2);
        x = x_dist(gen);
        y = y_dist(gen);
    } else if (edge == 2) { // Left edge
        std::uniform_real_distribution<> x_dist(-WIDTH, 0);
        std::uniform_real_distribution<> y_dist(-HEIGHT, HEIGHT * 2);
        x = x_dist(gen);
        y = y_dist(gen);
    } else { // Right edge
        std::uniform_real_distribution<> x_dist(WIDTH, WIDTH * 2);
        std::uniform_real_distribution<> y_dist(-HEIGHT, HEIGHT * 2);
        x = x_dist(gen);
        y = y_dist(gen);
    }
    return Particle(x, y);
}


int main() {
    // --- Setup ---
    sf::RenderWindow window(sf::VideoMode(WIDTH, HEIGHT), "Black Hole Gravity Simulation | C++ & SFML");
    window.setFramerateLimit(FPS);

    BlackHole blackHole(WIDTH / 2.0f, HEIGHT / 2.0f);

    std::vector<Particle> particles;
    for (int i = 0; i < PARTICLE_DENSITY; ++i) {
        particles.push_back(generate_particle());
    }

    // VertexArray for efficient rendering
    sf::VertexArray particle_vertices(sf::Points, PARTICLE_DENSITY);

    // --- Main Loop ---
    while (window.isOpen()) {
        sf::Event event;
        while (window.pollEvent(event)) {
            if (event.type == sf::Event::Closed) {
                window.close();
            }
        }

        // --- Update ---
        sf::Vector2f mousePos = window.mapPixelToCoords(sf::Mouse::getPosition(window));
        blackHole.update(mousePos);

        for (size_t i = 0; i < particles.size(); ++i) {
            particles[i].update(blackHole);

            // Update vertex position
            particle_vertices[i].position = particles[i].pos;

            // Update vertex color
            if (COLOR_VARIATION == 1) {
                particle_vertices[i].color = getColorBasedOnForce(particles[i].force);
            } else if (COLOR_VARIATION == 2) {
                particle_vertices[i].color = getColorBasedOnSpeed(particles[i].speed, Particle::MAX_SPEED);
            } else {
                particle_vertices[i].color = sf::Color::White;
            }
        }


        // --- Draw ---
        window.clear(sf::Color(10, 10, 20)); // A dark blue instead of pure black

        // Draw all particles with a single draw call
        window.draw(particle_vertices);

        blackHole.draw(window);

        window.display();
    }

    return 0;
}

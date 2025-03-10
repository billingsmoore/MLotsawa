<?php
/**
 * Plugin Name: React Plugin
 * Description: Embeds the React app inside WordPress.
 */

function embed_react_app() {
    echo '<div id="react-root"></div>';
    echo '<script src="http://localhost:3000/static/js/bundle.js"></script>';
}
add_shortcode('react_component', 'embed_react_app');

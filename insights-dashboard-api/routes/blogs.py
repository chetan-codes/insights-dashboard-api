import json
import os
from flask import Blueprint, jsonify, send_from_directory


blogs = [

    {
    "title": 'This is simple blog',
    "subtitle": '2 comments, 1 Like',
    "subtext": 'This is a wider card with supporting text below as a natural lead-in to additional content.',
    "image": 'assets/images/bg/bg1.jpg'
    },
    {
    "title": 'This is simple blog',
    "subtitle": '2 comments, 1 Like',
    "subtext": 'This is a wider card with supporting text below as a natural lead-in to additional content.',
    "image": 'assets/images/bg/bg2.jpg'
    },
    {
    "title": 'This is simple blog',
    "subtitle": '2 comments, 1 Like',
    "subtext": 'This is a wider card with supporting text below as a natural lead-in to additional content.',
    "image": 'assets/images/bg/bg3.jpg'
    },
    {
    "title": 'This is simple blog',
    "subtitle": '2 comments, 1 Like',
    "subtext": 'This is a wider card with supporting text below as a natural lead-in to additional content.',
    "image": 'assets/images/bg/bg4.jpg'
 }

]

blog_routes = Blueprint('blogs', __name__)

# Define route for blogs API
@blog_routes.route('/api/blogs', methods=['GET'])
def get_blogs():
    # Return the blogs list as JSON
    return jsonify(blogs)


# Enhanced user storage with JSON file persistence
# This replaces the in-memory users_db with file-based storage

import json
import os
import hashlib
from flask import Flask, request, render_template, jsonify, session, redirect, url_for

# File to store user data
USERS_FILE = 'users.json'

def load_users():
    """Load users from JSON file"""
    if os.path.exists(USERS_FILE):
        try:
            with open(USERS_FILE, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            pass
    
    # Return default demo user if file doesn't exist
    return {
        'demo@healthcare.com': {
            'password': hashlib.sha256('demo123'.encode()).hexdigest(),
            'name': 'Demo User'
        }
    }

def save_users(users_data):
    """Save users to JSON file"""
    with open(USERS_FILE, 'w') as f:
        json.dump(users_data, f, indent=4)

# Helper function to verify login
def verify_login(email, password):
    users_db = load_users()
    if email in users_db:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return users_db[email]['password'] == hashed_password
    return False

# Helper function to register user
def register_user(email, password, name):
    users_db = load_users()
    if email not in users_db:
        users_db[email] = {
            'password': hashlib.sha256(password.encode()).hexdigest(),
            'name': name
        }
        save_users(users_db)
        return True
    return False

def get_user_name(email):
    """Get user name by email"""
    users_db = load_users()
    return users_db.get(email, {}).get('name', 'User')

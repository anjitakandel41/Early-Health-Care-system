# Example of how to integrate persistent storage
# Replace the user management section in main.py with this:

from user_storage import verify_login, register_user, get_user_name

# Login route
@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        if verify_login(email, password):
            session['logged_in'] = True
            session['user_email'] = email
            session['user_name'] = get_user_name(email)
            return jsonify({'success': True, 'message': 'Login successful!'})
        else:
            return jsonify({'success': False, 'message': 'Invalid email or password!'})

# Signup route
@app.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        name = request.form.get('name', 'User')
        
        if register_user(email, password, name):
            session['logged_in'] = True
            session['user_email'] = email
            session['user_name'] = name
            return jsonify({'success': True, 'message': 'Account created successfully!'})
        else:
            return jsonify({'success': False, 'message': 'Email already exists!'})

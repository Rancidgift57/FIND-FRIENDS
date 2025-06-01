# FindFriends

Find Friends is a web application that helps users connect with new friends based on common preferences such as hobbies,favorite foods and other preferences. The backend is built using Flask, while the frontend is developed with HTML, CSS, and JavaScript. The application also features email integration via Flask-Mail, allowing users to send and receive friend requests.

Key Features: Preference-Based Matching: Uses set union and intersection logic to match users based on shared hobbies and interests. Friend Requests via Email: Sends friend requests directly to users through email using Flask-Mail. Simple and Intuitive UI: Clean, easy-to-use interface built with HTML, CSS, and JavaScript. Technologies Used: Flask (Backend) HTML, CSS, JavaScript (Frontend) Flask-Mail (Email Integration) Feel free to customize it further if needed!

## Table of Contents

- Features
- Project Structure
- Technologies Used
- Prerequisites
- Setup Instructions
  - Local Setup
  - Environment Variables
  - Database Initialization
- Usage
  - Sign Up
  - Sign In
  - Find Matches
  - Send Friend Requests
- Matching Algorithm
- Deployment on Render
- Testing
- Troubleshooting
- Contributing
- Future Improvements
- License

## Features

- **User Registration**: Sign up with personal details (name, email, year, branch, hobbies, etc.) via a form.
- **Secure Login**: Email and password authentication with hashed passwords (`pbkdf2:sha256`).
- **Friend Matching**: Algorithm matches users based on hobbies (40%), preferences (50%), and location (10%).
- **Email Notifications**: Sends friend request emails to matched users using Flask-Mail.
- **Password Reset**: Basic password change functionality (via `form.html`).
- **Responsive UI**: Login page with animated overlay panels and Bootstrap-styled flash messages.
- **Logging**: Comprehensive error logging for debugging.
- **Render Deployment**: Compatible with Render for cloud hosting.

## Technologies Used

- **Backend**: Flask 3.1.0, Flask-Mail 0.10.0, Werkzeug 3.1.3
- **Database**: SQLite (`findfriends.db`)
- **Email**: Gmail SMTP via Flask-Mail
- **Security**: Password hashing with `pbkdf2:sha256`
- **Frontend**: HTML, CSS (`style.css`), Bootstrap 5.3.3, JavaScript
- **Environment**: Python-Dotenv 1.0.1 for environment variables
- **Deployment**: Gunicorn 23.0.0, Render
- **Logging**: Python `logging` module

## Prerequisites

- Python 3.8+
- Git
- SQLite
- Gmail account with an app password for email notifications
- Render account for deployment (optional)
- Text editor (e.g., VS Code)
- Terminal or command prompt

## Setup Instructions

### Local Setup

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/findfriends.git
   cd findfriends
   ```

2. **Create a Virtual Environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**: Ensure `requirements.txt` contains:

   ```
   flask==3.1.0
   flask-mail==0.10.0
   werkzeug==3.1.3
   gunicorn==23.0.0
   python-dotenv==1.0.1
   ```

   Install them:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**: Create a `.env` file in the root directory:

   ```
   MAIL_USERNAME=your-email@gmail.com
   MAIL_PASSWORD=your-gmail-app-password
   SECRET_KEY=your-secret-key
   ```

   - **Gmail App Password**: Generate via Gmail’s 2-Step Verification settings.
   - **Secret Key**: A random string for Flask session security.

5. **Initialize the Database**: Run `import_csv.py` to populate `findfriends.db` with sample users:

   ```bash
   python import_csv.py
   ```

   - This creates the `friendfind` table and inserts 31 users with hashed passwords.
   - Save the printed raw passwords for testing.

6. **Run the Application**:

   ```bash
   python app.py
   ```

   Access the app at `http://localhost:5000`.

### Environment Variables

| Variable | Description | Example Value |
| --- | --- | --- |
| `MAIL_USERNAME` | Gmail address for sending emails | `nnair7598@gmail.com` |
| `MAIL_PASSWORD` | Gmail app password | `abcd-efgh-ijkl-mnop` |
| `SECRET_KEY` | Flask secret key for sessions | `your-secure-random-string` |

### Database Initialization

The `friendfind` table schema:

```sql
CREATE TABLE friendfind (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT UNIQUE,
    year TEXT,
    branch TEXT,
    prn TEXT,
    residing_pincode TEXT,
    first_hobby TEXT,
    second_hobby TEXT,
    third_hobby TEXT,
    favorite_food TEXT,
    social_media_usage TEXT,
    community_involvement TEXT,
    travel_destinations TEXT,
    preferred_gadget TEXT,
    physical_well_being TEXT,
    mental_well_being TEXT,
    creative_activities TEXT,
    future_goals TEXT,
    password TEXT
);
```

- Populated via `import_csv.py`.
- Passwords are hashed using `pbkdf2:sha256`.

## Usage

### Sign Up

1. Navigate to `http://localhost:5000/signup` or click “Sign Up” on the login page.
2. Fill out the form in `googleform.html` with:
   - Name, email, password (required)
   - Year (FE, SE, TE, BE)
   - Branch (AIML, Computer, EXTC, etc.)
   - PRN, pincode, hobbies, preferences
3. Submit to create a user profile.
4. On success, you’re redirected to the login page with a “Sign-up successful!” message.

### Sign In

1. Go to `http://localhost:5000`.
2. Enter your email and password in the sign-in form.
3. Submit to access the homepage.
   - Valid credentials redirect to `/homepage`.
   - Invalid credentials show flash messages (e.g., “Invalid password”).

### Find Matches

- After login, the `find_friends` function generates matches based on your profile.
- Matches are written to:
  - `/tmp/FINDFRIENDS.txt`: All matches with compatibility scores.
  - `/tmp/FINDFRIENDS2.txt`: Highest match.
  - `/tmp/FINDFRIENDS3.txt`: Match names.
  - `/tmp/match_1.txt`, `/tmp/match_2.txt`, `/tmp/match_3.txt`: Emails of top 3 matches.

### Send Friend Requests

- Access the following routes to send friend request emails to matches:
  - `http://localhost:5000/send-emails` (first match)
  - `http://localhost:5000/send-emailsw` (second match)
  - `http://localhost:5000/send-emailsr` (third match)
- Emails are sent via Gmail SMTP with the subject “Friend Request on Find Friends”.

## Matching Algorithm

The `find_friends` function calculates compatibility between users:

- **Inputs**: User profiles from the `friendfind` table.
- **Components**:
  - **Hobbies (40%)**: Compares three hobbies using exact matches and word overlap.
  - **Preferences (50%)**: Evaluates favorite food, social media usage, community involvement, travel destinations, gadgets, well-being, creative activities, and goals using word overlap or ordinal similarity.
  - **Location (10%)**: Matches based on residing pincode.
- **Output**: Top 3 matches with compatibility scores (0-100%).

## Deployment on Render

1. **Push to GitHub**:

   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Create Render Web Service**:

   - Sign in to Render.
   - Create a new Web Service, linking your GitHub repository.
   - Configure:
     - **Runtime**: Python
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `gunicorn app:app`
     - **Environment Variables**:
       - `MAIL_USERNAME`: Your Gmail address
       - `MAIL_PASSWORD`: Your Gmail app password
       - `SECRET_KEY`: Your secret key

3. **Upload Database**:

   - Commit `findfriends.db` to the repository or run `import_csv.py` on Render via a one-off dyno:

     ```bash
     python import_csv.py
     ```

4. **Deploy**:

   - Trigger a deploy from the Render dashboard.
   - Access the app at `https://your-app-name.onrender.com`.

5. **Verify**:

   - Test sign-up, sign-in, and friend request emails.
   - Check Render logs for errors.

## Testing

### Local Testing

1. **Sign Up**:
   - Submit a new user via `/signup`.
   - Verify redirect to `/` with a success message.
   - Check `findfriends.db` for the new user (`SELECT * FROM friendfind`).
2. **Sign In**:
   - Use a CSV user’s email and raw password (from `import_csv.py`).
   - Test invalid email (`test@invalid.com` → “Email not found”).
   - Test wrong password (“Invalid password”).
   - Confirm `/homepage` loads with valid credentials.
3. **Matches**:
   - Check `/tmp/FINDFRIENDS.txt` and `/tmp/match_*.txt` after login.
4. **Emails**:
   - Trigger `/send-emails`, `/send-emailsw`, `/send-emailsr`.
   - Verify emails in your Gmail “Sent” folder or recipient inboxes.
5. **Password Reset**:
   - Submit `oldpass` and `rewritepass` via `/form`.
   - Check success/error messages.

### Render Testing

- Repeat local tests on the Render URL.
- Monitor Render logs for database or SMTP errors.
- Ensure `/tmp/` is writable (Render’s filesystem supports it).

## Troubleshooting

- **Login Fails**:
  - **Symptom**: “Invalid password” or “Email not found” alerts.
  - **Fix**:
    - Verify email/password in `findfriends.db` (`SELECT email, password FROM friendfind`).
    - Use raw passwords from `import_csv.py`.
    - Check `app.py` for correct `find_friends` call.
- **No Flash Messages**:
  - **Symptom**: No alerts on `login.html`.
  - **Fix**:
    - Ensure `{% with messages = get_flashed_messages(with_categories=true) %}` is in `login.html`.
    - Confirm Bootstrap CSS/JS is loaded.
- **Database Errors**:
  - **Symptom**: `Database error` in logs.
  - **Fix**:
    - Run `import_csv.py` to repopulate `findfriends.db`.
    - Check SQLite file permissions.
- **Email Sending Fails**:
  - **Symptom**: `SMTPAuthenticationError` or no emails sent.
  - **Fix**:
    - Verify `MAIL_USERNAME` and `MAIL_PASSWORD` in `.env` or Render.
    - Ensure Gmail app password is correct.
    - Check Gmail security settings.
- **Matches Not Generated**:
  - **Symptom**: Empty `/tmp/FINDFRIENDS.txt`.
  - **Fix**:
    - Confirm at least two users in `friendfind` table.
    - Check `/tmp/` permissions on Render.
- **Render Deployment Issues**:
  - **Symptom**: App crashes or 500 errors.
  - **Fix**:
    - Review Render logs.
    - Ensure `gunicorn` and dependencies are installed.
    - Verify `findfriends.db` is present.

## Contributing

1. Fork the repository.
2. Create a feature branch:

   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit changes:

   ```bash
   git commit -m "Add your feature"
   ```
4. Push to the branch:

   ```bash
   git push origin feature/your-feature
   ```
5. Open a pull request with a detailed description.

## Future Improvements

- **Real-Time Chat**: Add Flask-SocketIO for messaging between matches.
- **Enhanced UI**: Use Bolt AI to design modern interfaces for all pages.
- **Session Management**: Implement `flask.session` for persistent logins.
- **Profile Pictures**: Allow image uploads for user profiles.
- **Notifications**: Add in-app notifications for friend requests.
- **Advanced Matching**: Incorporate machine learning for better compatibility.
- **Mobile App**: Develop iOS/Android apps using Flutter or React Native.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

**Contact**: For issues or suggestions, open a GitHub issue or contact the maintainer at `nnair855@gmail.com`.

**Last Updated**: June 1, 2025

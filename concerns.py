class UserManager:
    def create_user(self, username, password):
        # Input validation mixed with business logic and UI
        if len(username) < 3:
            print("Error: Username too short")
            return False
        
        # Database logic mixed with business logic
        connection = mysql.connector.connect(host='localhost', database='mydb')
        cursor = connection.cursor()
        
        # HTML generation mixed with business logic
        cursor.execute(f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')")
        connection.commit()
        
        # Email sending mixed with business logic
        import smtplib
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.send_message(f"Welcome {username}!")
        
        return f"""
        <html>
            <body>
                <h1>User created successfully!</h1>
                <p>Welcome, {username}</p>
            </body>
        </html>
        """

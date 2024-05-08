from datetime import datetime
import mysql.connector
import databaseConnection as dbc


def generate_unique_email(full_name):
    current_year = str(datetime.now().year)
    name_parts = full_name.split()
    first_name = name_parts[0]
    last_name = name_parts[-1]
    email = f"{first_name}.{last_name}.{current_year}@Aiu.edu.eg"

    conn = dbc.connect_to_db()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT COUNT(*) FROM Student WHERE Email = %s", (email,))
        count = cursor.fetchone()[0]

        if count == 0:
            cursor.close()
            conn.close()
            return email
        else:
            new_full_name = ' '.join(name_parts[:-1])
            return generate_unique_email(new_full_name)
    except mysql.connector.Error as e:
        print(f"Error checking for unique email: {e}")
        return None
    finally:
        cursor.close()
        conn.close()

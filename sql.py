import mysql.connector
import pandas as pd
import streamlit as st

# Function to fetch data from MySQL
def get_data():
    try:
        # Connect to MySQL database
        connection = mysql.connector.connect(
            host="localhost",         # Change to your MySQL host
            database="students_db",   # Your MySQL database name
            user="your_user",         # Replace with your MySQL username
            password="your_password"  # Replace with your MySQL password
        )
        
        cursor = connection.cursor()
        query = """
        SELECT 
            s.length_of_stay,
            AVG(sv.diagnostic_score) AS avg_diagnostic_score,
            AVG(sv.stress_level) AS avg_stress,
            AVG(sv.anxiety_level) AS avg_anxiety,
            AVG(sv.depression_level) AS avg_depression
        FROM 
            Students s
        JOIN 
            Surveys sv ON s.student_id = sv.student_id
        GROUP BY 
            s.length_of_stay
        ORDER BY 
            s.length_of_stay;
        """
        cursor.execute(query)
        result = cursor.fetchall()
        
        # Convert result to pandas DataFrame for better presentation
        df = pd.DataFrame(result, columns=["Length of Stay (years)", "Average Diagnostic Score", "Average Stress", "Average Anxiety", "Average Depression"])
        
        cursor.close()
        connection.close()
        
        return df
    
    except mysql.connector.Error as err:
        st.error(f"Error connecting to database: {err}")
        return None

# Streamlit App UI
def main():
    st.title("Student Mental Health Analysis")
    
    # Display a description of the app
    st.write("""
    This app analyzes how the **length of stay** impacts the **mental health diagnostic scores** 
    of international students. It fetches data from a MySQL database and displays the results below.
    """)
    
    # Fetch the data from MySQL and display it in a table
    data = get_data()
    
    if data is not None:
        st.write("### Average Diagnostic Scores by Length of Stay")
        st.dataframe(data)  # Display the result as a table
        
        # Plotting the data (optional)
        st.write("### Plot of Average Diagnostic Scores")
        st.bar_chart(data.set_index("Length of Stay (years)")["Average Diagnostic Score"])

# Run the Streamlit app
if __name__ == "__main__":
    main()


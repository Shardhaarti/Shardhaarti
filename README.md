-- Step 1: Create a new database (if not already created)
CREATE DATABASE students_db;

-- Step 2: Switch to the newly created database
USE students_db;


-- Create Students table
CREATE TABLE Students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    nationality VARCHAR(100),
    age INT,
    gender VARCHAR(10),
    length_of_stay INT  -- Length of stay in years
);

-- Create Surveys table (mental health data)
CREATE TABLE Surveys (
    survey_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    diagnostic_score INT,  -- Mental health diagnostic score (0-100)
    stress_level INT,      -- Stress level from 1-10
    anxiety_level INT,     -- Anxiety level from 1-10
    depression_level INT,  -- Depression level from 1-10
    social_isolation BOOLEAN, -- Whether the student feels isolated (True/False)
    survey_date DATE,
    FOREIGN KEY (student_id) REFERENCES Students(student_id)
);
-- Insert data into Students table
INSERT INTO Students (name, nationality, age, gender, length_of_stay) VALUES
('Alice', 'Japan', 21, 'Female', 2),
('Bob', 'USA', 22, 'Male', 1),
('Cathy', 'India', 23, 'Female', 3),
('David', 'Brazil', 24, 'Male', 1),
('Eva', 'Germany', 25, 'Female', 4);

-- Insert data into Surveys table
INSERT INTO Surveys (student_id, diagnostic_score, stress_level, anxiety_level, depression_level, social_isolation, survey_date) VALUES
(1, 75, 5, 3, 2, FALSE, '2025-01-10'),
(2, 68, 7, 6, 4, TRUE, '2025-02-15'),
(3, 80, 4, 2, 1, FALSE, '2025-03-01'),
(4, 55, 8, 7, 6, TRUE, '2025-03-10'),
(5, 85, 3, 1, 1, FALSE, '2025-03-25');
-- Query to calculate the average diagnostic score based on the length of stay
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


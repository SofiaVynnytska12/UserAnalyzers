-- Create user Analyzer with full privileges
CREATE USER 'Analyzer'@'%' IDENTIFIED BY 'UA';
GRANT ALL PRIVILEGES ON *.* TO 'Analyzer'@'%' WITH GRANT OPTION;

-- Create user UserAnalyzers with limited privileges
CREATE USER 'UserAnalyzers'@'%' IDENTIFIED BY 'UA';
GRANT ALL PRIVILEGES ON UserAnalyzers.* TO 'UserAnalyzers'@'%';

-- Apply the changes
FLUSH PRIVILEGES;

docker exec -it mysql-container mysql -uAnalyzer; -pUA 
docker exec -it mysql-container mysql -uUserAnalyzers; -pUA 

pipeline {
    agent any

    stages {
        

        stage('Checkout') {
            steps {
                // Check out the repository with a specific refspec
                git "https://github.com/gunjanpanda/jenkinspipeline_python_jira_creation"
                
            }
        }

        stage('Run Python Script') {
            steps {
                // Run your Python script
                script {
                    sh 'python issue_creation.py'
                }
            }
        }

        
    }
}
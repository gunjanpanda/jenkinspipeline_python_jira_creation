pipeline {
    agent any

    stages {
        

        stage('Checkout') {
            steps {
                script {
                    // Check out the repository with a specific refspec
                    checkout([$class: 'GitSCM',
                              branches: [[name: 'refs/heads/main']], // Adjust the branch name
                              doGenerateSubmoduleConfigurations: false,
                              extensions: [[$class: 'CleanCheckout']],
                              submoduleCfg: [],
                              userRemoteConfigs: [[url: 'https://github.com/gunjanpanda/jenkinspipeline_python_jira_creation.git']]])
                }
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
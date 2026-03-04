pipeline {
agent any
stages {
stage('Checkout Code') {
steps {
git 'https://github.com/your-repo/sample-project.git'
}
}
stage('Build') {
steps {
sh 'javac Main.java' // Example build step for Java
}
}
stage('Test') {
steps {
sh 'java Main' // Running the compiled Java program
}
}
stage('Deploy') {
steps {
echo 'Deploying application...'
}
}
}
}
